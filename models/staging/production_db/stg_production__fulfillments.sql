with src_fulfillments as (
    select * from {{ source('production_db', 'fulfillment') }}
),

final as (
    select
        order_id,
        customer_id,
        created_at,
        event_id,
        event_name
    from src_fulfillments
)

select * from final
