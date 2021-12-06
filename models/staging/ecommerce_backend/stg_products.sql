with products as (
    select * from {{ source('ecommerce_backend', 'products') }}
),

final as (
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

    from products
    where product_id not in (
        11033, 425, 1009, 8903, 29000, 100, 18166, 683, 14717, 27398)
)

select * from final
