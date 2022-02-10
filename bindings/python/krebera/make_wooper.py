#!/usr/bin/env python

from samplebase import SampleBase
from PIL import Image
from PIL import ImageDraw

class Wooper(SampleBase):
    def __init__(self):
        super(Wooper, self).__init__()

        # im = Image.open('./temp/pokemon.png').convert('RGBA')
        # w, h = im.size

        # nw = 50
        # nh = 50

        # left = (w - nw)//2
        # top = (h - nh)//2
        # right = (w + nw)//2
        # bottom = (h + nh)//2

        # # Crop the center of the image
        # im = im.crop((left, top, right, bottom))

        # background = Image.new('RGBA', im.size, (0,0,0))
        # self.pokemon = Image.alpha_composite(background, im).convert('RGB')

    def render(self):
        self.matrix.SetImage(self.pokemon, 0, 0)

    def set_im(self, image):
        self.pokemon = image