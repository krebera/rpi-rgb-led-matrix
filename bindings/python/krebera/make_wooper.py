#!/usr/bin/env python

from samplebase import SampleBase
from PIL import Image
from PIL import ImageDraw

class Wooper(SampleBase):
    def __init__(self):
        super(Wooper, self).__init__()

        # im = Image.open('./temp/pokemon.png').convert('RGBA')
        # w, h = im.size

        nw = 50
        nh = 50

        # left = (w - nw)//2
        # top = (h - nh)//2
        # right = (w + nw)//2
        # bottom = (h + nh)//2

        # Crop the center of the image
        # im = im.crop((left, top, right, bottom))

        # background = Image.new('RGBA', im.size, (0,0,0))
        # self.pokemon = Image.alpha_composite(background, im).convert('RGB')

    def render(self):
        # w, h = self.pokemon.size

        image = Image.new("RGB", (64, 64))  # Can be larger than matrix if wanted!!
        draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
        draw.rectangle((0, 0, 56, 10), fill=(0, 0, 0), outline=(0, 255, 0))
        self.matrix.SetImage(image, 0, 0)
        # self.matrix.SetImage(self.pokemon, 0, 0)