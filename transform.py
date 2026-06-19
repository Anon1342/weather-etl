from extract import extract_weather
import pandas as pd
def transform_weather(data):
    daily = data['daily']
    df = pd.DataFrame({
        "date":daily["time"],
        "temp_max":daily["temperature_2m_max"],
        "temp_min":daily['temperature_2m_min'],
    })
    df["date"] = pd.to_datetime(df["date"])
    df["temp_avg"] = (df["temp_max"] + df["temp_min"])/2
    return(df)

if __name__ == "__main__":
    data = extract_weather()
    res = transform_weather(data)
    print(res.head())
