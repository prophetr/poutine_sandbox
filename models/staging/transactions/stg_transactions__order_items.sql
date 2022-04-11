with src_order_items as (
    select * from {{ source('transactions', 'order_items') }}
),

final as (
    select 
        {{ dbt_utils.surrogate_key(['order_id', 'product_id']) }} as order_item_unique_sk,
        order_id,
        product_id,
        customer_id,
        quantity,
        name as product_name,
        cost as product_cost,
        subtotal,
        created_at as order_created_at
    from src_order_items
)

select * from final
