with sales_unioned as (
    select * from {{ ref('int_snowflake_sample_sales_unioned') }}
),

date_dim as (
    select * from {{ ref('stg_snowflake_sample__date_dim') }}
),

customers as (
    select * from {{ ref('stg_snowflake_sample__customers') }}
),

final as (
    select
        -- primary key
        sales_unioned.sales_id,

        -- foreign keys
        sales_unioned.sales_order_number,
        sales_unioned.catalog_sales_id,
        sales_unioned.store_sales_id,
        sales_unioned.web_sales_id,
        sales_unioned.sold_date_id,
        sales_unioned.sold_time_id,
        sales_unioned.ship_date_id,
        sales_unioned.customer_id,
        sales_unioned.cdemo_id,
        sales_unioned.hdemo_id,
        sales_unioned.addr_id,
        sales_unioned.bill_customer_id,
        sales_unioned.bill_cdemo_id,
        sales_unioned.bill_hdemo_id,
        sales_unioned.bill_addr_id,
        sales_unioned.ship_customer_id,
        sales_unioned.ship_cdemo_id,
        sales_unioned.ship_hdemo_id,
        sales_unioned.ship_addr_id,
        sales_unioned.call_center_id,
        sales_unioned.catalog_page_id,
        sales_unioned.store_id,
        sales_unioned.web_page_id,
        sales_unioned.web_site_id,
        sales_unioned.ship_mode_id,
        sales_unioned.warehouse_id,
        sales_unioned.item_id,
        sales_unioned.promo_id,
        sales_unioned.order_number,

        -- details
        --customers.first_name,
        sales_unioned.quantity,
        sales_unioned.wholesale_cost,
        sales_unioned.list_price,
        sales_unioned.sales_price,
        sales_unioned.ext_discount_amt,
        sales_unioned.ext_sales_price,
        sales_unioned.ext_wholesale_cost,
        sales_unioned.ext_list_price,
        sales_unioned.ext_tax,
        sales_unioned.coupon_amt,
        sales_unioned.ext_ship_cost,
        sales_unioned.net_paid,
        sales_unioned.net_paid_inc_tax,
        sales_unioned.net_paid_inc_ship,
        sales_unioned.net_paid_inc_ship_tax,
        sales_unioned.net_profit,

        -- dates
        --date_dim.standard_date,

        -- calculations
        case
            when coalesce(sales_unioned.sales_price, 0) = 0
                then 1
            else  round(sales_unioned.net_profit / sales_unioned.sales_price * 100, 0) 
        end as sales_profit_pctg--,
        --row_number() 
        --over (
         --   partition by coalesce(sales_unioned.customer_id, sales_unioned.bill_customer_id)
         --   order by sales_unioned.sold_date_id
        --) as customer_sales_sequence

    from sales_unioned
    --left join customers on 
      --  sales_unioned.customer_id = customers.customer_sk
    --left join date_dim on 
      --  sales_unioned.sold_date_id = date_dim.date_sk

    order by sales_unioned.sold_date_id

-- Try using a larger dataset, 
-- even a select * on one of the larger tables should create this behaviour. 
-- Throw in a bunch of order bys to add some more work. 
)

select * from final
