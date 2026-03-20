import streamlit as st

st.set_page_config(
    page_title="TONEME · 퍼스널 컬러 뷰티",
    page_icon="🌼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');

:root {
    --bg:      #fbf7ea;
    --surf:    #fffdf7;
    --surf2:   #f7f1dd;
    --line:    #e0d098;
    --lines:   #c8b040;
    --text:    #1e1700;
    --sub:     #4a3d1a;
    --muted:   #6b5a30;
    --acc:     #7a5800;
}
html,body,[data-testid="stAppViewContainer"],[data-testid="stApp"]{
    background:var(--bg)!important;
    font-family:'Noto Sans KR',sans-serif;
    color:var(--text);
}
[data-testid="stSidebar"]{display:none;}
.block-container{max-width:1160px!important;padding:2rem 2.8rem 4rem!important;}

/* hero */
.hero-kicker{
    display:inline-flex;align-items:center;gap:.4rem;
    padding:.26rem .7rem;border:1.5px solid var(--lines);border-radius:999px;
    background:rgba(255,255,255,.6);color:var(--acc);
    font-size:.77rem;font-weight:800;letter-spacing:.02em;
}
.hero-title{
    font-size:2.8rem;line-height:1.06;letter-spacing:-.03em;
    font-weight:900;color:var(--text);margin:.8rem 0 .6rem;
}
.hero-title .acc{color:var(--acc);}
.hero-sub{font-size:.92rem;line-height:1.8;color:var(--sub);margin-bottom:1.6rem;}

/* tabs */
.stTabs [data-baseweb="tab-list"]{gap:.2rem;border-bottom:1.5px solid var(--line);}
.stTabs [data-baseweb="tab"]{
    padding:.78rem 1rem .72rem;border-radius:12px 12px 0 0;
    color:var(--sub);font-size:.88rem;font-weight:700;
}
.stTabs [aria-selected="true"]{
    color:var(--acc)!important;background:rgba(255,255,255,.65)!important;
    border:1.5px solid var(--line)!important;
    border-bottom:1.5px solid var(--bg)!important;font-weight:900!important;
}

/* section */
.sec-title{font-size:1.1rem;font-weight:900;color:var(--text);margin-bottom:.15rem;}
.sec-sub{font-size:.88rem;line-height:1.8;color:var(--sub);margin-bottom:1.1rem;}
.col-head{
    font-size:.85rem;font-weight:900;color:var(--text);
    padding-bottom:.6rem;margin-bottom:.7rem;
    border-bottom:1.5px solid var(--line);
}

/* selectbox */
[data-testid="stSelectbox"] label{display:none!important;}
[data-testid="stSelectbox"]>div>div{
    border-radius:11px!important;border-color:var(--line)!important;
    background:var(--surf)!important;color:var(--text)!important;
    font-size:.85rem!important;font-weight:600!important;
}

/* mini info — 선택 완료 표시 */
.mini{
    display:grid;grid-template-columns:16px 1fr;gap:.6rem;align-items:start;
    margin-top:.35rem;padding:.68rem .8rem;
    background:var(--surf);border:1.5px solid var(--lines);border-radius:10px;
}
.dot{
    width:16px;height:16px;border-radius:50%;
    border:1.5px solid rgba(0,0,0,.12);margin-top:.1rem;
}
.mini-body{min-width:0;}
.mini-name{font-size:.82rem;font-weight:800;color:var(--text);line-height:1.4;
           display:flex;flex-wrap:wrap;align-items:center;gap:.3rem;}
.mini-note{font-size:.74rem;color:var(--sub);line-height:1.6;margin-top:.22rem;}

/* tags — 모두 어두운 배경+밝은 글씨 */
.tag{
    display:inline-flex;align-items:center;justify-content:center;
    height:1.45rem;padding:0 .54rem;border-radius:999px;
    font-size:.68rem;font-weight:800;white-space:nowrap;vertical-align:middle;
}
.t-warm  {background:#5c3300;color:#ffe4ac;}
.t-cool  {background:#1a3570;color:#c8dcff;}
.t-spring{background:#6a3800;color:#ffd8a8;}
.t-summer{background:#1e3870;color:#c0ccff;}
.t-autumn{background:#573000;color:#ffd0a0;}
.t-winter{background:#152870;color:#b8c8ff;}
.t-cat   {background:#3a2d00;color:#ffe898;}
.t-new   {background:#0d4a28;color:#a8ffce;}
.t-disc  {background:#4a4030;color:#e8dcc0;}
.t-fit1  {background:var(--acc);color:#fff8d8;}
.t-fit2  {background:#3a3000;color:#f8e898;}

/* card */
.card{
    display:grid;grid-template-columns:16px 1fr auto;
    gap:.68rem;align-items:start;
    padding:.82rem .9rem;margin-bottom:.5rem;
    border:1px solid var(--line);border-radius:13px;background:var(--surf);
}
.card-body{min-width:0;}
.card-name{
    font-size:.83rem;font-weight:800;color:var(--text);
    line-height:1.4;display:flex;flex-wrap:wrap;align-items:center;gap:.32rem;
}
.card-shade{
    font-size:.76rem;color:var(--muted);margin-top:.16rem;line-height:1.5;
    display:flex;flex-wrap:wrap;align-items:center;gap:.28rem;
}
.card-note{font-size:.74rem;color:var(--sub);margin-top:.16rem;line-height:1.6;}

/* result */
.rbox{border-radius:20px;padding:1.4rem 1.5rem;margin-bottom:1rem;border:1.5px solid var(--line);}
.rbox-warm{background:linear-gradient(135deg,#fff7da,#f6e9b0);}
.rbox-cool{background:linear-gradient(135deg,#e8eeff,#d8e2ff);}
.rbox-title{font-size:1.85rem;font-weight:900;letter-spacing:-.02em;
            margin-bottom:.3rem;color:var(--text);}
.rbox-desc{font-size:.9rem;line-height:1.78;color:var(--sub);}

/* info band */
.iband{
    padding:.88rem 1.1rem;border-radius:14px;margin-bottom:1rem;
    border:1px solid var(--line);background:rgba(255,255,255,.6);
}
.iband b{color:var(--text);font-size:.94rem;}
.iband small{display:block;color:var(--sub);font-size:.82rem;line-height:1.7;margin-top:.22rem;}

/* button */
.stButton>button{
    background:var(--acc)!important;color:#fff8d8!important;
    border:none!important;border-radius:11px!important;
    padding:.62rem 1.8rem!important;font-size:.87rem!important;
    font-weight:800!important;width:100%!important;
}
.stButton>button:hover{filter:brightness(1.15)!important;}

.stRadio label,.stCheckbox label{
    color:var(--text)!important;font-weight:700!important;font-size:.84rem!important;
}
details summary{font-size:.85rem!important;font-weight:700!important;color:var(--text)!important;}
hr{border-color:var(--line)!important;margin:1rem 0!important;}
.stInfo,.stWarning,.stSuccess{border-radius:11px!important;font-size:.84rem!important;}
.footer{margin-top:2rem;text-align:center;color:var(--muted);font-size:.73rem;}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# DATA
# ══════════════════════════════════════════════
def it(tone, seasons, chroma, value, cat, hex_col, note, avail=True, new26=False):
    return dict(tone=tone, seasons=seasons, chroma=chroma, value=value,
                cat=cat, hex=hex_col, note=note, avail=avail, new26=new26)

DB = {
    # ── LIP ────────────────────────────────────
    "롬앤 더 쥬시 래스팅 틴트": {
        "01 포멜로 스킨":    it("warm",["spring","autumn"],1,4,"lip","#D9A788","밝은 누드 코랄"),
        "02 누카다미아":     it("warm",["autumn","spring"],1,3,"lip","#BB7E63","잔잔한 브릭 베이지 MLBB"),
        "03 베어 그레이프":  it("cool",["summer"],         1,4,"lip","#C58FA1","맑은 포도빛 핑크"),
        "04 피그 피그":      it("cool",["summer","winter"],2,3,"lip","#BD738E","뮤트 로즈"),
        "05 쥬쥬브":         it("warm",["autumn","spring"],2,3,"lip","#B96858","웜 레드 브릭"),
        "06 필링 앵두":      it("cool",["winter"],         3,2,"lip","#A43E4E","선명한 체리 레드"),
        "07 체리 밤":        it("warm",["autumn"],         3,2,"lip","#95453E","브릭 체리"),
        "08 핑크 펌킨":      it("warm",["spring"],         3,4,"lip","#E19386","산뜻한 핑크 코랄"),
        "09 멀드 피치":      it("warm",["spring","autumn"],2,4,"lip","#D6937C","복숭아 누드"),
        "10 베어 애프리콧":  it("warm",["spring"],         2,4,"lip","#D9A27F","밝은 살구 코랄"),
        "11 파파야 잼":      it("warm",["spring"],         3,4,"lip","#D87556","생기있는 파파야 코랄"),
        "12 애플 브라운":    it("warm",["autumn"],         2,2,"lip","#9C5A47","깊은 브라운 레드"),
        "13 잇 도토리":      it("warm",["autumn"],         1,2,"lip","#8C624F","도토리 브라운 MLBB"),
        "14 아몬드 로즈":    it("cool",["summer","winter"],1,3,"lip","#9E7281","차분한 로즈 브라운"),
        "15 베어 피그":      it("cool",["summer"],         1,4,"lip","#D29AA5","부드러운 피그 핑크"),
        "16 플럼 콕":        it("cool",["winter"],         3,2,"lip","#8F4A67","딥 플럼"),
        "17 다크 코코넛":    it("warm",["autumn"],         1,2,"lip","#7F5648","다크 브라운 누드"),
        "19 썸머 센트":      it("cool",["summer"],         2,4,"lip","#D28CA4","맑은 쿨 핑크"),
        "20 쥬쥬 피그":      it("cool",["summer"],         2,3,"lip","#C37B94","로지 피그 핑크"),
        "21 그레이프 밤":    it("cool",["winter"],         3,2,"lip","#995272","포도빛 베리"),
        "22 도토리 밤":      it("warm",["autumn"],         1,2,"lip","#835B49","딥 도토리 브라운"),
        "23 피치 피치 미":   it("warm",["spring"],         3,4,"lip","#EA9A87","맑은 피치 핑크"),
        "24 베어 쥬시 오":   it("warm",["spring"],         2,4,"lip","#DEA08A","누디한 살구빛"),
    },
    "에뛰드 픽싱 틴트": {
        "01 아날로그 로즈":  it("cool",["summer"],          2,3,"lip","#B97886","차분한 로즈 핑크"),
        "02 빈티지 레드":    it("cool",["winter"],          3,2,"lip","#9E434D","깊은 레드"),
        "03 멜로우 피치":    it("warm",["spring"],          2,4,"lip","#D4947C","복숭아 코랄"),
        "04 진저 밀크티":    it("warm",["autumn"],          1,3,"lip","#A67967","부드러운 밀크티 브라운"),
        "05 미드나잇 모브":  it("cool",["winter","summer"], 2,2,"lip","#8B667C","모브 로즈"),
        "06 소프트 월넛":    it("warm",["autumn"],          1,2,"lip","#86604F","차분한 월넛 브라운"),
        "07 크랜베리 플럼":  it("cool",["winter"],          3,2,"lip","#8F4258","쿨 크랜베리"),
        "08 더스티 베이지":  it("warm",["autumn","spring"], 1,4,"lip","#C3A08D","누디 베이지"),
        "10 스모키 체리":    it("cool",["winter"],          3,2,"lip","#8D4150","스모키 체리 레드"),
        "11 로즈 블렌딩":    it("cool",["summer"],          2,3,"lip","#B77B8E","뮤트 로즈"),
        "12 살몬 브릭":      it("warm",["autumn","spring"], 2,3,"lip","#B66C5E","살몬 브릭"),
        "13 멜란지 로즈":    it("cool",["summer"],          1,3,"lip","#A37A84","그레이시 로즈"),
        "14 로즈 라일락":    it("cool",["summer","winter"], 2,4,"lip","#B28CA7","라일락 로즈"),
        "15 우디 핑크":      it("warm",["spring","autumn"], 1,3,"lip","#B88782","따뜻한 우디 핑크"),
        "16 베이크드 피칸":  it("warm",["autumn"],          1,2,"lip","#89634E","딥 피칸 브라운"),
    },
    "페리페라 무드 글로이 틴트 2026": {
        "21 쿨링 핑크":       it("cool",["summer"],          2,4,"lip","#D78FAE","맑은 쿨 핑크",          new26=True),
        "22 핑크 프라이즈":   it("cool",["summer"],          2,4,"lip","#DA91A8","생기있는 핑크",          new26=True),
        "23 코랄 케미스트리": it("warm",["spring"],          3,4,"lip","#E88A73","맑은 코랄",              new26=True),
        "24 코랄 프라이드":   it("warm",["spring"],          3,4,"lip","#E37F62","선명한 코랄 오렌지",     new26=True),
        "25 핫 스트로베리":   it("cool",["winter"],          3,3,"lip","#C85271","스트로베리 핑크",        new26=True),
        "26 와이 소 베리":    it("cool",["winter"],          3,2,"lip","#A94D72","베리 플럼",              new26=True),
        "27 조킹 핑크":       it("cool",["summer"],          3,4,"lip","#D56A9A","선명한 쿨 핑크",         new26=True),
        "28 로즈 스탠다드":   it("cool",["summer","winter"], 2,3,"lip","#B77488","기본 로즈 MLBB",         new26=True),
        "29 허리 업 핑크":    it("cool",["summer"],          3,4,"lip","#DD7DA9","밝고 화사한 핑크",       new26=True),
    },
    # ── BLUSH ──────────────────────────────────
    "롬앤 베러 댄 치크": {
        "C01 피치칩":          it("warm",["spring"],          2,4,"blush","#E6AF93","맑은 피치 코랄"),
        "C02 블루베리칩":      it("cool",["summer"],          2,4,"blush","#C9A1B8","부드러운 쿨 모브"),
        "C03 피그칩":          it("cool",["summer","winter"], 2,3,"blush","#C98798","피그 로즈"),
        "C04 페어칩":          it("warm",["spring"],          1,4,"blush","#DFC2A1","라이트 베이지 피치"),
        "W01 오디 밀크":       it("cool",["winter"],          2,3,"blush","#A7748E","오디빛 플럼"),
        "W02 스트로베리 밀크": it("cool",["summer"],          1,4,"blush","#DDB5C4","딸기우유 핑크"),
        "W03 애프리콧 밀크":   it("warm",["spring"],          1,4,"blush","#EDC0A4","밀키 살구빛"),
        "N01 너티 누드":       it("warm",["autumn"],          1,3,"blush","#C2A28E","누디 베이지"),
        "N02 바인 누드":       it("cool",["summer"],          1,3,"blush","#B59A9C","그레이시 누드 모브"),
    },
    "페리페라 맑게 물든 선샤인 치크": {
        "025 반달입떡해":  it("warm",["spring"],          2,4,"blush","#E0A58A","살짝 코랄 기운의 피치"),
        "026 달달베리해":  it("cool",["winter"],          3,3,"blush","#B46E86","베리 핑크"),
        "029 모브낭낭해":  it("cool",["summer"],          2,4,"blush","#CEA1B8","차분한 모브 핑크"),
        "030 장미멀멀해":  it("cool",["summer"],          2,3,"blush","#B98892","말린 장미 로즈"),
        "031 라떼달달해":  it("warm",["autumn"],          1,3,"blush","#C7A48D","밀키한 라떼 베이지"),
        "달방아콩콩해":    it("cool",["summer"],          2,4,"blush","#D6A9B3","맑은 핑크 블러셔"),
    },
    # ── SHADOW ─────────────────────────────────
    "클리오 프로 아이 팔레트 에어": {
        "01 코랄 스튜디오":   it("warm",["spring"],          3,4,"shadow","#C98D66","화사한 코랄/피치 팔레트"),
        "02 로즈 커넥트":     it("cool",["summer","winter"], 2,3,"shadow","#B68593","로즈 모브 계열 팔레트"),
        "03 뮤트 라이브러리": it("cool",["summer"],          1,3,"shadow","#9B8A8F","뮤트 그레이시 로즈 브라운"),
    },
}

PC = {
    "봄 라이트 웜":   dict(tone="warm", season="spring", emoji="🌼",
        desc="밝고 맑은 웜톤이에요. 살구·피치·라이트 코랄처럼 투명감 있는 컬러가 가장 자연스럽게 살아나요.",
        best=["피치","살구","라이트 코랄","누디 베이지"], avoid=["강한 블루 핑크","버건디","차가운 그레이"]),
    "봄 비비드 웜":   dict(tone="warm", season="spring", emoji="🌺",
        desc="맑고 선명한 색을 받는 타입이에요. 생기 있는 코랄 레드, 쨍한 웜 핑크가 얼굴을 또렷하게 보여줘요.",
        best=["비비드 코랄","오렌지 레드","웜 핑크"], avoid=["회끼 모브","탁한 브라운"]),
    "가을 뮤트 웜":   dict(tone="warm", season="autumn", emoji="🍁",
        desc="채도가 낮고 부드러운 웜톤이에요. 브라운, 누드 베이지, 잔잔한 브릭 계열이 차분하게 어울려요.",
        best=["누드 베이지","웜 브라운","브릭","카멜"], avoid=["형광 코랄","차가운 라일락"]),
    "가을 딥 웜":     dict(tone="warm", season="autumn", emoji="🥮",
        desc="깊이감 있는 웜톤이에요. 도토리 브라운, 테라코타, 딥 브릭처럼 무게감 있는 색이 잘 맞아요.",
        best=["테라코타","도토리 브라운","딥 브릭","카카오 브라운"], avoid=["아이스 핑크","블루 레드"]),
    "여름 라이트 쿨": dict(tone="cool", season="summer", emoji="🫧",
        desc="부드럽고 밝은 쿨톤이에요. 우유빛 핑크, 라일락, 라이트 로즈가 맑게 어울려요.",
        best=["베이비 핑크","라일락","라이트 로즈"], avoid=["노란 코랄","짙은 브라운"]),
    "여름 뮤트 쿨":   dict(tone="cool", season="summer", emoji="🌫️",
        desc="회끼와 부드러움이 있는 쿨톤이에요. 뮤트 로즈, 모브, 그레이시 핑크가 세련되게 맞아요.",
        best=["모브","뮤트 로즈","그레이시 핑크"], avoid=["쨍한 오렌지","노란 브릭"]),
    "겨울 비비드 쿨": dict(tone="cool", season="winter", emoji="❄️",
        desc="선명하고 대비감이 강한 쿨톤이에요. 또렷한 베리 핑크, 체리 레드가 얼굴을 살려줘요.",
        best=["체리 레드","비비드 핑크","쿨 베리"], avoid=["누디 베이지","오렌지 코랄"]),
    "겨울 딥 쿨":     dict(tone="cool", season="winter", emoji="🌌",
        desc="깊고 선명한 쿨톤이에요. 플럼, 버건디, 딥 로즈처럼 밀도 있는 컬러가 특히 잘 어울려요.",
        best=["플럼","버건디","딥 로즈","블랙 체리"], avoid=["웜 브라운","살구 코랄"]),
}

PAIRING = {
    ("spring","blush"):  [("롬앤 베러 댄 치크","C01 피치칩"),("롬앤 베러 댄 치크","W03 애프리콧 밀크"),("페리페라 맑게 물든 선샤인 치크","025 반달입떡해")],
    ("spring","shadow"): [("클리오 프로 아이 팔레트 에어","01 코랄 스튜디오")],
    ("autumn","blush"):  [("롬앤 베러 댄 치크","N01 너티 누드"),("페리페라 맑게 물든 선샤인 치크","031 라떼달달해")],
    ("autumn","shadow"): [("클리오 프로 아이 팔레트 에어","03 뮤트 라이브러리")],
    ("summer","blush"):  [("롬앤 베러 댄 치크","W02 스트로베리 밀크"),("페리페라 맑게 물든 선샤인 치크","029 모브낭낭해"),("페리페라 맑게 물든 선샤인 치크","달방아콩콩해")],
    ("summer","shadow"): [("클리오 프로 아이 팔레트 에어","02 로즈 커넥트"),("클리오 프로 아이 팔레트 에어","03 뮤트 라이브러리")],
    ("winter","blush"):  [("롬앤 베러 댄 치크","W01 오디 밀크"),("페리페라 맑게 물든 선샤인 치크","026 달달베리해")],
    ("winter","shadow"): [("클리오 프로 아이 팔레트 에어","02 로즈 커넥트")],
}

CAT_KR = {"lip":"립","blush":"블러셔","shadow":"섀도우"}
SEA_KR = {"spring":"봄 웜","summer":"여름 쿨","autumn":"가을 웜","winter":"겨울 쿨"}


# ══════════════════════════════════════════════
# HTML 헬퍼
# ══════════════════════════════════════════════
def tone_tag(t):
    return f'<span class="tag t-{"warm" if t=="warm" else "cool"}">{"웜톤" if t=="warm" else "쿨톤"}</span>'

def sea_tag(s):
    return f'<span class="tag t-{s}">{SEA_KR.get(s,s)}</span>'

def cat_tag(c):
    return f'<span class="tag t-cat">{CAT_KR.get(c,c)}</span>'

def new_tag(flag):
    return '<span class="tag t-new">NEW 2026</span>' if flag else ""

def dot(hex_col):
    return f'<span class="dot" style="background:{hex_col};display:inline-block;flex-shrink:0;"></span>'

def card(pname, shade, d, fit=""):
    fit_html = ""
    if fit == "완벽 매칭":
        fit_html = '<span class="tag t-fit1">완벽 매칭</span>'
    elif fit:
        fit_html = '<span class="tag t-fit2">같은 톤</span>'
    return f"""<div class="card">
{dot(d['hex'])}
<div class="card-body">
  <div class="card-name">{pname} {new_tag(d.get('new26',False))}</div>
  <div class="card-shade">{shade} &nbsp;·&nbsp; {CAT_KR[d['cat']]} &nbsp; {tone_tag(d['tone'])} {''.join(sea_tag(s) for s in d['seasons'])}</div>
  <div class="card-note">{d['note']}</div>
</div>
<div>{fit_html}</div>
</div>"""

def mini(pname, shade, d):
    return f"""<div class="mini">
{dot(d['hex'])}
<div class="mini-body">
  <div class="mini-name">{pname} · {shade} {tone_tag(d['tone'])} {''.join(sea_tag(s) for s in d['seasons'])} {cat_tag(d['cat'])} {new_tag(d.get('new26',False))}</div>
  <div class="mini-note">{d['note']}</div>
</div>
</div>"""


# ══════════════════════════════════════════════
# 데이터 헬퍼
# ══════════════════════════════════════════════
def pnames(cat_filter):
    result = []
    for pn, shades in DB.items():
        for d in shades.values():
            if cat_filter is None or d["cat"] == cat_filter:
                result.append(pn)
                break
    return sorted(result)

def shades_of(pn):
    return list(DB[pn].keys())

def get_recs(tone, season, cat=None, only_new=False, limit=8):
    pri, sec = [], []
    for pn, shades in DB.items():
        for sh, d in shades.items():
            if not d["avail"]: continue
            if cat and d["cat"] != cat: continue
            if only_new and not d.get("new26"): continue
            row = (pn, sh, d)
            if d["tone"]==tone and season in d["seasons"]: pri.append(row)
            elif d["tone"]==tone: sec.append(row)
    return (pri+sec)[:limit]

def analyze(goods, bads, bests):
    ts=cs=vs=wt=0.0
    def acc(lst, w):
        nonlocal ts,cs,vs,wt
        for e in lst:
            if not e: continue
            pn,sh=e; d=DB[pn][sh]
            ts+=(1 if d["tone"]=="warm" else -1)*w
            cs+=d["chroma"]*w; vs+=d["value"]*w; wt+=abs(w)
    acc(goods,1.0); acc(bests,2.0); acc(bads,-1.4)
    if wt==0: return None
    ac,av=cs/wt,vs/wt
    if ts>=0:
        pc=("봄 비비드 웜" if ac>=2.3 else "봄 라이트 웜") if av>=3.6 \
        else("가을 딥 웜"  if ac>=1.8 else "가을 뮤트 웜")
    else:
        pc=("여름 라이트 쿨" if ac>=1.8 else "여름 뮤트 쿨") if av>=3.5 \
        else("겨울 비비드 쿨" if ac>=2.5 else "겨울 딥 쿨")
    return {"pc":pc,"tone":PC[pc]["tone"],"season":PC[pc]["season"]}


# ══════════════════════════════════════════════
# 제품 선택 위젯
# ══════════════════════════════════════════════
def picker(prefix):
    cat_map = {"전체":None,"립":"lip","블러셔":"blush","섀도우":"shadow"}
    c1,c2 = st.columns([1,2])
    with c1:
        cl = st.selectbox("카", list(cat_map.keys()), key=f"{prefix}_c", label_visibility="collapsed")
    with c2:
        pn = st.selectbox("제품", pnames(cat_map[cl]), index=None,
                          placeholder="제품명 선택", key=f"{prefix}_p", label_visibility="collapsed")
    if not pn: return None
    sh = st.selectbox("호수", shades_of(pn), index=None,
                      placeholder="호수(컬러) 선택", key=f"{prefix}_s", label_visibility="collapsed")
    if not sh: return None
    st.markdown(mini(pn, sh, DB[pn][sh]), unsafe_allow_html=True)
    return (pn, sh)


# ══════════════════════════════════════════════
# TAB 1 — 분석
# ══════════════════════════════════════════════
def tab_analysis():
    st.markdown('<div class="sec-title">퍼스널 컬러 분석</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">실제 제품명과 호수명으로 입력해요. 잘 맞았던 제품 1개만 있어도 분석 가능해요.</div>', unsafe_allow_html=True)

    with st.expander("입력 기준 보기"):
        st.markdown("""
- **잘 맞았던** : 혼자 봐도 피부가 좋아 보였던 제품
- **안 맞았던** : 얼굴이 칙칙하거나 뜬다고 느꼈던 제품
- **반응 좋았던** : 주변 반응이 특히 좋았던 제품
        """)

    c1,c2,c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown('<div class="col-head">👍 잘 맞았던 제품 &nbsp;<small style="font-weight:400;color:#6b5a30">필수 1개↑</small></div>', unsafe_allow_html=True)
        g1=picker("g1"); st.divider(); g2=picker("g2"); st.divider(); g3=picker("g3")
    with c2:
        st.markdown('<div class="col-head">👎 안 맞았던 제품 &nbsp;<small style="font-weight:400;color:#6b5a30">선택</small></div>', unsafe_allow_html=True)
        b1=picker("b1"); st.divider(); b2=picker("b2"); st.divider(); b3=picker("b3")
    with c3:
        st.markdown('<div class="col-head">✨ 반응 좋았던 제품 &nbsp;<small style="font-weight:400;color:#6b5a30">선택</small></div>', unsafe_allow_html=True)
        t1=picker("t1"); st.divider(); t2=picker("t2"); st.divider(); t3=picker("t3")

    st.markdown("<div style='height:.4rem'></div>", unsafe_allow_html=True)
    _,bc,_ = st.columns([1.4,1.4,1.4])
    with bc:
        clicked = st.button("🌼 퍼스널 컬러 분석하기", use_container_width=True)

    if clicked:
        goods=[x for x in [g1,g2,g3] if x]
        bads =[x for x in [b1,b2,b3] if x]
        bests=[x for x in [t1,t2,t3] if x]
        if not goods:
            st.warning("잘 맞았던 제품을 최소 1개 선택해 주세요.")
        else:
            st.session_state["result"] = analyze(goods, bads, bests)

    if st.session_state.get("result"):
        render_result(st.session_state["result"])

def render_result(res):
    pc=res["pc"]; info=PC[pc]; tone=res["tone"]
    cls="rbox-warm" if tone=="warm" else "rbox-cool"
    st.divider()
    st.markdown(f'<div class="rbox {cls}"><div class="rbox-title">{info["emoji"]} {pc}</div><div class="rbox-desc">{info["desc"]}</div></div>', unsafe_allow_html=True)

    r1,r2=st.columns(2)
    with r1:
        st.markdown("**잘 어울리는 컬러**")
        for x in info["best"]:  st.markdown(f"- {x}")
    with r2:
        st.markdown("**피하면 좋은 컬러**")
        for x in info["avoid"]: st.markdown(f"- {x}")

    st.markdown("### 맞춤 추천 제품")
    f1,f2=st.columns([2.5,1])
    with f1:
        cl=st.radio("카테고리",["전체","립","블러셔","섀도우"],horizontal=True,
                    key="rc",label_visibility="collapsed")
    with f2:
        no=st.checkbox("2026 NEW만",key="rn")
    cmap={"전체":None,"립":"lip","블러셔":"blush","섀도우":"shadow"}
    recs=get_recs(tone,res["season"],cat=cmap[cl],only_new=no,limit=8)
    if not recs: st.info("조건에 맞는 제품이 없어요."); return
    cols=st.columns(2)
    for i,(pn,sh,d) in enumerate(recs):
        fit="완벽 매칭" if res["season"] in d["seasons"] else "같은 톤"
        with cols[i%2]: st.markdown(card(pn,sh,d,fit), unsafe_allow_html=True)


# ══════════════════════════════════════════════
# TAB 2 — 연계 추천
# ══════════════════════════════════════════════
def tab_pairing():
    st.markdown('<div class="sec-title">연계 추천</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">립에서 블러셔·섀도우까지 자연스럽게 이어지는 조합을 보여줘요.</div>', unsafe_allow_html=True)

    pc_list=list(PC.keys())
    default=st.session_state.get("result",{}).get("pc",pc_list[0]) if st.session_state.get("result") else pc_list[0]
    sel=st.selectbox("퍼스널 컬러",pc_list,index=pc_list.index(default),key="pair_sel")
    info=PC[sel]

    st.markdown(f'<div class="iband"><b>{info["emoji"]} {sel}</b><small>{info["desc"]}</small></div>', unsafe_allow_html=True)

    st.markdown("### 립 추천")
    recs=get_recs(info["tone"],info["season"],cat="lip",limit=6)
    cols=st.columns(2)
    for i,(pn,sh,d) in enumerate(recs):
        with cols[i%2]: st.markdown(card(pn,sh,d), unsafe_allow_html=True)

    st.markdown("### 블러셔 연결")
    bl=[(pn,sh,DB[pn][sh]) for pn,sh in PAIRING.get((info["season"],"blush"),[]) if pn in DB and sh in DB.get(pn,{})]
    if bl:
        cols=st.columns(2)
        for i,(pn,sh,d) in enumerate(bl):
            with cols[i%2]: st.markdown(card(pn,sh,d), unsafe_allow_html=True)
    else:
        st.info("연결 블러셔 정보가 없어요.")

    st.markdown("### 섀도우 연결")
    sd=[(pn,sh,DB[pn][sh]) for pn,sh in PAIRING.get((info["season"],"shadow"),[]) if pn in DB and sh in DB.get(pn,{})]
    if sd:
        cols=st.columns(2)
        for i,(pn,sh,d) in enumerate(sd):
            with cols[i%2]: st.markdown(card(pn,sh,d), unsafe_allow_html=True)
    else:
        st.info("연결 섀도우 정보가 없어요.")


# ══════════════════════════════════════════════
# TAB 3 — 제품 탐색
# ══════════════════════════════════════════════
def tab_browse():
    st.markdown('<div class="sec-title">제품 탐색</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">실제 제품명·호수명으로 정리한 목록이에요. 2026 NEW만 따로 볼 수도 있어요.</div>', unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)
    with c1: cl=st.selectbox("카테고리",["전체","립","블러셔","섀도우"],key="bc")
    with c2: tl=st.selectbox("톤",["전체","웜톤","쿨톤"],key="bt")
    with c3: no=st.checkbox("2026 NEW만",key="bn")
    cmap={"전체":None,"립":"lip","블러셔":"blush","섀도우":"shadow"}
    tmap={"전체":None,"웜톤":"warm","쿨톤":"cool"}

    rows=[]
    for pn,shades in DB.items():
        for sh,d in shades.items():
            if cmap[cl] and d["cat"]!=cmap[cl]: continue
            if tmap[tl] and d["tone"]!=tmap[tl]: continue
            if no and not d.get("new26"): continue
            rows.append((pn,sh,d))

    st.caption(f"총 {len(rows)}개")
    cols=st.columns(2)
    for i,(pn,sh,d) in enumerate(rows):
        with cols[i%2]: st.markdown(card(pn,sh,d), unsafe_allow_html=True)


# ══════════════════════════════════════════════
# TAB 4 — 가이드
# ══════════════════════════════════════════════
def tab_guide():
    st.markdown('<div class="sec-title">컬러 가이드</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">8개 세부톤의 분위기를 빠르게 확인할 수 있어요.</div>', unsafe_allow_html=True)

    for name,info in PC.items():
        with st.expander(f"{info['emoji']} {name}"):
            c1,c2=st.columns([1.3,1])
            with c1:
                st.markdown(f"**설명**\n\n{info['desc']}")
            with c2:
                st.markdown("**잘 어울림**")
                for x in info["best"]: st.markdown(f"- {x}")
                st.markdown("**주의 컬러**")
                for x in info["avoid"]: st.markdown(f"- {x}")


# ══════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════
def main():
    if "result" not in st.session_state:
        st.session_state["result"] = None

    st.markdown("""
<div class="hero-wrap" style="padding:1rem 0 1.5rem">
    <div class="hero-kicker">🌼 TONEME · curated for Korea</div>
    <div class="hero-title">실사용 기준으로 고르는<br><span class="acc">퍼스널 컬러 추천</span></div>
    <div class="hero-sub">제품명을 먼저 고르고, 실제 호수를 선택하면 바로 확인할 수 있어요.</div>
</div>""", unsafe_allow_html=True)

    t1,t2,t3,t4=st.tabs(["🎨 퍼스널 컬러 분석","✨ 연계 추천","🗂️ 제품 탐색","📖 컬러 가이드"])
    with t1: tab_analysis()
    with t2: tab_pairing()
    with t3: tab_browse()
    with t4: tab_guide()

    st.markdown('<div class="footer">TONEME · 실제 제품명/호수 기준 · NEW 표시는 2026 확인 항목만</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
