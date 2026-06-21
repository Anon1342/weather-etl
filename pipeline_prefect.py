from prefect import task, flow
from extract import extract_weather
from transform import transform_weather
from load_bq import load_bq_weather
import subprocess

extract_task = task(extract_weather)
transform_task = task(transform_weather)
load_bq_task = task(load_bq_weather)

@task
def dbt_run_task():
    subprocess.run(["rm", "-rf", "weather_dbt/target", "weather_dbt/dbt_packages"], cwd="/app")
    subprocess.run(["dbt","run","--profiles-dir","/app"],cwd = "/app/weather_dbt")

@flow
def prefect_pipeline():
    extracted_data = extract_task()
    transformed_data = transform_task(extracted_data)
    load_bq_task(transformed_data)
    dbt_run_task()




if __name__ == "__main__":
    prefect_pipeline()
    