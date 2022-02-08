import requests
import json
import time
from get_strava_tokens import loadStravaTokens

strava_tokens = loadStravaTokens()

response = requests.get(
    "https://www.strava.com/api/v3/athlete/activities",
    params={},
    headers={"Authorization": "Bearer " + strava_tokens['access_token']}
    )

with open('sample_data.json', 'w') as outfile:
    json.dump(response.json(), outfile)

# https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86