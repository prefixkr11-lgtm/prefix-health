#!/usr/bin/env python3
"""v14: 앱 내부 UI를 플랫·매트 미니멀(네온·글로우·그라데이션 제거)로 정리한다."""
import pathlib, sys

P = pathlib.Path('/workspace/work/prefix-health-pages/index.html')
src = P.read_text()

REPL = []

def rep(old, new):
    REPL.append((old, new))

# ---------------- 팔레트 ----------------
rep("""  :root{
    --bg:#141416;
    --bg2:#0A0A0B;
    --card:rgba(245,242,235,.045);
    --ink:#F5F2EB;
    --emerald:#10664A;        /* 딥 에메랄드 — 앱 아이콘 배경·[P] 배지 */
    --emerald-2:#34D399;      /* 어두운 배경 위 작은 글씨·포인트 (대비 9.6:1) */
    --emerald-3:#10B981;      /* 채움·그래프·글로우용 선명한 에메랄드 */
    --emerald-btn:#0F8555;    /* 흰 글씨 버튼 바탕 (흰색 대비 4.66:1) */
    --emerald-soft:rgba(16,185,129,.12);
    --good:#3FD37A;           /* 자세 양호(OK) — 판정색 */
    --dim:rgba(245,242,235,.56);
    --dim2:rgba(245,242,235,.34);
    --line:rgba(245,242,235,.12);
    --warn:#FFC24B;
    --bad:#FF3B62;            /* 교정 필요 — 판정색 로즈 레드 */
  }""",
"""  :root{
    --bg:#0F0F11;             /* 매트 다크 바탕 */
    --bg2:#0B0B0C;            /* 무대(영상) 바탕 */
    --card:#161618;           /* 카드 — 단색 판 */
    --card2:#131315;          /* 안쪽 판·입력 바탕 */
    --ink:#F2F2F0;
    --emerald:#10664A;        /* 딥 에메랄드 — 앱 아이콘 배경·[P] 배지 */
    --emerald-2:#6DB79B;      /* 어두운 배경 위 포인트 글씨 (대비 7.9:1) — 차분한 세이지 에메랄드 */
    --emerald-3:#1B7A58;      /* 막대·괘선 등 단색 채움 */
    --emerald-btn:#167A57;    /* 흰 글씨 버튼 바탕 (흰색 대비 5.3:1) */
    --emerald-soft:#17211D;   /* 선택된 카드 바탕 — 단색 */
    --good:#4FBE86;           /* 자세 양호(OK) — 판정색 */
    --dim:rgba(242,242,240,.56);
    --dim2:rgba(242,242,240,.34);
    --line:#262629;
    --warn:#D9AC57;
    --bad:#D8576E;            /* 교정 필요 — 판정색 로즈 레드 */
  }""")

rep(":focus-visible{outline:2px solid rgba(52,211,153,.75)",
    ":focus-visible{outline:2px solid rgba(109,183,155,.8)")
rep("::selection{background:rgba(16,185,129,.35);color:#fff}",
    "::selection{background:rgba(27,122,88,.55);color:#fff}")

# ---------------- 헤더 ----------------
rep("background:rgba(20,20,22,.88);backdrop-filter:blur(16px)",
    "background:rgba(15,15,17,.9);backdrop-filter:blur(16px)")
rep("""  .brand .mark{
    width:25px;height:25px;flex:0 0 auto;border-radius:8px;background:var(--emerald);color:#fff;
    display:grid;place-items:center;font-size:15px;font-weight:900;letter-spacing:-.04em;
    box-shadow:0 3px 12px rgba(16,185,129,.34), inset 0 1px 0 rgba(255,255,255,.22);
  }""",
"""  .brand .mark{
    width:25px;height:25px;flex:0 0 auto;border-radius:7px;background:var(--emerald);color:#fff;
    display:grid;place-items:center;font-size:15px;font-weight:900;letter-spacing:-.04em;
  }""")

