-- Use the `ref` function to select from other models

select *
from `magnetic-port-429910-q4`.`weather_data`.`my_first_dbt_model`
where id = 1