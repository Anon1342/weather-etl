import requests
def extract_weather():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=27.7&longitude=85.3&daily=temperature_2m_max,temperature_2m_min&timezone=Asia/Kathmandu'
    response = requests.get(url)
    data = response.json()
    return(data)

if __name__ == "__main__":
    data = extract_weather()
    print(data)