# PRO 배지: 그라데이션·글로우 없이 단정한 테두리 필
rep("""  .proBadge{
    display:inline-flex;align-items:center;gap:4px;flex:0 0 auto;border:0;cursor:pointer;
    background:linear-gradient(135deg,#0F8555,#0A6B47);color:#fff;
    font-size:10px;font-weight:900;letter-spacing:.14em;padding:6px 9px;border-radius:8px;
    box-shadow:0 3px 12px rgba(16,185,129,.32);transition:.15s;
  }
  .proBadge:hover{filter:brightness(1.07)}
  .proBadge::before{content:"\U0001F48E";font-size:9.5px;letter-spacing:0}""",
"""  .proBadge{
    display:inline-flex;align-items:center;gap:5px;flex:0 0 auto;cursor:pointer;
    background:none;border:1px solid #2C5748;color:var(--emerald-2);
    font-size:10px;font-weight:900;letter-spacing:.14em;padding:5px 10px;border-radius:999px;
    transition:border-color .15s,color .15s;
  }
  .proBadge:hover{border-color:#3D7360;color:#8BC9B1}
  .proBadge::before{content:"";width:4px;height:4px;border-radius:50%;background:currentColor;opacity:.9}""")

# ---------------- 운동 선택 · 레벨 ----------------
rep(".ex-btn[aria-selected=\"true\"]{background:var(--emerald-soft);border-color:rgba(16,185,129,.5)}",
    ".ex-btn[aria-selected=\"true\"]{background:var(--emerald-soft);border-color:#2C5748}")
rep(".ex-btn[aria-selected=\"true\"] .no{color:rgba(52,211,153,.7)}",
    ".ex-btn[aria-selected=\"true\"] .no{color:var(--emerald-2);opacity:.75}")
rep("background:rgba(10,10,11,.55);border:1px solid var(--line);border-radius:11px;padding:3px;flex:0 0 auto}",
    "background:#101012;border:1px solid var(--line);border-radius:10px;padding:3px;flex:0 0 auto}")
rep(".lv-btn[aria-pressed=\"true\"]{background:var(--emerald-btn);color:#fff;box-shadow:0 3px 12px rgba(16,185,129,.25)}",
    ".lv-btn[aria-pressed=\"true\"]{background:var(--emerald-btn);color:#fff}")
rep(".lv-btn[data-level=\"advanced\"][aria-pressed=\"true\"]{background:linear-gradient(135deg,#B4562A,#8A3F1E);box-shadow:0 3px 12px rgba(255,138,76,.25)}",
    ".lv-btn[data-level=\"advanced\"][aria-pressed=\"true\"]{background:#7A4224}")

# ---------------- 무대 · HUD ----------------
rep(".modes{display:inline-flex;background:rgba(245,242,235,.05);border:1px solid var(--line);border-radius:11px;padding:3px;gap:3px;margin-bottom:10px}",
    ".modes{display:inline-flex;background:#131315;border:1px solid var(--line);border-radius:10px;padding:3px;gap:3px;margin-bottom:10px}")
rep("position:relative;background:var(--bg2);border:1px solid var(--line);border-radius:16px;",
    "position:relative;background:var(--bg2);border:1px solid var(--line);border-radius:14px;")
rep(".chip.accent{border-color:rgba(16,185,129,.55);color:var(--emerald-2);background:rgba(20,20,22,.82)}",
    ".chip.accent{border-color:#2C5748;color:var(--emerald-2);background:rgba(15,15,17,.86)}")
rep(".chip.good{border-color:rgba(63,211,122,.5);color:var(--good)}",
    ".chip.good{border-color:rgba(79,190,134,.5);color:var(--good)}")
rep(".chip.bad{border-color:rgba(255,59,98,.55);color:var(--bad)}",
    ".chip.bad{border-color:rgba(216,87,110,.55);color:var(--bad)}")
rep(".chip.warn{border-color:rgba(255,194,75,.5);color:var(--warn)}",
    ".chip.warn{border-color:rgba(217,172,87,.5);color:var(--warn)}")
