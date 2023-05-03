import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 5.1
AGE = 20

APP_ID = "a824f715"
API_KEY = "e448d4180759e718cbd58d59be69abc2"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/4bbf6252f12ebc8107aab6bbea8b8b11/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #No Auth
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


    #Basic Auth
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        auth=("fidelis", "Felix2003!")
    )

    #Bearer Token
    bearer_headers = {
    "Authorization": f"Bearer {'97656'}"
    }
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        headers=bearer_headers
    )

    print(sheet_response.text)
