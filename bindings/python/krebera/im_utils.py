from PIL import Image
from samplebase import SampleBase

def center_crop(im, nw, nh):
    w, h = im.size

    left = (w - nw)//2
    top = (h - nh)//2
    right = (w + nw)//2
    bottom = (h + nh)//2

    # Crop the center of the image
    img = im.crop((left, top, right, bottom))
    return img.resize((nw, nh))

def scale_image(im, nw, nh):
    im.thumbnail((nw, nh), Image.NEAREST)
    return im

def autocrop(im):
    img_box = im.getbbox()
    cropped = im.crop(img_box)
    return cropped

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