rep(".chip.quality{border-color:rgba(245,242,235,.2);", ".chip.quality{border-color:rgba(242,242,240,.2);")
rep(".chip.quality[data-state=\"good\"]{border-color:rgba(63,211,122,.55);color:var(--good)}",
    ".chip.quality[data-state=\"good\"]{border-color:rgba(79,190,134,.55);color:var(--good)}")
rep(".chip.quality[data-state=\"fair\"]{border-color:rgba(255,194,75,.5);color:var(--warn)}",
    ".chip.quality[data-state=\"fair\"]{border-color:rgba(217,172,87,.5);color:var(--warn)}")
rep(".chip.quality[data-state=\"bad\"]{border-color:rgba(255,59,98,.55);color:var(--bad)}",
    ".chip.quality[data-state=\"bad\"]{border-color:rgba(216,87,110,.55);color:var(--bad)}")
rep(".chip.pause{border-color:rgba(255,194,75,.65);color:var(--warn);background:rgba(20,20,22,.9)}",
    ".chip.pause{border-color:rgba(217,172,87,.6);color:var(--warn);background:rgba(15,15,17,.92)}")
rep(".bigCount .v{font-size:30px;font-weight:800;color:#fff;letter-spacing:-.03em;text-shadow:0 1px 10px rgba(0,0,0,.45)}",
    ".bigCount .v{font-size:30px;font-weight:800;color:#fff;letter-spacing:-.03em}")
rep("gap:12px;text-align:center;padding:22px;background:radial-gradient(circle at 50% 40%,rgba(245,242,235,.05),transparent 62%);",
    "gap:12px;text-align:center;padding:22px;")

# ---------------- 버튼 · 입력 ----------------
rep("""    background:rgba(245,242,235,.06);border:1px solid var(--line);border-radius:10px;
    padding:9px 13px;font-size:12.5px;font-weight:700;cursor:pointer;transition:.14s;""",
"""    background:#1A1A1D;border:1px solid var(--line);border-radius:10px;
    padding:9px 13px;font-size:12.5px;font-weight:700;cursor:pointer;transition:.14s;""")
rep(".btn:hover:not(:disabled){background:rgba(245,242,235,.11)}",
    ".btn:hover:not(:disabled){background:#242428}")
rep(".btn.primary{background:var(--emerald-btn);border-color:var(--emerald-btn);color:#fff;font-weight:800;box-shadow:0 4px 14px rgba(16,185,129,.28)}",
    ".btn.primary{background:var(--emerald-btn);border-color:var(--emerald-btn);color:#fff;font-weight:800}")
rep(".btn.primary:hover:not(:disabled){background:#0C7A4C;border-color:#0C7A4C}",
    ".btn.primary:hover:not(:disabled){background:#1B8A63;border-color:#1B8A63}")
rep("""    background:rgba(245,242,235,.06);border:1px solid var(--line);border-radius:10px;
    padding:9px 8px;font-size:12px;font-weight:700;color:var(--ink);min-height:40px;""",
"""    background:#1A1A1D;border:1px solid var(--line);border-radius:10px;
    padding:9px 8px;font-size:12px;font-weight:700;color:var(--ink);min-height:40px;""")
rep("select.speed option{background:#1c1c20;color:var(--ink)}",
    "select.speed option{background:#161618;color:var(--ink)}")
rep("""    border:1px solid var(--line);background:rgba(245,242,235,.05);
  }
  .notice[data-level="warn"]{border-color:rgba(255,194,75,.42);background:rgba(255,194,75,.09)}
  .notice[data-level="bad"]{border-color:rgba(255,59,98,.45);background:rgba(255,59,98,.09)}
  .notice[data-level="good"]{border-color:rgba(63,211,122,.42);background:rgba(63,211,122,.09)}""",
"""    border:1px solid var(--line);background:var(--card2);
  }
  .notice[data-level="warn"]{border-color:rgba(217,172,87,.45);background:rgba(217,172,87,.08)}
  .notice[data-level="bad"]{border-color:rgba(216,87,110,.45);background:rgba(216,87,110,.08)}
  .notice[data-level="good"]{border-color:rgba(79,190,134,.42);background:rgba(79,190,134,.08)}""")

