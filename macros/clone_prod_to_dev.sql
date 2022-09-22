{% macro update_prod_clone(schemas) -%}

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

{% macro update_dev_clone(target_db, schemas) -%}

    {%- if "{{target_db}}" != var("prod_db") -%}
        CREATE TRANSIENT DATABASE IF NOT EXISTS {{target.database}};
        {% for schema_name in schemas %}
            CREATE OR REPLACE TRANSIENT SCHEMA {{target.database}}.{{generate_schema_name(schema_name)}} CLONE {{var("prod_clone_db")}}.{{schema_name}};
        {% endfor %}

    {%- else -%}
        CAREFUL! YOU RAN THE clone_schemas_to_target_db() macro AGAINST PROD -- FORCED ERROR

    {%- endif -%}

{%- endmacro %}
