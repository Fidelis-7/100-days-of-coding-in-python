import requests
from datetime import datetime


USERNAME = "fidelis"
TOKEN = "fhk984fjohjuijk"
GRAPH_ID = "graph1"

pixel_api_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}


# response = requests.post(url=pixel_api_endpoint, json=user_params)           #create a user
# print(response.text)

    # posting a graph
graph_endpoint = f"{pixel_api_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":GRAPH_ID,
    "name":"Cycling graph",
    "unit":"km",
    "type":"float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# posting a pixel
pixel_endpoint = f"{pixel_api_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"), 
    "quantity": "9.56",
}

headers = { 
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)


update_endpoint = f"{pixel_api_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{'%Y%m%d'}"

new_pixel_data = {
    "quantity": "4.5",

}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

delete_endpoint = f"{pixel_api_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{'%Y%m%d'}"

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)