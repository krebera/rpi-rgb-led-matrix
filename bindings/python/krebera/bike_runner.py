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

# Custom Canvases
from animtest import LoadingBar

data = None
bar = LoadingBar()

def getJSON(newData):
    global data

    data = newData
    bar.dismiss()

    print(data[0])

asyncio.run(get_strava_data(closure = getJSON))