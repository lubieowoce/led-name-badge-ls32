from PIL import Image
import sys
from functools import reduce

_, direction, file, out_file = sys.argv
# file = sys.argv[1]
# out_file = sys.argv[2]
im = Image.open(file)

WIDTH = 44
ANIM_WIDTH = 48  # not
HEIGHT = 11

iw, ih = im.size
# print(iw, ih)


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


if direction == 'down':
    if ih <= HEIGHT:
        raise Exception(f'Image too short ({ih}px), nothing to scroll')
    res = reduce(
        merge_horizontal,
        (
            extend(im.crop((0, y, WIDTH, y+HEIGHT)), (ANIM_WIDTH, HEIGHT))
            for y in range(0, ih - HEIGHT + 1)
        )
    )
elif direction == 'right':
    if iw <= WIDTH:
        raise Exception(f'Image too narrow ({iw}px), nothing to scroll')
    res = reduce(
        merge_horizontal,
        (
            extend(im.crop((x, 0, x + WIDTH, HEIGHT)), (ANIM_WIDTH, HEIGHT))
            for x in range(0, iw - WIDTH + 1)
        )
    )
else:
    raise Exception(f'Invalid direction: {direction}')

num_bytes = (res.size[0] * res.size[1]) // 8
print(f"{num_bytes} bytes", file=sys.stderr)
res.save(out_file)
