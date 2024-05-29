import requests
import config
from datetime import datetime

#endpoint for user
pixela_endpoint = "https://pixe.la/v1/users"
#user params for account creation
user_params = {
    "token": config.TOKEN,
    "username": config.USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#Creating user account
#response = requests.post(url=pixela_endpoint,json=user_params)

#Endpoint for graphs
graph_endpoint = f"{pixela_endpoint}/{config.USERNAME}/graphs"

"""
FROM DOCS
id	string	[required] It is an ID for identifying the pixelation graph.
Validation rule: ^[a-z][a-z0-9-]{1,16}
name	string	[required] It is the name of the pixelation graph.
unit	string	[required] It is a unit of the quantity recorded in the pixelation graph. Ex. commit, kilogram, calory.
type	string	[required] It is the type of quantity to be handled in the graph. Only int or float are supported.
color	string	[required] Defines the display color of the pixel in the pixelation graph.
shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black) are supported as color kind.
"""

#graph params for graph creation
graph_config = {
    "id": config.HABIT_GRAPHID,
    "name": "Reading Graph",
    "unit": "chapters",
    "type": "int",
    "color": "momiji"
}

#headers
headers = {
    "X-USER-TOKEN": config.TOKEN
}

#Creating graph
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

#endpoint for accessing graph by ID
graph_pixel_endpoint = f"{graph_endpoint}/{config.HABIT_GRAPHID}"
#using datetime module to get todays date automatically
today = datetime.now()

#pixel params for adding data to graph (represents each time we complete a habit)
graph_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8",
    "optionalData": "{\"book\":\"Psalms\"}"
}

#posting data to graph
response = requests.post(url=graph_pixel_endpoint, json=graph_pixel_config, headers=headers)
#print(response.json())

