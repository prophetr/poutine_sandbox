with inventory_items as (
    select * from {{ source('ecommerce_backend', 'inventory_items') }}
),

final as (
    select
        id as inventory_item_id,
        product_id,
        created_at,
        sold_at,
        cost,
        product_category,
        product_name,
        product_brand,
        product_retail_price,
        product_department,
        product_sku,
        product_distribution_center_id

    from inventory_items
    where inventory_item_id not in (288038, 218960, 325238, 45766, 99912)
)

select * from final
