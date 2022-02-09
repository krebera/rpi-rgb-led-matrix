#!/usr/bin/env python
from samplebase import SampleBase
from PIL import Image
from PIL import ImageDraw

class StupidTest(SampleBase):
    def __init__(self):
        super(StupidTest, self).__init__()

    def render(self):
        image = Image.new("RGB", (64, 64))  # Can be larger than matrix if wanted!!
        draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
        draw.rectangle((0, 0, 56, 10), fill=(0, 0, 0), outline=(0, 255, 0))
        self.matrix.SetImage(image, 0, 0)