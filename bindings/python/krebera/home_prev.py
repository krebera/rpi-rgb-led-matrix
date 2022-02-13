from os import listdir
from os.path import isfile, join
import aiohttp
import asyncio
import aiofiles
from im_utils import center_crop, alpha_comp, scale_image, autocrop
from PIL import Image, ImageDraw
import time

from im_utils import ImagePreview


if __name__ == "__main__":
    prev = ImagePreview()
    prev.set_im(Image.open("./assets/home.jpg"))
    prev.render()
    time.sleep(30)
    # canvas.show()