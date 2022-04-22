with users as (
    select * from {{ source('ecommerce_backend','users') }}
),

final as (
    select
        -- primary key
        id as user_id,

        -- details
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
        traffic_source,

        -- dates & timestamps
        created_at

    from users
)

select * from final
