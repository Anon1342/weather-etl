from prefect import task, flow
from extract import extract_weather
from transform import transform_weather
from load_bq import load_bq_weather

extract_task = task(extract_weather)
transform_task = task(transform_weather)
load_bq_task = task(load_bq_weather)

@flow
def prefect_pipeline():
    extracted_data = extract_task()
    transformed_data = transform_task(extracted_data)
    load_bq_task(transformed_data)
    return("Data Loaded Successfully")


if __name__ == "__main__":
    prefect_pipeline()
    