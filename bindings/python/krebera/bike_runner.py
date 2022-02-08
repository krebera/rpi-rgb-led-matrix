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

def main():
    bar.run()
    asyncio.run(get_strava_data(closure = getJSON))

try:
    # Start loop
    print("Press CTRL-C to stop sample")
    main()
except KeyboardInterrupt:
    print("Exiting\n")
    sys.exit(0)