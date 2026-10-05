"""Echo Peel icon: a white video card on the Echo teal tile, its top corner peeled back, with the Echo waveform
inside, so it reads as "the sound under the picture" next to Echo Loop+ and Echo Stems.
Run it with Python 3 (needs Pillow and NumPy): python3 make_icons.py"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

OUT = os.path.dirname(os.path.abspath(__file__))
S = 2048          # drawn large, then scaled down, for smooth edges
C = S / 2

# Background: teal at the top left to deep cyan at the bottom right, with a soft light in the top corner.
a = np.array([45, 212, 191], dtype=float)   # teal-400
b = np.array([21, 94, 117], dtype=float)    # cyan-800
yy, xx = np.mgrid[0:S, 0:S]
t = ((xx + yy) / (2 * S - 2))[..., None]
img = Image.fromarray((a * (1 - t) + b * t).astype(np.uint8), "RGB").convert("RGBA")
glow = Image.new("L", (S, S), 0)
ImageDraw.Draw(glow).ellipse([-S * 0.25, -S * 0.35, S * 0.75, S * 0.55], fill=56)
glow = glow.filter(ImageFilter.GaussianBlur(S * 0.08))
img = Image.composite(Image.new("RGBA", (S, S), (255, 255, 255, 255)), img, glow)

# The card (a portrait video frame) with its top-right corner cut off along the fold line.
x0, x1, y0, y1 = 0.25 * S, 0.75 * S, 0.17 * S, 0.83 * S
fold = 0.19 * S
card = Image.new("L", (S, S), 0)
cd = ImageDraw.Draw(card)
cd.rounded_rectangle([x0, y0, x1, y1], radius=0.075 * S, fill=255)
cd.polygon([(x1 - fold, y0 - 2), (x1 + 2, y0 - 2), (x1 + 2, y0 + fold)], fill=0)

# A soft shadow under the card, then the card itself.
shadow = card.filter(ImageFilter.GaussianBlur(S * 0.03)).point(lambda v: int(v * 0.28))
img = Image.composite(Image.new("RGBA", (S, S), (8, 40, 56, 255)), img, shadow.transform((S, S), Image.AFFINE, (1, 0, 0, 0, 1, -S * 0.018)))
img = Image.composite(Image.new("RGBA", (S, S), (255, 255, 255, 255)), img, card)

# The peeled flap: the cut-off corner folded down over the card, with a shadow beneath it.
p1, p2, q = (x1 - fold, y0), (x1, y0 + fold), (x1 - fold, y0 + fold)
flap_shadow = Image.new("L", (S, S), 0)
ImageDraw.Draw(flap_shadow).polygon([p1, p2, (q[0] - 0.02 * S, q[1] + 0.03 * S)], fill=120)
flap_shadow = flap_shadow.filter(ImageFilter.GaussianBlur(S * 0.018))
flap_shadow = Image.composite(flap_shadow, Image.new("L", (S, S), 0), card)   # only on the card
img = Image.composite(Image.new("RGBA", (S, S), (14, 80, 100, 255)), img, flap_shadow)
flap = Image.new("L", (S, S), 0)
ImageDraw.Draw(flap).polygon([p1, p2, q], fill=255)
# the flap is lighter along the fold and a little darker towards its tip, like a curling sticker
u = np.clip(((xx - p1[0]) * -1 + (yy - p1[1])) / (2 * fold), 0, 1)[..., None]
flap_col = np.array([236, 254, 255], float) * (1 - u) + np.array([165, 243, 252], float) * u
img = Image.composite(Image.fromarray(flap_col.astype(np.uint8), "RGB").convert("RGBA"), img, flap)

# The Echo waveform inside the card.
d = ImageDraw.Draw(img)
heights = [0.09, 0.19, 0.31, 0.21, 0.27, 0.14, 0.07]
bw, gap = 0.030 * S, 0.024 * S
total = len(heights) * bw + (len(heights) - 1) * gap
bx = C - total / 2
cy = 0.585 * S
for i, hgt in enumerate(heights):
    x = bx + i * (bw + gap)
    hh = hgt * S
    d.rounded_rectangle([x, cy - hh / 2, x + bw, cy + hh / 2], radius=bw / 2, fill=(14, 116, 144, 255))

img = img.convert("RGB")
for size, name in [(512, "icon-512.png"), (192, "icon-192.png"), (180, "icon-180.png")]:
    img.resize((size, size), Image.LANCZOS).save(os.path.join(OUT, name), optimize=True)
print("icons written to", OUT)
