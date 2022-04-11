with src_products as (
    select * from {{ source('production_db', 'products') }}
),

final as (
    select
        product_id,
        name as product_name,
        cost as product_cost,
        description as product_description,
        size as product_size,
        type as product_type
    from src_products
)

select * from final
