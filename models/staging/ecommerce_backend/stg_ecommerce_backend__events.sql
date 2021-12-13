with events as (
    select * from {{ source('ecommerce_backend', 'events') }}
),

final as (
    select

        -- primary key
        id as event_id,

        -- foreign key
        user_id,

        -- details
        sequence_number,
        session_id,
        ip_address,
        city,
        state,
        country,
        zip,
        latitude,
        longitude,
        os,
        browser,
        traffic_source,
        uri,
        event_type,

        -- dates & timestamps
        created_at

    from events
)

select * from final
