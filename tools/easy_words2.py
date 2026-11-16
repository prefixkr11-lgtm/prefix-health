#!/usr/bin/env python3
"""v14-2 (2/2): 화면 라벨·리포트 코멘트·결과 카드 문구를 쉬운 한국어로 정리."""
import pathlib, sys

P = pathlib.Path('/workspace/work/prefix-health-pages/index.html')
src = P.read_text()
R = []
def rep(old, new, n=1):
    R.append((old, new, n))

# ---------- 소개 문단 ----------
rep("    <p>동영상을 올리거나 카메라를 켜면 관절 33개를 실시간으로 추적해서 무릎·팔꿈치 각도, 몸통 일직선, 반복 횟수까지 세어 줍니다. 영상은 브라우저 밖으로 나가지 않아요.</p>",
    "    <p>동영상을 올리거나 카메라를 켜면 몸의 관절 33곳을 실시간으로 따라가며 무릎·팔꿈치가 얼마나 굽었는지, 몸이 곧은지, 몇 번 했는지 세어 줘요. 영상은 이 기기 밖으로 나가지 않아요.</p>")

# ---------- 운동 선택 보조 설명 ----------
rep('<span class="fc">무릎 깊이 · 상체 숙임</span>', '<span class="fc">무릎 깊이 · 상체 숙임</span>')
rep('<span class="fc">팔꿈치 각도 · 몸통 일직선</span>', '<span class="fc">팔꿈치 각도 · 몸이 곧은지</span>')
rep('<span class="fc">상체 기울기 · 팔 스윙 · 케이던스</span>', '<span class="fc">상체 기울기 · 팔 스윙 · 발걸음 속도</span>')

# ---------- HUD / 세션 카드 ----------
rep('<div class="chip" id="hudFrames">33 JOINTS</div>', '<div class="chip" id="hudFrames">관절 33곳</div>')
rep('<span class="k" id="hudCountKey">REPS</span>', '<span class="k" id="hudCountKey">횟수</span>')
rep('<span id="sessModel">모델 대기 중</span><span id="sessFrames">0 frames</span>',
    '<span id="sessModel">분석 준비 중</span><span id="sessFrames">0컷 분석</span>')
rep("        <h3>FEEDBACK LOG</h3>", "        <h3>실시간 코칭</h3>")
rep("        <h3>SESSION</h3>", "        <h3>이번 운동</h3>")
rep("      <span class=\"tag\">SESSION REPORT</span>", "      <span class=\"tag\">운동 리포트</span>")
rep("    <h4>주요 교정 포인트 · 타임라인</h4>", "    <h4>자주 나온 고칠 점 · 시간 순</h4>")
rep('<div class="tagline">MY RECORDS</div>\n        <h2>내 운동 기록</h2>',
    '<div class="tagline">내 운동 기록</div>\n        <h2>운동 기록 한눈에 보기</h2>')

# ---------- Pro 잠금 카드 ----------
rep("        <span class=\"plTitle\">Pro 심층 관절 리포트</span>\n        <span class=\"plSub\">관절별 각도 편차 · 좌우 밸런스 · 4주 점수 추이</span>",
    "        <span class=\"plTitle\">Pro 관절별 자세 리포트</span>\n        <span class=\"plSub\">관절마다 얼마나 흔들렸는지 · 좌우 균형 · 4주 점수 변화</span>")

# ---------- Pro 모달 ----------
rep("    <p class=\"sheetLead\">자세 점수 다음에 오는 <b>관절 단위 심층 리포트</b>. 무릎·팔꿈치 각도 편차와 좌우 밸런스까지 숫자로 보여드려요.</p>",
    "    <p class=\"sheetLead\">점수 하나로는 알 수 없는 걸 <b>더 자세히</b> 봐요. 무릎·팔꿈치가 얼마나 흔들렸는지, 좌우가 얼마나 다른지 숫자로 보여드려요.</p>")
