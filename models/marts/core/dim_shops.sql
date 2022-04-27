with shops as (
    select * from {{ ref('stg_production__shops') }}
),

final as (
    select
        --primary key
        shops.id as shop_id,

        --dimensions
        shops.address,
        shops.city,
        shops.province,
        shops.country,
        shops.postal_code,
        shops.latitude,
        shops.longitude

    from shops
)

select * from final
