{% macro clone_schema_for_prod_clone(schema_name) -%}
    create or replace transient schema
        {{ var("prod_clone_db") }}.{{ generate_schema_name(schema_name) }}
        clone {{ var("prod_db") }}.{{ schema_name }};

    grant all privileges on schema
        {{ var("prod_clone_db") }}.{{ generate_schema_name(schema_name) }}
        to role {{ var("dev_role") }};

    grant ownership on all tables in schema
        {{ var("prod_clone_db") }}.{{ generate_schema_name(schema_name) }}
        to role {{ var("dev_role") }} revoke current grants;
    
    grant ownership on all views in schema
        {{ var("prod_clone_db") }}.{{ generate_schema_name(schema_name) }}
        to role {{ var("dev_role") }} revoke current grants;

{%- endmacro %} 