rep("      <li><span class=\"bi\" aria-hidden=\"true\">🔬</span><span><b>관절별 심층 분석</b> — 무릎·팔꿈치 각도 편차, 좌우 밸런스, 반복별 점수 분포</span></li>\n      <li><span class=\"bi\" aria-hidden=\"true\">📈</span><span><b>4주 추이 리포트</b> — 주간 점수 변화와 부상 위험 구간 알림</span></li>\n      <li><span class=\"bi\" aria-hidden=\"true\">🎯</span><span><b>맞춤 교정 루틴</b> — 내 교정 포인트만 모은 5분 훈련</span></li>\n      <li><span class=\"bi\" aria-hidden=\"true\">📤</span><span><b>카드·기록 무제한</b> — 결과 카드 고해상도 저장과 기록 백업</span></li>",
    "      <li><span class=\"bi\" aria-hidden=\"true\">🔬</span><span><b>관절별 자세 분석</b> — 무릎·팔꿈치가 얼마나 흔들렸는지, 좌우 균형, 몇 번째 반복에서 점수가 떨어졌는지</span></li>\n      <li><span class=\"bi\" aria-hidden=\"true\">📈</span><span><b>4주 변화 리포트</b> — 주마다 점수가 어떻게 달라지는지, 다칠 수 있는 구간 알림</span></li>\n      <li><span class=\"bi\" aria-hidden=\"true\">🎯</span><span><b>나만의 5분 루틴</b> — 내가 자주 틀리는 동작만 모아서 알려줘요</span></li>\n      <li><span class=\"bi\" aria-hidden=\"true\">📤</span><span><b>카드·기록 무제한</b> — 결과 카드를 높은 화질로 저장하고 기록도 백업</span></li>")
rep("      <button class=\"btn primary\" id=\"proCta\" type=\"button\">출시 알림 · 결제 테스트</button>",
    "      <button class=\"btn primary\" id=\"proCta\" type=\"button\">출시되면 알려 주세요</button>")
rep("    <div class=\"proCount\">이 기기 관심 카운트 <b id=\"proCount\">0</b>회 · 결제는 아직 연동되지 않았어요</div>",
    "    <div class=\"proCount\">이 기기에서 관심 표시 <b id=\"proCount\">0</b>번 · 결제는 아직 안 돼요</div>")
rep("    <p class=\"proNote\">분석·기록·결과 카드 저장은 Pro와 관계없이 지금처럼 모두 무료로 쓸 수 있어요. Pro는 심층 리포트만 담당합니다.</p>",
    "    <p class=\"proNote\">분석·기록·결과 카드 저장은 지금처럼 모두 무료예요. Pro는 더 자세한 리포트만 맡아요.</p>")
rep("  toast('결제 연동 준비 중입니다! 관심 카운트 +1');",
    "  toast('결제는 아직 준비 중이에요. 관심 있다고 표시해 뒀어요');")

# ---------- 푸터 ----------
rep("""    Prehealth · 자세 분석 프로토타입 (프로토타입 0.1) — 관절 인식은 MediaPipe Pose Landmarker, 모든 처리는 이 기기의 브라우저 안에서만 이루어집니다. 업로드한 영상은 서버로 전송되지 않아요.<br>
    각도 판정은 3D 월드 랜드마크(실측 좌표) 기준이라 카메라가 비스듬해도 오차를 줄였습니다. 가려진 관절은 판정에서 자동으로 빠집니다. 통증이 있는 동작은 무리하지 마세요.""",
"""    Prehealth · 자세 분석 프로토타입 (0.1) — 자세 인식은 MediaPipe Pose Landmarker를 쓰고, 모든 계산은 이 기기 브라우저 안에서만 해요. 올린 영상은 서버로 보내지 않아요.<br>
    각도는 실제 3D 좌표로 계산해서 카메라가 비스듬해도 정확해요. 가려진 관절은 판정에서 자동으로 빼요. 통증이 있는 동작은 무리하지 마세요.""")

# ---------- 에러 안내 ----------
rep("      '<b>분석 엔진을 불러오지 못했어요.</b><br>인터넷 연결을 확인해 주세요. 이 파일은 처음 열 때 MediaPipe(CDN)를 내려받기 때문에, 오프라인이거나 사내망에서 CDN이 막혀 있으면 동작하지 않아요.',",
    "      '<b>분석 엔진을 불러오지 못했어요.</b><br>인터넷 연결을 확인해 주세요. 처음 열 때 분석 프로그램을 내려받기 때문에, 인터넷이 끊겼거나 회사·학교 네트워크에서 막혀 있으면 동작하지 않아요.',")
