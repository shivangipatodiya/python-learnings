import requests
from datetime import datetime

APP_ID = "99ae2d56"
API_KEY = "d0febb6f59650af95ae54257c68c4e43"

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/d0278df176e3855559dfe57ca57e700c/workoutTracking/workouts"
GENDER = "female"
AGE = 29
WEIGHT_KG = 65
HEIGHT_CM = 164

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

req_body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=ENDPOINT, json=req_body, headers=headers)
result = response.json()
# print(result)

date_today = datetime.today().strftime("%d%m%Y")
time_now = datetime.today().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)