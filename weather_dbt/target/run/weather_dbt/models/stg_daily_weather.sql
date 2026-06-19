

  create or replace view `magnetic-port-429910-q4`.`weather_data`.`stg_daily_weather`
  OPTIONS()
  as with cte as(
select date,temp_min,temp_max,round(temp_avg,2) as average_temp, 
row_number() over(partition by date order by date) as row_no
from `magnetic-port-429910-q4`.`weather_data`.`daily_weather`
)

select c.* except (row_no)
from cte c
where row_no = 1;

