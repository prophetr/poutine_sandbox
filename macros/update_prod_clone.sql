{% macro update_prod_clone(schemas) -%}

    {%- if target.database == var('prod_db') -%}
        create or replace transient database {{ var("prod_clone_db") }};
        grant all privileges on database {{ var("prod_clone_db") }} to role {{ var("dev_role") }};

        {% for schema_name in schemas %}
            {{ clone_schema_for_prod_clone(schema_name) }}
        {% endfor %}

        use database {{ target.database }};

    {%- else -%}
        SELECT 1

    {%- endif -%}

{%- endmacro %}
