#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from PIL import Image
from PIL import ImageDraw
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)

    def run(self):
        font = graphics.Font()
        font.LoadFont("../../../fonts/6x10.bdf")
        textColor = graphics.Color(0, 255, 0)

        image = Image.new("RGB", (32, 32))  # Can be larger than matrix if wanted!!
        draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
        draw.rectangle((2, 2, 30, 20), fill=(0, 0, 0), outline=(0, 255, 0))

        for n in range(-32, 33):  # Start off top-left, move off bottom-right
            self.matrix.Clear()
            self.matrix.SetImage(image, 0, 0)
            graphics.DrawText(self.matrix, font, 15, 45, textColor, "Charging")
            graphics.DrawText(self.matrix, font, 11, 55, textColor, "Bike")
            time.sleep(0.02)

        # while True:
            # time.sleep(0.1)
            # offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
