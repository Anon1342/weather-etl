from transform import transform_weather
from extract import extract_weather
import sqlite3

def load_weather(df):
    conn = sqlite3.connect("weather.db")
    df.to_sql("weather_data",conn,if_exists="append")
    conn.close()


if __name__== "__main__":
        extract_data = extract_weather()
        transformed_data = transform_weather(extract_data)
        loaded_data = load_weather(transformed_data)
        print("Data Loaded successfully")