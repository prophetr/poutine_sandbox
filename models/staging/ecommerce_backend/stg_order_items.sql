with order_items as (
    select * from {{ source('ecommerce_backend','order_items') }}
),

final as (
    select
        id as order_item_id,
        order_id,
        user_id,
        inventory_item_id,
        sale_price,
        status,
        created_at,
        returned_at,
        shipped_at,
        delivered_at
        
    from order_items
    where order_item_id not in (298433, 56567, 68410, 84202, 289395)
)

select * from final
