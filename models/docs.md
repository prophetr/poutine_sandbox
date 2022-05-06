{% docs fct_orders__orders_sk %}
Unique identifier for order_items table.
{% enddocs %}

{% docs fct_orders__order_item_unique_sk %}
Unique identifier for orders.
{% enddocs %}

{% docs fct_orders__order_id %}
Unique order identifier.
{% enddocs %}

{% docs fct_orders__product_id %}
Unique product identifier.
{% enddocs %}

{% docs fct_orders__customer_id %}
Unique customer identifier.
{% enddocs %}

{% docs fct_orders__shop_id %}
Unique identifier for the shop that the order was placed.
{% enddocs %}

{% docs fct_orders__quantity %}
The number of items ordered by the customer.
{% enddocs %}

{% docs fct_orders__unit_price %}
Price of 1 unit of the product
{% enddocs %}

{% docs fct_orders__price %}
Combined price for all units in order item (i.e. unit_price multiplied by quantity)
{% enddocs %}

{% docs fct_orders__order_created_at %}
When the order was created at.
{% enddocs %}

{% docs fct_orders__order_tax %}
The tax on the order
{% enddocs %}

{% docs fct_orders__order_total %}
The order's total amount
{% enddocs %}