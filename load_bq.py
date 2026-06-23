from dotenv import load_dotenv 
import os
from google.cloud import bigquery
from extract import extract_weather
from transform import transform_weather
load_dotenv()
def load_bq_weather(df):
    client = bigquery.Client()
    table_id = os.getenv("TABLE_ID")
    job = client.load_table_from_dataframe(df,table_id)
    job.result()
    return("Job done succesfully")

if __name__ == "__main__":
    extracted_data = extract_weather()
    transformed_data = transform_weather(extracted_data)
    loaded_data = load_bq_weather(transformed_data)
    print(loaded_data)
