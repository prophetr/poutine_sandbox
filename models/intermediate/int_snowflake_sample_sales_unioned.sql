with catalog_sales as (
    select * from {{ ref('stg_snowflake_sample__catalog_sales') }}
),

store_sales as (
    select * from {{ ref('stg_snowflake_sample__store_sales') }}
),

web_sales as (
    select * from {{ ref('stg_snowflake_sample__web_sales') }}
),

unioned as (

    {{ 
        dbt_utils.union_relations(
            relations=[
                ref('stg_snowflake_sample__catalog_sales'), 
                ref('stg_snowflake_sample__store_sales'), 
                ref('stg_snowflake_sample__web_sales')
            ]
        ) 
    }}


),

final as (

    select
        coalesce(catalog_sales_id, store_sales_id, web_sales_id) as sales_id,
        coalesce(order_number, ticket_number) as sales_order_number,
        *
    from unioned

)

select * from final
