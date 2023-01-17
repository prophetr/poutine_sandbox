with src_store_sales as (
    select * from {{ source('snowflake_sample_data', 'store_sales') }}
),

final as (
    select
        -- primary key
        {{ dbt_utils.surrogate_key(['ss_ticket_number', 'ss_item_sk']) }} as store_sales_id,

        -- foreign keys
        ss_sold_date_sk as sold_date_id,
        ss_sold_time_sk as sold_time_id,
        ss_customer_sk as customer_id,
        ss_cdemo_sk as cdemo_id,
        ss_hdemo_sk as hdemo_id,
        ss_addr_sk as addr_id,
        ss_store_sk as store_id,
        ss_item_sk as item_id,
        ss_promo_sk as promo_id,
        ss_ticket_number as ticket_number,

        -- details
        ss_quantity as quantity,
        ss_wholesale_cost as wholesale_cost,
        ss_list_price as list_price,
        ss_sales_price as sales_price,
        ss_ext_discount_amt as ext_discount_amt,
        ss_ext_sales_price as ext_sales_price,
        ss_ext_wholesale_cost as ext_wholesale_cost,
        ss_ext_list_price as ext_list_price,
        ss_ext_tax as ext_tax,
        ss_coupon_amt as coupon_amt,
        ss_net_paid as net_paid,
        ss_net_paid_inc_tax as net_paid_inc_tax,
        ss_net_profit as net_profit

    from src_store_sales
    where sold_date_id >= 2452634
)

select * from final
