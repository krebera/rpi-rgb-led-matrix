from PIL import Image
from samplebase import SampleBase

def center_crop(im, nw, nh):
    w, h = im.size

    nw = 50
    nh = 50

    left = (w - nw)//2
    top = (h - nh)//2
    right = (w + nw)//2
    bottom = (h + nh)//2

    # Crop the center of the image
    return im.crop((left, top, right, bottom))

def alpha_comp(im):
    background = Image.new('RGBA', im.size, (0,0,0))
    return Image.alpha_composite(background, im).convert('RGB')

class ImagePreview(SampleBase):
    def __init__(self):
        super(ImagePreview, self).__init__()

    def render(self):
        self.matrix.SetImage(self.img, 0, 0)

    def set_im(self, image):
        self.img = image