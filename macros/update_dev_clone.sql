{% macro update_dev_clone(schemas = null, target_db = var('dev_db')) -%}
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
        create transient database if not exists {{target_db}};
            {% for schema in schemas -%}
                create or replace transient schema {{ target_db }}.{{ generate_schema_name(schema) }} clone {{ var("prod_db") }}.{{ schema }}; 
            {%- endfor %} 
        {% endset %}

        {% do run_query(sql) %}
        {{ log('Cloned '~schemas~' to '~target_db~' from production', info=True) }}

    {% endif -%}

{% endmacro %}
