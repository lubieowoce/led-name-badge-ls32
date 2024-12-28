from PIL import Image, ImageOps
import os
import sys
from functools import reduce

_, file, out_file = sys.argv
should_invert = bool(os.environ.get('INVERT', ''))
# file = sys.argv[1]
# out_file = sys.argv[2]
im = Image.open(file)

WIDTH = 44
ANIM_WIDTH = 48  # not
HEIGHT = 11

iw, ih = im.size
print(f"{iw}x{ih}, {im.n_frames} frames")


def strip_alpha(im):
    r, g, b, _a = im.split()
    return Image.merge('RGB', (r, g, b))


def extend(im: Image.Image, size: tuple[int, int]):
    res = Image.new("RGBA", size)
    res.paste(im, (0, 0))
    return res


def merge_horizontal(im1: Image.Image, im2: Image.Image) -> Image.Image:
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im


res = None
for frame_index in range(im.n_frames):
    im.seek(frame_index)
    frame = extend(im, (ANIM_WIDTH, HEIGHT))
    if should_invert:
        frame = ImageOps.invert(strip_alpha(frame))
    if res == None:
        res = frame
    else:
        res = merge_horizontal(res, frame)

res.save(out_file)
