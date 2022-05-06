with fulfillments as (
    select * from {{ ref('stg_production__fulfillments') }}
),

customers as (
    select * from {{ ref('stg_production__customers') }}
),

orders as (
    select * from {{ ref('stg_transactions__orders') }}
),

final as (
    select
        -- primary key
        fulfillment_event_id,

        -- foreign keys
        fulfillments.order_id,
        fulfillments.customer_id,

        -- dates & timestamps
        created_at,

        -- details
        event_name

        -- metrics: TODO would be intereting to have a most_recent_order snapshot

    from fulfillments
    left join customers
        on fulfillments.customer_id = customers.customer_id
    left join orders
        on fulfillments.order_id = orders.order_id
)

select * from final


