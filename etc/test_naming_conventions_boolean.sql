{{
    config(
        severity='warn',
        tags = 'naming_convention'
    )
}}

select
    table_name as model,
    column_name

from {{ target.database }}.INFORMATION_SCHEMA.COLUMNS
where table_schema = '{{ target.schema }}'
    and data_type = 'BOOLEAN'
    and regexp_substr(lower(column_name), '^has_') is null
    and regexp_substr(lower(column_name), '^is_') is null
