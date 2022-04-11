with src_customers as (
    select * from {{ source('production_db', 'customers') }}
),

final as (
    select
        customer_id,
        name as customer_name,
        birthdate as customer_birth_date,
        city as customer_city,
        state as customer_state,
        zipcode as customer_zip_code,
        "phone-number" as customer_phone_number,
        email as customer_email,
        gender
    from src_customers
)

select * from final
