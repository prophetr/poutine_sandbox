with products as (
    select
        id as product_id,
        cost,
        category,
        name as product_name,
        brand,
        retail_price,
        department,
        sku,
        distribution_center_id
    from {{ source('ecommerce_backend', 'products') }}
)

select * from products
