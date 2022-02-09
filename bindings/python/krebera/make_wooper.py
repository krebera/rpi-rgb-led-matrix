#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from PIL import Image
from PIL import ImageDraw
import time
import random
import asyncio

class Wooper(SampleBase):
    def __init__(self):
        super(Wooper, self).__init__()

        im = Image.open('./temp/pokemon.png').convert('RGBA')
        w, h = im.size

        nw = 50
        nh = 50

        left = (w - nw)//2
        top = (h - nh)//2
        right = (w + nw)//2
        bottom = (h + nh)//2

        # Crop the center of the image
        im = im.crop((left, top, right, bottom))

        print(w)
        background = Image.new('RGBA', im.size, (0,0,0))
        self.pokemon = Image.alpha_composite(background, im).convert('RGB')

    def render(self):
        w, h = self.pokemon.size

        # image = Image.new("RGB", (w, h))  # Can be larger than matrix if wanted!!
        # draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
        # draw.rectangle((0, 0, 56, 10), fill=(0, 0, 0), outline=(0, 255, 0))

        # graphics.DrawText(self.matrix, self.font, 5, 15, self.textColor, self.verb)
        # graphics.DrawText(self.matrix, self.font, 5, 25, self.textColor, self.noun)

        # draw.rectangle((0, 0, int(progress * 0.56), 10), fill=(0, 255, 0), outline=(0, 255, 0))
        self.matrix.SetImage(self.pokemon, 0, 00)