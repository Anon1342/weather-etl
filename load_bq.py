from dotenv import load_dotenv 
load_dotenv()
from google.cloud import bigquery
from extract import extract_weather
from transform import transform_weather

def load_bq_weather(df):
    client = bigquery.Client()
    table_id = "magnetic-port-429910-q4.weather_data.daily_weather"
    job = client.load_table_from_dataframe(df,table_id)
    job.result()
    return("Job done succesfully")

if __name__ == "__main__":
    extracted_data = extract_weather()
    transformed_data = transform_weather(extracted_data)
    loaded_data = load_bq_weather(transformed_data)
    print(loaded_data)
