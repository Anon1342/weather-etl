

  create or replace view `magnetic-port-429910-q4`.`weather_data`.`mart_daily_weather`
  OPTIONS()
  as select *
from `magnetic-port-429910-q4`.`weather_data`.`stg_daily_weather`;

