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

        image = Image.new("RGB", (58, 12))  # Can be larger than matrix if wanted!!
        draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
        draw.rectangle((0, 0, 56, 10), fill=(0, 0, 0), outline=(0, 255, 0))

        graphics.DrawText(self.matrix, font, 10, 15, textColor, "Charging")
        graphics.DrawText(self.matrix, font, 18, 25, textColor, "Bike")

        for n in range(0, 56 * 4):  # Start off top-left, move off bottom-right
            # self.matrix.Clear()
            if( n == 56 * 2):
                self.matrix.Clear()
                graphics.DrawText(self.matrix, font, 10, 15, textColor, "Absorbing")
                graphics.DrawText(self.matrix, font, 18, 15, textColor, "Coolness")

            draw.rectangle((0, 0, n // 4, 10), fill=(0, 255, 0), outline=(0, 255, 0))
            self.matrix.SetImage(image, 0, 40)
            time.sleep(0.05)

        # while True:
            # time.sleep(0.1)
            # offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
