#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from PIL import Image
from PIL import ImageDraw
import time
import random

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)

    def getVerb():
        return random.choice(list(open('./assets/verbs.txt')))

    def getNoun():
        return random.choice(list(open('./assets/nouns.txt')))

    def run(self):
        font = graphics.Font()
        font.LoadFont("../../../fonts/6x10.bdf")
        textColor = graphics.Color(0, 255, 0)

        image = Image.new("RGB", (58, 12))  # Can be larger than matrix if wanted!!
        draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
        draw.rectangle((0, 0, 56, 10), fill=(0, 0, 0), outline=(0, 255, 0))

        graphics.DrawText(self.matrix, font, 5, 15, textColor, self.getVerb())
        graphics.DrawText(self.matrix, font, 5, 25, textColor, self.getNoun())

        for n in range(0, 56 * 6):  # Start off top-left, move off bottom-right
            # self.matrix.Clear()

            if( n == 56 * 2):
                self.matrix.Clear()
                graphics.DrawText(self.matrix, font, 5, 15, textColor, self.getVerb())
                graphics.DrawText(self.matrix, font, 5, 25, textColor, self.getNoun())

            if( n == 56 * 4):
                self.matrix.Clear()
                graphics.DrawText(self.matrix, font, 5, 15, textColor, self.getVerb())
                graphics.DrawText(self.matrix, font, 5, 25, textColor, self.getNoun())

            draw.rectangle((0, 0, n // 6, 10), fill=(0, 255, 0), outline=(0, 255, 0))
            self.matrix.SetImage(image, 4, 40)
            time.sleep(0.02)

        # while True:
            # time.sleep(0.1)
            # offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
