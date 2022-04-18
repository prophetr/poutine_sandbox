with customers as (
    select * from {{ ref('stg_production__customers') }}
),

orders as (
    select * from {{ ref('stg_transactions__orders') }}
),

events as (
    select * from {{ ref('stg_production__fulfillments') }}   
),

customers_orders as (
    select
        customer_id,
        min(order_created_at) as first_order_created_at,
        max(order_created_at) as latest_order_created_at,
        sum(order_total) as sum_order_revenue,
        count(order_id) as count_orders
      
    from orders
    group by 1
),

customers_fulfillments as (
    select
       customer_id,
       count(distinct event_id) as count_unique_events
    from events
    group by 1
),

final as (
    select
     --primary key
       customers.customer_id,

     --date & timestamp
       customers_orders.first_order_created_at,
       customers_orders.latest_order_created_at,

     --dimensions
       customers.customer_name,
       customers.gender,

     --metrics
       coalesce(customers_orders.count_orders, 0) as count_orders,
       coalesce(customers_fulfillments.count_unique_events,0) as count_unique_events,
       coalesce(customers_orders.sum_order_revenue,0) as sum_order_revenue
  
    from customers
    left join customers_orders 
     on customers.customer_id = customers_orders.customer_id
    left join customers_fulfillments 
     on customers.customer_id = customers_fulfillments.customer_id
)

select * from final