# ---------------- 사이드 ----------------
rep("border-radius:8px;background:rgba(245,242,235,.04);border-left:2px solid var(--dim2)}",
    "border-radius:8px;background:var(--card2);border-left:2px solid var(--dim2)}")
rep(".scoreBar{height:4px;border-radius:99px;background:rgba(245,242,235,.1);overflow:hidden;margin-top:7px}",
    ".scoreBar{height:4px;border-radius:99px;background:#262629;overflow:hidden;margin-top:7px}")

# ---------------- 리포트 ----------------
rep(".report{margin-top:16px;border:1px solid rgba(16,185,129,.3);border-radius:16px;padding:16px;background:rgba(16,185,129,.05)}",
    ".report{margin-top:16px;border:1px solid #2A4A3E;border-radius:14px;padding:16px;background:#121714}")
rep(".reportGrid>div:first-child{grid-column:1/-1}", ".reportGrid>div:first-child{grid-column:1/-1}")
rep(".rbig{background:rgba(20,20,22,.5);border:1px solid var(--line);border-radius:12px;padding:11px 13px}",
    ".rbig{background:var(--card2);border:1px solid var(--line);border-radius:11px;padding:11px 13px}")
rep(".issueChip{font-size:11.5px;font-weight:700;padding:5px 9px;border-radius:999px;border:1px solid var(--line);background:rgba(245,242,235,.05)}",
    ".issueChip{font-size:11.5px;font-weight:700;padding:5px 9px;border-radius:999px;border:1px solid var(--line);background:var(--card2)}")
rep(".issueChip[data-lv=\"bad\"]{border-color:rgba(255,59,98,.45);color:var(--bad)}",
    ".issueChip[data-lv=\"bad\"]{border-color:rgba(216,87,110,.45);color:var(--bad)}")
rep(".issueChip[data-lv=\"warn\"]{border-color:rgba(255,194,75,.45);color:var(--warn)}",
    ".issueChip[data-lv=\"warn\"]{border-color:rgba(217,172,87,.45);color:var(--warn)}")
rep(".issueChip[data-lv=\"good\"]{border-color:rgba(63,211,122,.45);color:var(--good)}",
    ".issueChip[data-lv=\"good\"]{border-color:rgba(79,190,134,.45);color:var(--good)}")
rep("border-bottom:1px solid rgba(245,242,235,.06)}", "border-bottom:1px solid rgba(242,242,240,.06)}")

# ---------------- 기록 ----------------
rep(".wb .wc{width:100%;border-radius:6px 6px 3px 3px;background:rgba(245,242,235,.09);min-height:4px;transition:.2s}",
    ".wb .wc{width:100%;border-radius:5px 5px 2px 2px;background:#262629;min-height:4px;transition:.2s}")
rep(".wb .wc.on{background:linear-gradient(180deg,#34D399,#10B981)}",
    ".wb .wc.on{background:var(--emerald-3)}")
rep(".wb.today .wc.on{box-shadow:0 0 0 1px rgba(52,211,153,.6),0 4px 14px rgba(16,185,129,.35)}",
    ".wb.today .wc.on{background:var(--emerald-2)}")
rep("""    background:rgba(245,242,235,.04);border:1px solid transparent;border-radius:11px;padding:8px 10px;transition:.14s;""",
"""    background:var(--card2);border:1px solid transparent;border-radius:10px;padding:8px 10px;transition:.14s;""")
rep(".recRow:hover{background:rgba(245,242,235,.085);border-color:var(--line)}",
    ".recRow:hover{background:#1B1B1E;border-color:var(--line)}")
rep("color:var(--emerald-2);border:1px solid rgba(16,185,129,.45);border-radius:999px;",
    "color:var(--emerald-2);border:1px solid #2C5748;border-radius:999px;")
rep(".recRow .lv.adv{color:#FF9A5E;border-color:rgba(255,138,76,.5)}",
    ".recRow .lv.adv{color:#C98F63;border-color:#5E4630}")

