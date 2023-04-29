import requests
from datetime import datetime

MY_LATITUDE = 5.603717
MY_LONGITUDE = -0.186964

parameters =  {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted":0
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sun = (sunrise, sunset)
print(sun)

time_now = datetime.now()
print(time_now)