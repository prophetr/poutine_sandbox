{% macro increase_wh_size() %}
    
    use role admin;
    alter warehouse set warehouse_size = 'LARGE';
    use role dbt_cloud_role;

{% endmacro %}
