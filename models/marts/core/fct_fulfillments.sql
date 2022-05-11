with fulfillments as (
    select * from {{ ref('stg_production__fulfillments') }}
),

orders as (
    select * from {{ ref('stg_transactions__orders') }}
),

final as (
    select
        -- primary key
        fulfillments.fulfillment_event_id,

        -- foreign keys
        fulfillments.order_id,
        fulfillments.customer_id,

        -- dates & timestamps
        fulfillments.created_at,

        -- details
        fulfillments.event_name

    from fulfillments
    left join orders
        on fulfillments.order_id = orders.order_id
)

select * from final
