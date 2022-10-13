-- depends_on: {{ ref('fct_orders') }}
select * from 
{{ metrics.calculate(
    metric('revenue')
    ,grain='month'
    ,dimensions=['shop_id']
) }}
