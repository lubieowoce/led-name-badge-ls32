from PIL import Image, ImageDraw
import os
import sys
from functools import reduce

_, direction, file, out_file = sys.argv
# file = sys.argv[1]
# out_file = sys.argv[2]
im = Image.open(file)

offset_str = os.environ.get('OFFSET', None)
offset = int(offset_str) if offset_str is not None else 0

background = os.environ.get('BACKGROUND', '')

loop_repeat_str = os.environ.get('LOOP_REPEAT', 0)
loop_repeat = int(loop_repeat_str)

WIDTH = 44
ANIM_WIDTH = 48  # not
HEIGHT = 11

iw, ih = im.size
# print(iw, ih)


def extend(im: Image.Image, size: tuple[int, int]):
    res = Image.new("RGBA", size)
    res.paste(im, (0, 0, im.width, im.height))
    return res


def merge_horizontal(im1: Image.Image, im2: Image.Image) -> Image.Image:
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im


def onto_background(im: Image.Image, background):
    res = Image.new("RGBA", im.size)
    draw = ImageDraw.Draw(res)
    draw.rectangle(((0, 0), im.size), fill=background, outline=None, width=1)
    res.alpha_composite(im)
    return res


if direction == 'down':
    # if ih <= HEIGHT:
    #     raise Exception(f'Image too short ({ih}px), nothing to scroll')
    frames = (
        extend(im.crop((0, y, WIDTH, y+HEIGHT)), (ANIM_WIDTH, HEIGHT))
        for y in range(0, ih - HEIGHT + 1)
    )

elif direction == 'right':
    # if iw <= WIDTH:
    #     raise Exception(f'Image too narrow ({iw}px), nothing to scroll')
    frames = []
    for x in range(0, iw - WIDTH + 1):
        im.seek(x % im.n_frames)
        frame = extend(im.crop((x, 0, x + WIDTH, HEIGHT)),
                       (ANIM_WIDTH, HEIGHT))
        frames.append(frame)
elif direction == 'left-loop':
    frames = []
    for x in range(-offset, iw + 1):
        im.seek(x % im.n_frames)
        frame = extend(im.crop((-x, 0, -x + WIDTH, HEIGHT)),
                       (ANIM_WIDTH, HEIGHT))
        frames.append(frame)
elif direction == 'move-right-loop':
    frames = []
    x_start = 0
    for x in range(x_start, WIDTH + 1 if loop_repeat == 0 else loop_repeat):
        im.seek(x % im.n_frames)
        frame = Image.new("RGBA", (WIDTH, HEIGHT))
        frame.paste(im, (x, 0))

        if loop_repeat:
            first_x = x
            while first_x+iw > 0:
                first_x -= loop_repeat
            clone_x = first_x
            while clone_x < WIDTH:
                frame.paste(im, (clone_x, 0))
                clone_x = clone_x + loop_repeat
        frame = extend(frame, (WIDTH, HEIGHT))
        if background:
            frame = onto_background(frame, background)
        frame = extend(frame, (ANIM_WIDTH, HEIGHT))
        frames.append(frame)
else:
    raise Exception(f'Invalid direction: {direction}')

res = reduce(
    merge_horizontal,
    frames
)

num_bytes = (res.size[0] * res.size[1]) // 8
print(f"{num_bytes} bytes", file=sys.stderr)
res.save(out_file)
