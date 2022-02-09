#!/usr/bin/env python

# API Imports
from get_strava_tokens import loadStravaTokens
from apitest import get_strava_data
import asyncio

# Animation Imports
from samplebase import SampleBase
from rgbmatrix import graphics
from PIL import Image
from PIL import ImageDraw
import time
import random
import sys

# Custom Canvases
from animtest import LoadingBar
from make_wooper import Wooper

bar = LoadingBar()

async def updateBar():
    progress = 0
    while progress < 100:
        bar.render(progress)
        await asyncio.sleep(0.05)
        progress = progress + 1

# TODO: APPLICATION STATE MANAGER WITH ACTIVE WINDOW
# TODO: GENERAL WINDOW CLASS WITH AN UPDATE, SETUP, TEARDOWN
# TODO: CHEEKY MESSAGE FOR FLAVOR BEFORE STATE BREAKDOWN
# TODO: STAT BREAKDOWN

async def main():
    tasks = []
    tasks.append(asyncio.ensure_future(updateBar()))
    tasks.append(asyncio.ensure_future(get_strava_data()))

    json = await asyncio.gather(*tasks)
    print(json)
    bar.dismiss()

try:
    # Start loop
    print("Press CTRL-C to stop sample")
    # asyncio.run(main())
    wooper = Wooper()
    wooper.render()
    time.sleep(10)
except KeyboardInterrupt:
    print("Exiting\n")
    sys.exit(0)