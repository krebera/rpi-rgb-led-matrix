import requests
import json
import time
from get_strava_tokens import loadStravaTokens

import aiohttp
import asyncio

async def get_strava_data(before = None, after = None, page = 1, per_page = 30):

    strava_tokens_task = asyncio.ensure_future(loadStravaTokens())
    strava_tokens = await(strava_tokens_task)

    async with aiohttp.ClientSession(headers = {"Authorization": "Bearer " + strava_tokens['access_token']}) as session:
        strava_url = f'https://www.strava.com/api/v3/athlete/activities?page={str(page)}&per_page={str(per_page)}{("&before=" + str(before)) if before else ""}{("&after=" + str(after)) if after else ""}'

        async with session.get(strava_url) as resp:
            strava = await resp.json()
            print("Got strava data")
            return strava