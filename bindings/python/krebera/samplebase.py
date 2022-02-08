import argparse
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
from rgbmatrix import RGBMatrix, RGBMatrixOptions


class SampleBase(object):
    def __init__(self):
        options = RGBMatrixOptions()
        options.rows = 64
        options.cols = 64
        options.pixel_mapper_config = "Rotate:270"

        self.matrix = RGBMatrix(options = options)

    def usleep(self, value):
        time.sleep(value / 1000000.0)

    def run(self):
        print("Running")
