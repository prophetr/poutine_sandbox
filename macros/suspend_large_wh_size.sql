{% macro suspend_large_wh_size() %}
    
    use role admin;
    alter warehouse set warehouse_size = 'X-SMALL';
    use role dbt_cloud_role;

    alter warehouse suspend;

{% endmacro %}