# ---------------- Pro 잠금 카드 ----------------
rep("""    background:linear-gradient(120deg,rgba(16,185,129,.13),rgba(245,242,235,.03));
    border:1px dashed rgba(16,185,129,.5);border-radius:14px;padding:12px 13px;transition:.15s;
  }
  .proLock:hover{border-color:rgba(16,185,129,.8);background:linear-gradient(120deg,rgba(16,185,129,.18),rgba(245,242,235,.04))}""",
"""    background:var(--card2);
    border:1px dashed #2C4E41;border-radius:12px;padding:12px 13px;transition:.15s;
  }
  .proLock:hover{border-color:#3D7360;background:#161B19}""")
rep("border:1px solid rgba(16,185,129,.45);border-radius:999px;padding:4px 8px;background:rgba(20,20,22,.5);",
    "border:1px solid #2C5748;border-radius:999px;padding:4px 8px;background:#15171A;")

# ---------------- 모달 ----------------
rep(".modalBackdrop{position:absolute;inset:0;background:rgba(6,6,7,.74);",
    ".modalBackdrop{position:absolute;inset:0;background:rgba(8,8,9,.76);")
rep("""    background:#18181B;border:1px solid var(--line);border-radius:22px 22px 0 0;
    box-shadow:0 -12px 60px rgba(0,0,0,.65);""",
"""    background:var(--card);border:1px solid var(--line);border-radius:20px 20px 0 0;""")
rep(".sheetClose:hover{color:var(--ink);background:rgba(245,242,235,.08)}",
    ".sheetClose:hover{color:var(--ink);background:#1E1E21}")
rep("""    width:34px;height:34px;flex:0 0 auto;border-radius:11px;background:linear-gradient(135deg,#12855A,#10664A);
    display:grid;place-items:center;font-size:17px;font-weight:900;color:#fff;letter-spacing:-.04em;
    box-shadow:0 4px 14px rgba(16,185,129,.35);""",
"""    width:34px;height:34px;flex:0 0 auto;border-radius:9px;background:var(--emerald);
    display:grid;place-items:center;font-size:17px;font-weight:900;color:#fff;letter-spacing:-.04em;""")
rep(".plan{display:flex;align-items:center;gap:10px;width:100%;text-align:left;cursor:pointer;background:rgba(245,242,235,.04);border:1px solid var(--line);border-radius:12px;padding:11px 13px;transition:.14s}",
    ".plan{display:flex;align-items:center;gap:10px;width:100%;text-align:left;cursor:pointer;background:var(--card2);border:1px solid var(--line);border-radius:11px;padding:11px 13px;transition:.14s}")
rep(".plan:hover{background:rgba(245,242,235,.07)}", ".plan:hover{background:#1B1B1E}")
rep(".plan[aria-pressed=\"true\"]{border-color:rgba(16,185,129,.65);background:rgba(16,185,129,.1)}",
    ".plan[aria-pressed=\"true\"]{border-color:#2C5748;background:var(--emerald-soft)}")
rep(".benefits li{display:flex;gap:9px;font-size:12.5px;line-height:1.5;color:rgba(245,242,235,.86)}",
    ".benefits li{display:flex;gap:9px;font-size:12.5px;line-height:1.5;color:rgba(242,242,240,.86)}")
rep(".cardPreviewWrap{margin:12px 0 10px;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#0A0A0B}",
    ".cardPreviewWrap{margin:12px 0 10px;border-radius:12px;overflow:hidden;border:1px solid var(--line);background:var(--bg2)}")

# ---------------- 토스트 ----------------
rep("""    background:rgba(24,24,27,.97);border:1px solid rgba(16,185,129,.55);color:var(--ink);
    font-size:12.5px;font-weight:700;padding:11px 15px;border-radius:12px;text-align:center;
    box-shadow:0 12px 36px rgba(0,0,0,.55);opacity:0;pointer-events:none;transition:opacity .2s,transform .2s;""",
"""    background:#1A1A1D;border:1px solid #2C5748;color:var(--ink);
    font-size:12.5px;font-weight:700;padding:11px 15px;border-radius:11px;text-align:center;
    opacity:0;pointer-events:none;transition:opacity .2s,transform .2s;""")

