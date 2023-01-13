with src_date as (
    select * from {{ source('snowflake_sample_data', 'date_dim') }}
),

final as (
    select
        -- primary key
        d_date_sk as date_sk,
        d_date_id as date_id,

        -- date
        d_date as standard_date

    from src_date

)

select * from final
