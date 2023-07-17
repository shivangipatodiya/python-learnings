import requests

API_KEY = "my_api_key"
LATITUDE = 43.589046
LONGITUDE = -79.644119
URL = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(URL, params=params)
response.raise_for_status()
weather_info = response.json()
weather_info_sliced = weather_info["hourly"][:12]

will_rain = False

for hour in weather_info_sliced:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring your umbrella.")
