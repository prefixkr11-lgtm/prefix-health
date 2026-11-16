#!/usr/bin/env python3
"""PREFIX HEALTH 앱 아이콘 생성기 — 크림 · 차콜 · 라임.

downloads/logo-prefix-friendly-2.png 로고에서 뽑은 팔레트를 그대로 쓴다.
  배경 크림    #FDF8F0
  글자 차콜    #282827
  포인트 라임  #B2D434
락업: 라임 '[' + 차콜 'PH' + 작은 라임 스파클·스마일 포인트.
필요한 크기마다 그 크기 그대로(슈퍼샘플 후 영역 평균 축소) 그려서
링잉(흰 테두리) 없이 또렷하게 만든다.

  python3 tools/make_icons.py                 # icons/ 에 4종 저장
  python3 tools/make_icons.py --variants DIR  # 포인트 변형 미리보기
"""
import math
import os
import sys
from PIL import Image, ImageChops, ImageDraw

BG = (253, 248, 240)   # #FDF8F0 크림
INK = (40, 40, 39)     # #282827 차콜
LIME = (178, 212, 52)  # #B2D434 라임

S = 2048               # 기준(마스터) 크기 — 모든 좌표는 이 기준 단위
FILL = 0.85            # 잉크가 사각형에서 차지하는 최대 비율
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'icons')

# ── 비율(모두 캡하이트 CH 기준) ──────────────────────────────
CH = 0.360 * S         # 글자 캡하이트
T = 0.225 * CH         # 글자 획 두께
PW = 0.830 * CH        # 'P' 폭
BH = 0.705 * CH        # 'P' 볼 높이
HW = 0.720 * CH        # 'H' 폭
LGAP = 0.062 * CH      # P · H 사이
BT = 0.200 * CH        # 브래킷 획 두께
BARM = 0.400 * CH      # 브래킷 팔 길이
BOVER = 0.170 * CH     # 브래킷이 캡 위·아래로 솟는 양
BGAP = 0.085 * CH      # 브래킷 · P 사이
ACCENT = 'both'        # 'none' | 'sparkle' | 'smile' | 'both'

SIZES = (('icon-512.png', 512, 3), ('icon-192.png', 192, 4),
         ('apple-touch-icon.png', 180, 4))


def _star(d, cx, cy, r, fill, n=0.52, steps=720):
    """4꼭지 반짝임(스파클). 초타원 |x|^n+|y|^n=1 — 꼭지 사이가 오목하다."""
    pts = []
    for i in range(steps):
        a = 2 * math.pi * i / steps
        ca, sa = abs(math.cos(a)), abs(math.sin(a))
        rad = r / ((ca ** n + sa ** n) ** (1.0 / n))
        pts.append((cx + math.sin(a) * rad, cy - math.cos(a) * rad))
    d.polygon(pts, fill=fill)


def _fillet(d, f, cx, cy, r, sx=1, sy=1, ink=INK, bg=BG):
    """오목한 모서리를 둥글게 다듬는다. sx·sy는 비어 있는 사분면의 방향."""
    x0, x1 = sorted((cx, cx + sx * r))
    y0, y1 = sorted((cy, cy + sy * r))
    d.rectangle([f(x0), f(y0), f(x1), f(y1)], fill=ink)
    d.ellipse([f(cx + sx * r - r), f(cy + sy * r - r),
               f(cx + sx * r + r), f(cy + sy * r + r)], fill=bg)


