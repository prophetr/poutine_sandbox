with order_items as (

    select * from {{ ref('stg_transactions__order_items') }}

),

customers as (

    select * from {{ ref('stg_production__customers') }}

),

orders as (

    select * from {{ ref('stg_transactions__orders') }}

),

final as (

    select
        -- surrogate key
        {{ dbt_utils.surrogate_key(['order_items.order_item_unique_sk',
            'order_items.order_id']) 
        }} as orders_sk,

        --foreign key
        order_items.order_item_unique_sk,
        order_items.order_id,
        order_items.product_id,
        order_items.customer_id,

        --facts
        order_items.quantity as order_quantity,
        order_items.product_cost,
        order_items.subtotal,
        orders.order_tax,
        orders.order_total,

        -- timestamps
        order_items.order_created_at

    from order_items
    left join customers
        on order_items.customer_id = customers.customer_id
    left join orders
        on order_items.order_id = orders.order_id

)

select * from final
