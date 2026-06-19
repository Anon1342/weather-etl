from extract import extract_weather
from transform import transform_weather
from load_bq import load_bq_weather

def pipeline_weather():
    extracted_data = extract_weather()
    transformed_data = transform_weather(extracted_data)
    load_bq_weather(transformed_data)
    return("The pipeline ran")

if __name__ == "__main__":
    message = pipeline_weather()
    print(message)
