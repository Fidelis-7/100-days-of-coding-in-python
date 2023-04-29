import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "517ed19953a7293b0ecac2f451e3ba1a"
LONGITUDE = -0.225710
LATITUDE = 5.564540
parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,minutely,daily" 
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data["weather"][0]["id"])

