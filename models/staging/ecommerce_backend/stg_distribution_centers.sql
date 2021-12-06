with distribution_centers as (
    select * from {{ source('ecommerce_backend', 'distribution_centers') }}
),

final as (
    select
        id as distribution_center_id,
        name as location_name,
        latitude,
        longitude

    from distribution_centers
)

select * from final