# ---------------- 설치 안내 ----------------
rep("""    border:1px solid rgba(16,185,129,.28);border-radius:12px;
    background:rgba(16,185,129,.08);font-size:12px;line-height:1.45;color:var(--ink);""",
"""    border:1px solid #2C4E41;border-radius:11px;
    background:#121816;font-size:12px;line-height:1.45;color:var(--ink);""")

# ---------------- 스플래시 H 색 ----------------
rep(".splashH{color:#34D399;margin-left:.02em;animation:splashFlyH",
    ".splashH{color:#6DB79B;margin-left:.02em;animation:splashFlyH")

# ---------------- 무대 빈 화면 SVG ----------------
rep('stroke="#34D399" stroke-width="2.2" opacity=".85"', 'stroke="#6DB79B" stroke-width="2.2" opacity=".85"')
rep('stroke="#34D399" stroke-width="2.2" stroke-linecap="round" opacity=".7"',
    'stroke="#6DB79B" stroke-width="2.2" stroke-linecap="round" opacity=".7"')
rep('stroke="#F5F2EB" stroke-width="2.2" stroke-linecap="round" opacity=".7"',
    'stroke="#F2F2F0" stroke-width="2.2" stroke-linecap="round" opacity=".7"')

# ---------------- 라이브 오버레이 스켈레톤 ----------------
rep("ctx.strokeStyle = isBad ? 'rgba(255,59,98,.92)' : 'rgba(245,242,235,.55)';",
    "ctx.strokeStyle = isBad ? 'rgba(216,87,110,.92)' : 'rgba(242,242,240,.55)';")
rep("ctx.lineWidth = 1.5; ctx.strokeStyle = 'rgba(10,10,11,.8)'; ctx.stroke();",
    "ctx.lineWidth = 1.5; ctx.strokeStyle = 'rgba(8,8,9,.8)'; ctx.stroke();")
rep("ctx.strokeStyle = a.bad ? 'rgba(255,59,98,.85)' : 'rgba(63,211,122,.5)';",
    "ctx.strokeStyle = a.bad ? 'rgba(216,87,110,.85)' : 'rgba(79,190,134,.5)';")

# ---------------- 결과 카드 (1080×1350) ----------------
rep("""  const MINT = '#10B981', MINT2 = '#34D399', DEEP = '#10664A', INK = '#F5F2EB', DIM = 'rgba(245,242,235,.56)', DIM2 = 'rgba(245,242,235,.34)';
  g.textBaseline = 'alphabetic';
  g.textAlign = 'left';
  g.fillStyle = '#141416';
  g.fillRect(0, 0, W, H);

  /* 배경 글로우 + 결 */
  const glow = g.createRadialGradient(W * 0.84, -140, 40, W * 0.84, -140, 980);
  glow.addColorStop(0, 'rgba(16,185,129,.45)');
  glow.addColorStop(.5, 'rgba(16,185,129,.08)');
  glow.addColorStop(1, 'rgba(16,185,129,0)');
  g.fillStyle = glow; g.fillRect(0, 0, W, H);
  const low = g.createLinearGradient(0, H * 0.5, 0, H);
  low.addColorStop(0, 'rgba(0,0,0,0)');
  low.addColorStop(1, 'rgba(0,0,0,.55)');
  g.fillStyle = low; g.fillRect(0, 0, W, H);
  g.fillStyle = MINT; g.fillRect(0, 0, W, 10);""",
"""  /* v14: 네온·글로우·그라데이션 없이 매트 다크 + 단색 에메랄드 포인트만 */
  const MINT = '#1B7A58', MINT2 = '#6DB79B', DEEP = '#10664A', INK = '#F2F2F0',
        DIM = 'rgba(242,242,240,.56)', DIM2 = 'rgba(242,242,240,.34)',
        LINE = '#262629', PANEL = '#131315';
  g.textBaseline = 'alphabetic';
  g.textAlign = 'left';
  g.fillStyle = '#0F0F11';
  g.fillRect(0, 0, W, H);

  /* 상단 헤어라인 — 단색 에메랄드 포인트 */
  g.fillStyle = MINT; g.fillRect(0, 0, W, 10);""")