def _draw(accent, px, sup, g):
    """px 크기 아이콘을 sup배 슈퍼샘플 캔버스에 그린다(여백 포함)."""
    k = px * sup / S                     # 기준 단위 → 캔버스 픽셀
    pad = 0.10 * S
    CW = int(round((S + 2 * pad) * k))

    img = Image.new('RGB', (CW, CW), BG)
    d = ImageDraw.Draw(img)

    ch, t = CH * g, T * g
    pw, bh, hw = PW * g, BH * g, HW * g
    lgap, barm, bgap = LGAP * g, BARM * g, BGAP * g
    bt, bover = BT * g, BOVER * g

    def u(v):
        return v * k

    def f(v):
        return (v + pad) * k

    def bx(x0, y0, x1, y1):
        return [f(x0), f(y0), f(x1), f(y1)]

    def stadium(x0, y0, x1, y1, fill):
        r = min((x1 - x0), (y1 - y0)) / 2
        d.rounded_rectangle(bx(x0, y0, x1, y1), radius=u(r), fill=fill)

    def bowl(x0, y0, x1, y1, fill):
        """왼쪽은 살짝 둥글고 오른쪽은 반원으로 끝나는 활 모양(이음매 없이)."""
        r = (y1 - y0) / 2
        xc = x1 - r
        ov = max(1.0, t * 0.02)                     # 이음매가 벌어지지 않게 살짝 겹친다
        d.rounded_rectangle(bx(x0, y0, xc + ov, y1), radius=u(t * 0.42), fill=fill,
                            corners=(True, False, False, True))
        d.ellipse(bx(xc - r, y0, xc + r, y1), fill=fill)

    def stem(x0, y0, x1, y1):
        """세로획 — 로고 글자처럼 모서리를 살짝만 둥글린 기둥."""
        d.rounded_rectangle(bx(x0, y0, x1, y1), radius=u(t * 0.42), fill=INK)

    lock_w = barm + bgap + pw + lgap + hw
    x = (S - lock_w) / 2
    cap_top = S / 2 - ch / 2
    cap_bot = cap_top + ch

    # ── 브래킷 '[' — 둥근 캡 스트로크 ────────────────────────
    b_top, b_bot = cap_top - bover, cap_bot + bover
    stadium(x, b_top, x + bt, b_bot, LIME)
    stadium(x, b_top, x + barm, b_top + bt, LIME)
    stadium(x, b_bot - bt, x + barm, b_bot, LIME)

    # ── 'P' ──────────────────────────────────────────────────
    px0 = x + barm + bgap
    stem(px0, cap_top, px0 + t, cap_bot)                              # 세로획
    bowl(px0, cap_top, px0 + pw, cap_top + bh, INK)                   # 볼
    stadium(px0 + t, cap_top + t, px0 + pw - t, cap_top + bh - t, BG)  # 카운터
    _fillet(d, f, px0 + t, cap_top + bh, t * 0.16)                     # 볼·세로획 오목 모서리

    # ── 'H' ──────────────────────────────────────────────────
    hx = px0 + pw + lgap
    stem(hx, cap_top, hx + t, cap_bot)
    stem(hx + hw - t, cap_top, hx + hw, cap_bot)
    bar_cy, bar_t = cap_top + ch * 0.515, t * 1.05     # 가로획은 살짝 두껍게(광학 보정)
    d.rectangle(bx(hx + t * 0.5, bar_cy - bar_t / 2, hx + hw - t * 0.5, bar_cy + bar_t / 2),
                fill=INK)
    # 가로획·세로획이 만나는 오목 모서리 네 곳
    for sx_, cxx in ((1, hx + t), (-1, hx + hw - t)):
        for sy_, cyy in ((1, bar_cy + bar_t / 2), (-1, bar_cy - bar_t / 2)):
            _fillet(d, f, cxx, cyy, t * 0.14, sx=sx_, sy=sy_)

    # ── 라임 포인트 ──────────────────────────────────────────
    if accent in ('sparkle', 'both'):
        _star(d, u(hx + hw + ch * 0.105 + pad), u(cap_top + ch * 0.055 + pad), u(ch * 0.098), LIME)

    if accent in ('smile', 'both'):
        smile_w, th = ch * 0.440, ch * 0.055
        lis = int(round(u(smile_w + th * 4)))
        lay = Image.new('RGBA', (lis, lis), (0, 0, 0, 0))
        ld = ImageDraw.Draw(lay)
        p2 = 2 * u(th)
        ld.arc([p2, p2, lis - p2, lis * 0.62],
               start=15, end=165, fill=LIME + (255,), width=int(round(u(th))))
        lay = lay.rotate(-7, resample=Image.BICUBIC, expand=True)
        lay = lay.crop(lay.split()[3].getbbox())
        lp = (int(round(u(hx + hw + ch * 0.030 + pad))) - lay.width,
              int(round(u(cap_bot + ch * 0.010 + pad))))
        img.paste(lay, lp, lay)

    return img


def _ink_bbox(img):
    return ImageChops.difference(img, Image.new('RGB', img.size, BG)).getbbox()


def render(accent=ACCENT, px=S, sup=2):
    """px 크기 아이콘. 잉크 경계로 크롭 → 정중앙, 넘치면 비율 유지 축소."""
    g = 1.0
    probe = _draw(accent, 320, 2, g)
    bb = _ink_bbox(probe)
    fill = max((bb[2] - bb[0]) / probe.width, (bb[3] - bb[1]) / probe.height) / FILL
    if fill > 1:
        g /= fill

    img = _draw(accent, px, sup, g)
    bb = _ink_bbox(img)
    crop = img.crop(bb)
    crop = crop.reduce(sup) if sup > 1 else crop
    out = Image.new('RGB', (px, px), BG)
    out.paste(crop, ((px - crop.width) // 2, (px - crop.height) // 2))
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    if '--variants' in sys.argv:
        dst = sys.argv[sys.argv.index('--variants') + 1]
        os.makedirs(dst, exist_ok=True)
        for acc in ('none', 'sparkle', 'smile', 'both'):
            render(acc, 512, 3).save(os.path.join(dst, 'v-%s-512.png' % acc))
            render(acc, 192, 4).save(os.path.join(dst, 'v-%s-192.png' % acc))
        return
    render(ACCENT, S, 2).save(os.path.join(OUT, 'icon-master-2048.png'), optimize=True)
    print('wrote icons/icon-master-2048.png 2048x2048')
    for name, px, sup in SIZES:
        render(ACCENT, px, sup).save(os.path.join(OUT, name), optimize=True)
        print('wrote icons/%s %dx%d' % (name, px, px))


if __name__ == '__main__':
    main()
