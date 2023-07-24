import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("ENDPOINT")
sheet_endpoint = os.getenv("SHEETY_ENDPOINT")
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

sheety_headers = {
    "Authorization": os.getenv("SHEETY_BEARER_TOKEN"),
}

response = requests.post(url=ENDPOINT, json=req_body, headers=headers)
result = response.json()
print(result)

date_today = datetime.today().strftime("%d/%m/%Y")
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

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheety_headers)

    # print(sheet_response.text)