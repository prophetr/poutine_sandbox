{% macro update_dev_clone(schemas = null, target_db = var('dev_db')) -%}
{# This macro creates or updates a development schema within a dev database (by default)
    Schema name generation depends on target and schema defined in the .dbt/profiles.yml
    All schemas will be nested within target.schema and custom schema names ignore when target!=prod 

    Allocating both individual schemas and different target database is possible, 
    though these arguments default to all schemas within prod (save for 'information_schema' and public)
    and the dev_db variable within dbt_project.yml
#}

    {% if target_db != var("prod_db") %}
        {%- if schemas == null -%}
        {# Go and get every schema that lives within the production db when a schema list is not provided #}
            {%- set query -%}
                select SCHEMA_NAME from {{var("prod_db")}}.INFORMATION_SCHEMA.SCHEMATA 
                where SCHEMA_NAME not in ('INFORMATION_SCHEMA','PUBLIC')
            {% endset %}
            {% if execute %}
                {% set results = run_query(query) %}
                {% set schemas = results.columns[0] %}
            {% endif %}
        {%- endif -%}

        {%- set sql -%}
        CREATE TRANSIENT DATABASE IF NOT EXISTS {{target_db}};
            {% for schema in schemas -%}
                CREATE OR REPLACE TRANSIENT SCHEMA {{target_db}}.{{generate_schema_name(schema)}} CLONE {{var("prod_db")}}.{{schema}}; 
            {%- endfor %} 
        {% endset %}

        {% do run_query(sql) %}
        {{ log('Cloned '~schemas~' to '~target_db~' from production', info=True) }}

    {% endif -%}

{% endmacro %}

{% macro update_prod_clone(schemas) -%}
{# This macro creates a sandbox database based on the production database, with selectively cloning schemas provided #}

    {%- if target.database == var('prod_db') -%}
        CREATE OR REPLACE TRANSIENT DATABASE {{var("prod_clone_db")}};
        GRANT ALL PRIVILEGES ON DATABASE {{var("prod_clone_db")}} TO ROLE {{var("dev_role")}};

        {% for schema_name in schemas %}
            {{clone_schema_from_prod(clone_db, var("prod_db"), schema_name, role_to_own)}}
        {% endfor %}

        USE DATABASE {{ target.database }};

    {%- else -%}
        SELECT 1

    {%- endif -%}

{%- endmacro %}

{% macro clone_schema_from_prod(schema_name) -%}
{# This macro is called to copy individual schemas within update_prod_clone #}
    CREATE OR REPLACE TRANSIENT SCHEMA
        {{var("prod_clone_db")}}.{{generate_schema_name(schema_name)}}
        CLONE {{var("prod_db")}}.{{schema_name}};

    GRANT ALL PRIVILEGES ON SCHEMA
        {{var("prod_clone_db")}}.{{generate_schema_name(schema_name)}}
        TO ROLE {{var("dev_role")}};

    GRANT OWNERSHIP ON ALL TABLES IN SCHEMA
        {{var("prod_clone_db")}}.{{generate_schema_name(schema_name)}}
        TO ROLE {{var("dev_role")}} REVOKE CURRENT GRANTS;
    
    GRANT OWNERSHIP ON ALL VIEWS IN SCHEMA
        {{var("prod_clone_db")}}.{{generate_schema_name(schema_name)}}
        TO ROLE {{var("dev_role")}} REVOKE CURRENT GRANTS;

{%- endmacro %} 
