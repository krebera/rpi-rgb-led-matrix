import requests
import json
import time

import aiohttp
import asyncio

'''
def firstTimeAuth(code):
  # Make Strava auth API call with your 
  # client_code, client_secret and code
  response = requests.post(
                      url = 'https://www.strava.com/oauth/token',
                      data = {
                              'client_id': int(list(open('./assets/client.txt'))[0].rstrip()),
                              'client_secret': list(open('./assets/client.txt'))[1].rstrip(),
                              'code': code,
                              'grant_type': 'authorization_code'
                              }
                  )
  #Save json response as a variable
  strava_tokens = response.json()
  # Save tokens to file
  with open('assets/strava_tokens.json', 'w') as outfile:
      json.dump(strava_tokens, outfile)
  print("Saved to file!")
'''

async def loadStravaTokens():
    # Get the tokens from file to connect to Strava
    with open('assets/strava_tokens.json') as json_file:
        strava_tokens = json.load(json_file)

    ## If access_token has expired then use the refresh_token to get the new access_token
    if strava_tokens['expires_at'] < time.time():
        #Make Strava auth API call with current refresh token
        async with aiohttp.ClientSession(headers = {"Authorization": "Bearer " + strava_tokens['access_token']}) as session:

            async with session.post('https://www.strava.com/oauth/token', json = {
                'client_id': int(list(open('./assets/client.txt'))[0].rstrip()),
                'client_secret': list(open('./assets/client.txt'))[1].rstrip(),
                'grant_type': 'refresh_token',
                'refresh_token': strava_tokens['refresh_token']
            }) as auth_response:

                #Save response as json in new variable
                new_strava_tokens = auth_response.json()
                # Save new tokens to file
                with open('assets/strava_tokens.json', 'w') as outfile:
                    json.dump(new_strava_tokens, outfile)

            #Use new Strava tokens from now
            strava_tokens = new_strava_tokens
            
        return strava_tokens