with order_items as (
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
    from {{ source('ecommerce_backend','order_items') }}
)

select * from order_items
