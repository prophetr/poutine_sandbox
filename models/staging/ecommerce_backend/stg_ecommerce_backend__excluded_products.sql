with all_products as (
    select * from {{ ref('stg_ecommerce_backend__all_products') }}
),

final as (
    select
        product_id,
        distribution_center_id,
        cost,
        category,
        name,
        brand,
        retail_price,
        department,
        sku

    from all_products
    where product_id in (
        -- records with null sku
        425,
        1009,
        8903,
        29000,
        100,
        -- records with non-unique sku code
        18166,
        683,
        14717,
        27398,
        -- record with no matching distribution centers relationship
        11033
    )
)

select * from final
