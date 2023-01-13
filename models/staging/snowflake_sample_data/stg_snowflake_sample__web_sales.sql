with src_web_sales as (
    select * from {{ source('snowflake_sample_data', 'web_sales') }}
),

final as (
    select
        -- primary key
        {{ dbt_utils.surrogate_key(['ws_order_number', 'ws_item_sk']) }} as web_sales_id,

        -- foreign keys
        ws_sold_date_sk as sold_date_id,
        ws_sold_time_sk as sold_time_id,
        ws_ship_date_sk as ship_date_id,
        ws_bill_customer_sk as bill_customer_id,
        ws_bill_cdemo_sk as bill_cdemo_id,
        ws_bill_hdemo_sk as bill_hdemo_id,
        ws_bill_addr_sk as bill_addr_id,
        ws_ship_customer_sk as ship_customer_id,
        ws_ship_cdemo_sk as ship_cdemo_id,
        ws_ship_hdemo_sk as ship_hdemo_id,
        ws_ship_addr_sk as ship_addr_id,
        ws_web_page_sk as web_page_id,
        ws_web_site_sk as web_site_id,
        ws_ship_mode_sk as ship_mode_id,
        ws_warehouse_sk as warehouse_id,
        ws_item_sk as item_id,
        ws_promo_sk as promo_id,
        ws_order_number as order_number,

        -- details
        ws_quantity as quantity,
        ws_wholesale_cost as wholesale_cost,
        ws_list_price as list_price,
        ws_sales_price as sales_price,
        ws_ext_discount_amt as ext_discount_amt,
        ws_ext_sales_price as ext_sales_price,
        ws_ext_wholesale_cost as ext_wholesale_cost,
        ws_ext_list_price as ext_list_price,
        ws_ext_tax as ext_tax,
        ws_coupon_amt as coupon_amt,
        ws_ext_ship_cost as ext_ship_cost,
        ws_net_paid as net_paid,
        ws_net_paid_inc_tax as net_paid_inc_tax,
        ws_net_paid_inc_ship as net_paid_inc_ship,
        ws_net_paid_inc_ship_tax as net_paid_inc_ship_tax,
        ws_net_profit as net_profit

    from src_web_sales
    where sold_date_id >= 2452554
)

select * from final
