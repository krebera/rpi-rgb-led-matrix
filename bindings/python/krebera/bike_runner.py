#!/usr/bin/env python

# API Imports
from get_strava_tokens import loadStravaTokens
from apitest import get_strava_data
import asyncio
import sys

# Custom Canvases
from animtest import LoadingBar
from make_wooper import Wooper

# bar = LoadingBar()

# async def updateBar():
#     progress = 0
#     while progress < 100:
#         bar.render(progress)
#         await asyncio.sleep(0.05)
#         progress = progress + 1

# TODO: APPLICATION STATE MANAGER WITH ACTIVE WINDOW
# TODO: GENERAL WINDOW CLASS WITH AN UPDATE, SETUP, TEARDOWN
# TODO: CHEEKY MESSAGE FOR FLAVOR BEFORE STATE BREAKDOWN
# TODO: STAT BREAKDOWN

#TODO: You need to create exactly one matrix and then assign and deassign views to it
# You can't own multiple

# async def main():
#     tasks = []
#     tasks.append(asyncio.ensure_future(updateBar()))
#     tasks.append(asyncio.ensure_future(get_strava_data()))

#     json = await asyncio.gather(*tasks)
#     print(json)
#     bar.dismiss()

try:
    # Start loop
    print("Press CTRL-C to stop sample")
    # asyncio.run(main())
    woop = Wooper()
    woop.render()
except KeyboardInterrupt:
    print("Exiting\n")
    sys.exit(0)