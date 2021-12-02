with distribution_centers as (
    select
        id as distribution_center_id,
        name as location_name,
        latitude,
        longitude
    from {{ source('ecommerce_backend', 'distribution_centers') }}
)

select * from distribution_centers
