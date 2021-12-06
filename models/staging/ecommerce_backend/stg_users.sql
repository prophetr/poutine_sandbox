with users as (
    select * from {{ source('ecommerce_backend','users') }}
),

final as (
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
        
    from users
)

select * from final