rep("    showNotice('bad', '<b>분석 엔진 파일(.wasm)을 내려받지 못했어요.</b><br>잠시 후 다시 시도해 주세요.',",
    "    showNotice('bad', '<b>분석에 필요한 파일을 내려받지 못했어요.</b><br>잠시 후 다시 시도해 주세요.',")
rep("  showNotice('bad', '<b>자세 인식 모델을 불러오지 못했어요.</b><br>' + (lastErr ? String(lastErr.message || lastErr) : '') + '<br>네트워크 상태를 확인한 뒤 다시 시도해 주세요.',",
    "  showNotice('bad', '<b>자세를 알아보는 프로그램을 불러오지 못했어요.</b><br>' + (lastErr ? String(lastErr.message || lastErr) : '') + '<br>인터넷 연결을 확인한 뒤 다시 시도해 주세요.',")
rep("      showNotice('warn', '프레임 분석 중 문제가 생겼어요. 잠시 후 다시 시도해 주세요.');",
    "      showNotice('warn', '분석 중에 문제가 생겼어요. 잠시 후 다시 시도해 주세요.');")

# ---------- 세션 표시 ----------
rep("  setText(els.sessFrames, '0 frames');", "  setText(els.sessFrames, '0컷 분석');")
rep("sum.frames + ' frames'", "sum.frames + '컷 분석'")

# ---------- 리포트 ----------
rep("    + (isRun && sum.cadence ? ' · 케이던스 ' + sum.cadence + ' spm' : '') + (sum.world3d ? ' · 3D' : ''));",
    "    + (isRun && sum.cadence ? ' · 분당 ' + sum.cadence + '걸음' : '') + (sum.world3d ? ' · 3D' : ''));")
rep("    c.textContent = '교정 포인트 없음';", "    c.textContent = '고칠 점 없음';")

