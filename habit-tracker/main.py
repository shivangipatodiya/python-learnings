import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "ef45ytgbtyu67cv"

pixela_endpoint = "https://pixe.la/v1/users"
user_req_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
## POST
# response = requests.post(url=pixela_endpoint, json=user_req_body)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"
graph_req_body = {
    "id": graph_id,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_req_body, headers=headers)
# print(graph_response.text)

today = datetime.today()
pixel_endpoint = f"{graph_endpoint}/{graph_id}"

pixel_req_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15.6"
}

# pixel_response = requests.post(url=pixel_endpoint, json=pixel_req_body, headers=headers)
# print(pixel_response.text)

date_to_be_updated = "20230719"
update_pixel_endpoint = f"{pixel_endpoint}/{date_to_be_updated}"

update_pixel_req_body = {
    "quantity": "10.6"
}
## UPDATE
# update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_pixel_req_body, headers=headers)
# print(update_pixel_response.text)

## DELETE
# delete_pixel_response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(delete_pixel_response.text)

