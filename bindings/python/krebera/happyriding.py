#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from PIL import Image
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/6x10.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = 0
        my_text = "Happy Riding"
        graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)

        image = Image.open("./img/bike.ppm").convert('RGB')
        img_width, img_height = image.size
        offscreen_canvas.SetImage(image, 0)

        while True:
            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
