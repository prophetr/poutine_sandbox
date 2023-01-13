# Model-Level Descriptions

{% docs stg_snowflake_sample__catalog_sales %}
One row per item sold from a catalog.
{% enddocs %}

{% docs stg_snowflake_sample__store_sales %}
One row per item sold from a store.
{% enddocs %}

{% docs stg_snowflake_sample__web_sales %}
One row per item sold from a website.
{% enddocs %}

{% docs stg_snowflake_sample__date_dim %}
One row per specific date.
{% enddocs %}

{% docs stg_snowflake_sample__customers %}
One row per specific customer.
{% enddocs %}

# Column-Level Descriptions

## Shared Descriptions

{% docs snowflake_sample__order_number %}
Order number linked to sales.
{% enddocs %}

## Catalog Sales Descriptions

{% docs snowflake_sample_catalog_sales__catalog_sales_id %}
Primary key of the table, surrogate key made of the fields `order_number` and `item_id`.
{% enddocs %}

## Store Sales Descriptions

{% docs snowflake_sample_store_sales__store_sales_id %}
Primary key of the table, surrogate key made of the fields `ticket_number` and `item_id`.
{% enddocs %}

## Catalog Sales Descriptions

{% docs snowflake_sample_web_sales__web_sales_id %}
Primary key of the table, surrogate key made of the fields `order_number` and `item_id`.
{% enddocs %}

## Date Dim Descriptions

{% docs snowflake_sample_date_dim__date_sk %}
Primary key of the table, as a number format.
{% enddocs %}

{% docs snowflake_sample_date_dim__date_id %}
Primary key of the table, as a varchar format.
{% enddocs %}

{% docs snowflake_sample_date_dim__standard_date %}
The date dimension in format 'YYYY-MM-DD'
{% enddocs %}

## Customers Descriptions

{% docs snowflake_sample_customers__customer_sk %}
Primary key of the table, as a number format.
{% enddocs %}

{% docs snowflake_sample_customers__customer_id %}
Primary key of the table, as a varchar format.
{% enddocs %}

{% docs snowflake_sample_customers__first_name %}
The date first name of the customer
{% enddocs %}
