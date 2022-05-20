{% macro grant_select(role) %}
      grant select on {{ this }} to role {{ role }}
{% endmacro %}
