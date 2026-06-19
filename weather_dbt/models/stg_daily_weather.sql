with cte as(
select date,temp_min,temp_max,round(temp_avg,2) as average_temp, 
row_number() over(partition by date order by date) as row_no
from {{ source("weather_data","daily_weather")}}
)

select c.* except (row_no)
from cte c
where row_no = 1

