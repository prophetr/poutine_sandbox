with src_customer as (
    select * from {{ source('snowflake_sample_data', 'customer') }}
),

final as (
    select
        -- primary key
        c_customer_sk as customer_sk,
        c_customer_id as customer_id,

        -- dimensions
        c_first_name as first_name

    from src_customer

)

select * from final
