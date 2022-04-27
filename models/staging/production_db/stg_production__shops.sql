with src_shops as (
    select * from {{ source('production_db', 'shops') }}
),

final as (
    select
        id,
        address,
        city,
        province,
        country,
        postal_code,
        latitude,
        longitude
    from src_shops
)

select * from final