# ---------- report 코멘트 (commentFor) ----------
rep("""  if (kind === 'running'){
    if (none || !sum.reps) return adv
      ? '스텝을 충분히 잡지 못했습니다. 측면 전신(머리~발끝) 프레임으로 다시 촬영하세요.'
      : '스텝을 충분히 잡지 못했어요. 옆에서 머리부터 발끝까지 한 화면에 들어오게 다시 찍어 볼까요?';
    if (score >= 88) return adv
      ? '체간·주관절 각도 기준 충족. 케이던스를 5~10spm 단위로 올려 볼 차례입니다.'
      : '상체 각도와 팔 스윙이 안정적이에요. 이 리듬 그대로 케이던스를 조금씩 올려 볼까요?';
    if (score >= 75) return adv
      ? '상위 이슈 1~2개만 제거하면 지표가 정리됩니다. 발생 빈도 순으로 처리하세요.'
      : '전반적으로 좋아요. 아래 교정 포인트 한두 개만 잡으면 훨씬 가벼워져요.';
    if (score >= 60) return adv
      ? '체간 전경과 주관절 각도가 권장 범위를 벗어났습니다. 이 두 지표부터 고정하세요.'
      : '기본은 잡혔어요. 상체 기울기와 팔꿈치 각도를 조금만 더 신경 써 볼까요?';
    return adv
      ? '전 지표 재설정 필요 · 속도 하향, 체간 4~16°, 주관절 90°로 스트라이드를 재구성하세요.'
      : '지금은 자세를 먼저 만드는 게 좋아요. 속도를 줄이고 상체는 살짝 앞으로, 팔은 90°로 접어 보세요.';
  }
  if (kind === 'plank'){
    if (none) return adv
      ? '유효 유지 시간이 없습니다. 견–골반–발목 168~180°로 프레임을 다시 잡으세요.'
      : '자세를 잡지 못했어요. 옆에서 어깨·엉덩이·발목이 한 화면에 들어오게 다시 시도해 볼까요?';
    if (score >= 88) return adv
      ? '체간 정렬 유지 시간 양호 · 세트 시간을 10초 단위로 증량하세요.'
      : '일직선이 아주 잘 유지됐어요. 시간을 조금씩 늘려 볼 차례예요.';
    if (score >= 72) return adv
      ? '이탈 구간만 국소 교정하면 됩니다. 복압 유지 구간을 확인하세요.'
      : '전체적으로 안정적이에요. 무너졌던 구간만 배에 힘을 더 주면 되겠어요.';
    if (score >= 55) return adv
      ? '유지 시간보다 체간 정렬이 우선입니다. 니플랭크로 정렬부터 확보하세요.'
      : '유지 시간보다 자세가 먼저예요. 무릎을 꿇은 플랭크로 일직선을 잡아 보세요.';
    return adv
      ? '체간 라인 붕괴 빈도가 높습니다. 시간을 줄이고 정렬을 먼저 고정하세요.'
      : '일직선이 자주 무너졌어요. 시간을 줄이고 자세를 먼저 잡는 걸 추천해요.';
  }
  if (none) return adv
    ? '유효 Rep 없음 · 가동범위와 프레임을 재설정한 뒤 다시 측정하세요.'
    : '반복이 감지되지 않았어요. 전신이 화면에 다 들어오는지, 자세가 옆에서 잘 보이는지 확인한 뒤 다시 해 볼까요?';
  if (sum.reps === 0) return adv
    ? '유효 Rep 0 · 동작 범위를 기준 이상으로 키우세요.'
    : '반복이 없어 점수를 낼 수 없어요. 동작을 한 번 더 크게 해 볼까요?';
  if (score >= 90) return adv
    ? '각도·정렬 기준 충족. 이 가동범위와 템포를 유지하세요.'
    : '자세가 아주 안정적이에요. 이 리듬과 깊이 그대로 유지해 볼까요?';
  if (score >= 75) return adv
    ? '감점 항목 1~2개 · 발생 빈도가 높은 지표부터 제거하세요.'
    : '전반적으로 좋아요. 아래 교정 포인트 한두 개만 잡으면 훨씬 깔끔해져요.';
  if (score >= 60) return adv
    ? '가동범위와 체간 정렬이 기준 미달입니다. 두 지표를 우선 교정하세요.'
    : '기본은 잡혔어요. 깊이와 몸통 정렬을 조금만 더 신경 써 볼까요?';
  return adv
    ? '전체 재설정 권장 · 템포를 낮추고 가동범위부터 확보하세요.'
    : '지금은 자세를 먼저 만드는 게 좋아요. 속도를 줄이고 가동범위부터 확보해 볼까요?';""",
"""  if (kind === 'running'){
    if (none || !sum.reps) return adv
      ? '발걸음을 충분히 잡지 못했어요. 옆에서 머리부터 발끝까지 한 화면에 담아 다시 찍어 주세요.'
      : '발걸음을 충분히 잡지 못했어요. 옆에서 머리부터 발끝까지 한 화면에 들어오게 다시 찍어 볼까요?';
    if (score >= 88) return adv
      ? '상체와 팔 각도 모두 좋아요. 이제 발걸음 속도를 분당 5~10걸음씩 올려 보세요.'
      : '상체와 팔이 안정적이에요. 이 리듬 그대로 발걸음만 조금씩 빠르게 해 볼까요?';
    if (score >= 75) return adv
      ? '고칠 점이 1~2개예요. 자주 나온 것부터 하나씩 고치면 점수가 확 올라가요.'
      : '전반적으로 좋아요. 아래 고칠 점 한두 개만 잡으면 훨씬 가벼워져요.';
    if (score >= 60) return adv
      ? '상체 기울기와 팔 각도가 기준을 벗어났어요. 이 두 가지부터 맞춰 보세요.'
      : '기본은 잡혔어요. 상체 기울기와 팔꿈치 각도를 조금만 더 신경 써 볼까요?';
    return adv
      ? '처음부터 다시 잡는 게 좋아요. 속도를 줄이고 상체는 살짝 앞으로, 팔은 90도로 접어 보세요.'
      : '지금은 자세를 먼저 만드는 게 좋아요. 속도를 줄이고 상체는 살짝 앞으로, 팔은 90도로 접어 보세요.';
  }
  if (kind === 'plank'){
    if (none) return adv
      ? '자세가 잡힌 시간이 없어요. 어깨·골반·발목을 한 줄로 만들고 다시 해 주세요.'
      : '자세를 잡지 못했어요. 옆에서 어깨·엉덩이·발목이 한 화면에 들어오게 다시 해 볼까요?';
    if (score >= 88) return adv
      ? '일직선을 잘 지켰어요. 세트 시간을 10초씩 늘려 보세요.'
      : '일직선이 아주 잘 유지됐어요. 시간을 조금씩 늘려 볼 차례예요.';
    if (score >= 72) return adv
      ? '무너진 구간만 잡으면 돼요. 배에 힘을 놓친 순간을 확인해 보세요.'
      : '전체적으로 안정적이에요. 무너졌던 구간만 배에 힘을 더 주면 되겠어요.';
    if (score >= 55) return adv
      ? '시간보다 자세가 먼저예요. 무릎을 꿇은 플랭크로 일직선부터 잡아 보세요.'
      : '유지 시간보다 자세가 먼저예요. 무릎을 꿇은 플랭크로 일직선을 잡아 보세요.';
    return adv
      ? '일직선이 자주 무너져요. 시간을 줄이고 자세부터 다시 잡아 보세요.'
      : '일직선이 자주 무너졌어요. 시간을 줄이고 자세를 먼저 잡는 걸 추천해요.';
  }
  if (none) return adv
    ? '동작이 잡히지 않았어요. 머리부터 발끝까지 다 보이게 하고 다시 해 주세요.'
    : '반복이 세어지지 않았어요. 머리부터 발끝까지 다 보이는지, 옆에서 자세가 잘 보이는지 확인한 뒤 다시 해 볼까요?';
  if (sum.reps === 0) return adv
    ? '센 반복이 없어요. 동작을 기준보다 크게 해 주세요.'
    : '반복이 없어 점수를 낼 수 없어요. 동작을 한 번 더 크게 해 볼까요?';
  if (score >= 90) return adv
    ? '각도도 자세도 좋아요. 이 깊이와 속도를 그대로 유지하세요.'
    : '자세가 아주 안정적이에요. 이 리듬과 깊이 그대로 유지해 볼까요?';
  if (score >= 75) return adv
    ? '고칠 점이 1~2개예요. 자주 나온 것부터 하나씩 고쳐 보세요.'
    : '전반적으로 좋아요. 아래 고칠 점 한두 개만 잡으면 훨씬 깔끔해져요.';
  if (score >= 60) return adv
    ? '깊이와 몸통 자세가 기준에 조금 못 미쳐요. 이 두 가지부터 맞춰 보세요.'
    : '기본은 잡혔어요. 깊이와 몸통 자세를 조금만 더 신경 써 볼까요?';
  return adv
    ? '처음부터 다시 잡는 게 좋아요. 속도를 줄이고 깊이부터 확보하세요.'
    : '지금은 자세를 먼저 만드는 게 좋아요. 속도를 줄이고 조금 더 깊이 내려가 보세요.';""")

