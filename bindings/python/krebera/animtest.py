#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from PIL import Image
from PIL import ImageDraw
import time
import random
import asyncio

class LoadingBar(SampleBase):
    def __init__(self):
        super(LoadingBar, self).__init__()
        self.font = graphics.Font()
        self.font.LoadFont("../../../fonts/6x10.bdf")
        self.textColor = graphics.Color(0, 255, 0)

        self.verb = random.choice(list(open('./assets/verbs.txt'))).rstrip()
        self.noun = random.choice(list(open('./assets/nouns.txt'))).rstrip()

        self.used_verbs = [self.verb]
        self.used_nouns = [self.noun]

    def getVerb(self):
        this_verb = self.verb
        while(this_verb in self.used_verbs):
            this_verb = random.choice(list(open('./assets/verbs.txt'))).rstrip()
        self.used_verbs.append(self.verb)
        return this_verb

    def getNoun(self):
        this_noun = self.noun
        while(this_noun in self.used_nouns):
            this_noun = random.choice(list(open('./assets/nouns.txt'))).rstrip()
        self.used_nouns.append(self.noun)
        return this_noun

    def render(self, progress):
        if(progress == 33 or progress == 66):
            self.verb = self.getVerb()
            self.noun = self.getNoun()
            self.matrix.Clear()

        image = Image.new("RGB", (58, 12))  # Can be larger than matrix if wanted!!
        draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
        draw.rectangle((0, 0, 56, 10), fill=(0, 0, 0), outline=(0, 255, 0))

        graphics.DrawText(self.matrix, self.font, 5, 15, self.textColor, self.verb)
        graphics.DrawText(self.matrix, self.font, 5, 25, self.textColor, self.noun)

        draw.rectangle((0, 0, int(progress * 0.56), 10), fill=(0, 255, 0), outline=(0, 255, 0))
        self.matrix.SetImage(image, 4, 40)
    
    def dismiss(self):
        self.used_nouns = []
        self.used_verbs = []
        self.matrix.Clear()