
-- This model will be created in the database with the identifier `products`
-- Note that `alias` is used along with a custom schema
{{ config(alias='products', schema='raw_data') }}

with all_products as (
    select * from {{ source('ecommerce_backend', 'products') }}
),

final as (
    select
        id as product_id,
        distribution_center_id,
        cost,
        category,
        name,
        brand,
        retail_price,
        department,
        sku

    from all_products
)

select * from final
