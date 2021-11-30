with events as (
    select
        id as event_id,
        sequence_number,
        session_id,
        created_at,
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
        user_id,
        uri,
        event_type
    from {{ source('snowlooker', 'events') }}
)

select * from events