rep("""  const lx = 80, ly = 92, ls = 104;
  roundRect(g, lx, ly, ls, ls, 26);
  const lg = g.createLinearGradient(lx, ly, lx + ls, ly + ls);
  lg.addColorStop(0, '#12855A'); lg.addColorStop(1, DEEP);
  g.fillStyle = lg; g.fill();""",
"""  const lx = 80, ly = 92, ls = 104;
  roundRect(g, lx, ly, ls, ls, 22);
  g.fillStyle = DEEP; g.fill();""")

rep("g.strokeStyle = 'rgba(245,242,235,.14)'; g.lineWidth = 2;\n  g.beginPath(); g.moveTo(80, 266); g.lineTo(W - 80, 266); g.stroke();",
    "g.strokeStyle = LINE; g.lineWidth = 2;\n  g.beginPath(); g.moveTo(80, 266); g.lineTo(W - 80, 266); g.stroke();")

rep("""    g.fillStyle = isAdv ? 'rgba(255,138,76,.16)' : 'rgba(16,185,129,.16)';
    g.fill();
    g.strokeStyle = isAdv ? 'rgba(255,138,76,.55)' : 'rgba(16,185,129,.5)';
    g.lineWidth = 1.5; g.stroke();
    g.fillStyle = isAdv ? '#FFB27E' : MINT2;""",
"""    g.fillStyle = isAdv ? '#1E1813' : '#16211D';
    g.fill();
    g.strokeStyle = isAdv ? '#4A3626' : '#2C5748';
    g.lineWidth = 1.5; g.stroke();
    g.fillStyle = isAdv ? '#C98F63' : MINT2;""")

rep("""  g.fillStyle = 'rgba(245,242,235,.045)'; g.fill();
  g.strokeStyle = 'rgba(245,242,235,.12)'; g.lineWidth = 2; g.stroke();
  g.strokeStyle = 'rgba(245,242,235,.1)'; g.lineWidth = 1.5;""",
"""  g.fillStyle = PANEL; g.fill();
  g.strokeStyle = LINE; g.lineWidth = 2; g.stroke();
  g.strokeStyle = '#1F1F22'; g.lineWidth = 1.5;""")

rep("g.fillStyle = 'rgba(245,242,235,.92)'; g.font = cardFont(700, 33);",
    "g.fillStyle = 'rgba(242,242,240,.92)'; g.font = cardFont(700, 33);")

rep("""  roundRect(g, 80, 1116, fbW, 56, 28);
  g.fillStyle = 'rgba(16,185,129,.14)'; g.fill();
  g.strokeStyle = 'rgba(16,185,129,.45)'; g.lineWidth = 1.5; g.stroke();""",
"""  roundRect(g, 80, 1116, fbW, 56, 28);
  g.fillStyle = '#161F1B'; g.fill();
  g.strokeStyle = '#2C5748'; g.lineWidth = 1.5; g.stroke();""")

rep("g.strokeStyle = 'rgba(245,242,235,.12)'; g.lineWidth = 2;\n  g.beginPath(); g.moveTo(80, 1222); g.lineTo(W - 80, 1222); g.stroke();",
    "g.strokeStyle = LINE; g.lineWidth = 2;\n  g.beginPath(); g.moveTo(80, 1222); g.lineTo(W - 80, 1222); g.stroke();")

# ---------------- 버전 ----------------
rep("  version: 'v13',", "  version: 'v14',")

fail = 0
for old, new in REPL:
    n = src.count(old)
    if n != 1:
        print('!! %d회 일치: %r' % (n, old[:70]))
        fail += 1
        continue
    src = src.replace(old, new)

if fail:
    sys.exit('%d replacement(s) failed' % fail)
P.write_text(src)
print('ok · %d replacements applied' % len(REPL))
