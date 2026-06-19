import sqlite3
import pandas as pd

conn = sqlite3.connect("weather.db")
df = pd.read_sql("select * from weather_data",conn)
print(df)
conn.close()