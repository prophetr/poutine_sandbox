with src_catalog_sales as (
    select * from {{ source('snowflake_sample_data', 'catalog_sales') }}
),

final as (
    select
        -- primary key
        {{ dbt_utils.surrogate_key(['cs_order_number', 'cs_item_sk']) }} as catalog_sales_id,

        -- foreign keys
        cs_sold_date_sk as sold_date_id,
        cs_sold_time_sk as sold_time_id,
        cs_ship_date_sk as ship_date_id,
        cs_bill_customer_sk as bill_customer_id,
        cs_bill_cdemo_sk as bill_cdemo_id,
        cs_bill_hdemo_sk as bill_hdemo_id,
        cs_bill_addr_sk as bill_addr_id,
        cs_ship_customer_sk as ship_customer_id,
        cs_ship_cdemo_sk as ship_cdemo_id,
        cs_ship_hdemo_sk as ship_hdemo_id,
        cs_ship_addr_sk as ship_addr_id,
        cs_call_center_sk as call_center_id,
        cs_catalog_page_sk as catalog_page_id,
        cs_ship_mode_sk as ship_mode_id,
        cs_warehouse_sk as warehouse_id,
        cs_item_sk as item_id,
        cs_promo_sk as promo_id,
        cs_order_number as order_number,

        -- details
        cs_quantity as quantity,
        cs_wholesale_cost as wholesale_cost,
        cs_list_price as list_price,
        cs_sales_price as sales_price,
        cs_ext_discount_amt as ext_discount_amt,
        cs_ext_sales_price as ext_sales_price,
        cs_ext_wholesale_cost as ext_wholesale_cost,
        cs_ext_list_price as ext_list_price,
        cs_ext_tax as ext_tax,
        cs_coupon_amt as coupon_amt,
        cs_ext_ship_cost as ext_ship_cost,
        cs_net_paid as net_paid,
        cs_net_paid_inc_tax as net_paid_inc_tax,
        cs_net_paid_inc_ship as net_paid_inc_ship,
        cs_net_paid_inc_ship_tax as net_paid_inc_ship_tax,
        cs_net_profit as net_profit

    from src_catalog_sales
    where sold_date_id >= 2452634
)

select * from final
