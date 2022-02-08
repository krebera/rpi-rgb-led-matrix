import requests
import json
import time
from get_strava_tokens import loadStravaTokens

strava_tokens = loadStravaTokens()

# response = requests.get(
#     "https://www.strava.com/api/v3/athlete/activities",
#     params={},
#     headers={"Authorization": "Bearer " + strava_tokens['access_token']}
#     )

# with open('sample_data.json', 'w') as outfile:
#     json.dump(response.json(), outfile)

# https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86

import aiohttp
import asyncio

async def get_strava_data(closure, before = None, after = None, page = 1, per_page = 30):

    before_str = str(before) if before else ""
    after_str = str(after) if after else ""
    page_str = str(page)
    per_page_str = str(per_page)
    
    async with aiohttp.ClientSession(headers = {"Authorization": "Bearer " + strava_tokens['access_token']}) as session:
        strava_url = f'https://www.strava.com/api/v3/athlete/activities?before={before_str}&after={after_str}&page={page_str}&per_page={per_page_str}'

        async with session.get(strava_url) as resp:
            strava = await resp.json()
            closure(strava)

#asyncio.run(get_strava_data())