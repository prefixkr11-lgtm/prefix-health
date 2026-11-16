#!/usr/bin/env python3
"""Prehealth 앱 아이콘 가져오기 — 코랄 오렌지 + 화이트 러닝 P.

원본: downloads/icon-ph-10-01.png (1254x1254, RGB)
  · 원본을 RGB(불투명)로 유지한 채 LANCZOS로 2048 마스터까지 키우고,
    살짝 언샤프를 걸어 가장자리를 살린다.
  · 나머지 크기는 2048 마스터에서 LANCZOS로 줄여 만든다(한 번만 줄여
    단계별 리샘플링으로 생기는 흐림을 피한다).

  python3 tools/import_icon.py                # icons/ 에 5종 저장
  python3 tools/import_icon.py SRC            # 다른 원본으로
"""
import os
import sys

from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'icons')
DEFAULT_SRC = os.path.join(os.path.dirname(ROOT), '..', 'downloads', 'icon-ph-10-01.png')

MASTER = 2048


def _rgb(im):
    """알파가 있으면 흰 배경 위에 합성해 불투명 RGB로 만든다."""
    im = Image.open(im)
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
        bg = Image.new('RGB', im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        return bg
    return im.convert('RGB')


def _resize(im, size):
    return im.resize((size, size), Image.LANCZOS)


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SRC
    os.makedirs(OUT, exist_ok=True)

    base = _rgb(src)
    if base.width != base.height:
        side = min(base.size)
        left = (base.width - side) // 2
        top = (base.height - side) // 2
        base = base.crop((left, top, left + side, top + side))

    # 마스터: 원본보다 크면 LANCZOS 업스케일 + 약한 언샤프로 가장자리 선명도 보정
    master = _resize(base, MASTER)
    if base.width < MASTER:
        master = master.filter(ImageFilter.UnsharpMask(radius=2.4, percent=110, threshold=2))

    targets = (
        ('icon-master-2048.png', MASTER),
        ('icon-1024.png', 1024),
        ('apple-touch-icon.png', 1024),
        ('icon-512.png', 512),
        ('icon-192.png', 192),
    )
    for name, size in targets:
        img = master if size == MASTER else _resize(master, size)
        path = os.path.join(OUT, name)
        img.save(path, 'PNG', optimize=True)
        print(f'{name:24s} {size}x{size}  {os.path.getsize(path):,} bytes')

    print(f'원본 {base.size[0]}x{base.size[1]} → 마스터 {MASTER}x{MASTER}')


if __name__ == '__main__':
    main()
