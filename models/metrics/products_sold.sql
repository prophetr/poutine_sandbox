-- depends_on: {{ ref('fct_orders') }}
select * from 
{{ metrics.calculate(
    metric('products_sold')
    ,grain='week'
    ,dimensions=['shop_id', 'product_id']
) }}
order by 1 desc
