{% macro round_value(column,decimal_places=1) %}
    ROUND({{column}},{{decimal_places}})
{%endmacro%}