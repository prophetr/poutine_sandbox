with src_orders as (
    select * from {{ source('transactions', 'orders') }}
),

final as (
    select
        order_id,
        customer_id,
        quantity as order_quantity,
        subtotal as order_subtotal,
        tax as order_tax,
        total as order_total,
        created_at as order_created_at
    from src_orders
    qualify
        row_number() over (
            partition by
                order_id,
                customer_id,
                quantity,
                subtotal,
                tax,
                total,
                created_at
            order by created_at desc
        ) = 1
)

select * from final