# ---------- 결과 카드 문구 ----------
rep("  if (typeof s !== 'number') return '이번엔 점수를 낼 만큼 동작이 잡히지 않았어요. 전신이 다 보이게 다시 찍어 볼까요?';",
    "  if (typeof s !== 'number') return '이번엔 점수를 낼 만큼 동작이 잡히지 않았어요. 머리부터 발끝까지 다 보이게 다시 찍어 볼까요?';")
rep("  if (s >= 75) return '전반적으로 좋아요. 교정 포인트 한두 개만 잡으면 훨씬 깔끔해져요.';",
    "  if (s >= 75) return '전반적으로 좋아요. 고칠 점 한두 개만 잡으면 훨씬 깔끔해져요.';")
rep("  if (s >= 60) return '기본은 잡혔어요. 가동범위를 조금만 더 확보해 볼까요?';",
    "  if (s >= 60) return '기본은 잡혔어요. 조금만 더 깊이 움직여 볼까요?';")
rep("  return '지금은 속도보다 자세예요. 가동범위부터 천천히 만들어 봐요.';",
    "  return '지금은 속도보다 자세예요. 깊이부터 천천히 만들어 봐요.';")
rep("  const fb = '교정 포인트 · ' + (rec.topFeedback || '기록 없음');",
    "  const fb = '고칠 점 · ' + (rec.topFeedback || '기록 없음');")
rep("  drawTracked(g, 'SESSION RESULT', 82, 348, 7);", "  drawTracked(g, '운동 결과', 82, 348, 7);")

fail = 0
for old, new, n in R:
    c = src.count(old)
    if c != n:
        print('!! %d회 (기대 %d): %r' % (c, n, old[:80]))
        fail += 1
        continue
    src = src.replace(old, new)
if fail:
    sys.exit('%d replacement(s) failed' % fail)
P.write_text(src)
print('ok · %d replacements applied' % len(R))
