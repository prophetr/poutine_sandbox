with users as (
    select
        id as user_id,
        first_name,
        last_name,
        email,
        age,
        city,
        state,
        country,
        zip,
        latitude,
        longitude,
        gender,
        created_at,
        traffic_source
    from {{ source('ecommerce_backend','users') }}
)

select * from users
