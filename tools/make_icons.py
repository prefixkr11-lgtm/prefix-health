#!/usr/bin/env python3
"""PREFIX HEALTH 앱 아이콘 생성기.

다크 차콜(#141416) 배경 + 라임(#B8FF3B) 브래킷 '[' + 크림(#F5F2EB) 'PH'.
2048px 마스터를 그린 뒤 LANCZOS로 512 / 192 / 180 사이즈를 만든다.
"""
import os
from PIL import Image, ImageDraw, ImageFont

BG = (20, 20, 22)          # #141416
LIME = (184, 255, 59)      # #B8FF3B
CREAM = (245, 242, 235)    # #F5F2EB

S = 2048
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'icons')
FONT = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'

STROKE = 172      # 브래킷 두께
ARM = 312         # 브래킷 위/아래 팔 길이
TOP, BOT = 505, 1543
GAP = 88          # 브래킷과 'PH' 사이
TYPE = 900        # 'PH' 폰트 크기


def draw_master():
    img = Image.new('RGB', (S, S), BG)
    d = ImageDraw.Draw(img)

    font = ImageFont.truetype(FONT, TYPE)
    box = d.textbbox((0, 0), 'PH', font=font)
    tw, th = box[2] - box[0], box[3] - box[1]

    # 전체 록업(브래킷 + 글자)을 가로 중앙에 광학 정렬
    lock_w = ARM + GAP + tw
    x = round((S - lock_w) / 2)

    # 브래킷 '['
    d.rectangle([x, TOP, x + STROKE, BOT], fill=LIME)
    d.rectangle([x, TOP, x + ARM, TOP + STROKE], fill=LIME)
    d.rectangle([x, BOT - STROKE, x + ARM, BOT], fill=LIME)

    # 'PH' — 브래킷 세로 중앙에 정렬
    cy = (TOP + BOT) / 2
    tx = x + ARM + GAP
    d.text((tx - box[0], cy - th / 2 - box[1]), 'PH', font=font, fill=CREAM)
    return img


def main():
    os.makedirs(OUT, exist_ok=True)
    master = draw_master()
    master.save(os.path.join(OUT, 'icon-master-2048.png'), optimize=True)
    for name, px in (('icon-512.png', 512), ('icon-192.png', 192), ('apple-touch-icon.png', 180)):
        master.resize((px, px), Image.LANCZOS).save(os.path.join(OUT, name), optimize=True)
        print('wrote icons/' + name, str(px) + 'x' + str(px))


if __name__ == '__main__':
    main()
