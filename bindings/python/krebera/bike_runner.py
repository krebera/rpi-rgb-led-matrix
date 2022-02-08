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


def getJSON(newData):
    global data
    global bar
    
    data = newData
    bar.dismiss()

    print(newData)

data = None
bar = LoadingBar()

async def updateBar():
    progress = 0
    while progress < 100:
        bar.render(progress)
        await asyncio.sleep(0.05)
        progress = progress + 1

async def main():
    task1 = asyncio.create_task(updateBar())
    task2 = asyncio.create_task(get_strava_data(closure = getJSON))

    await task1
    # await task2

try:
    # Start loop
    print("Press CTRL-C to stop sample")
    asyncio.run(main())
except KeyboardInterrupt:
    print("Exiting\n")
    sys.exit(0)