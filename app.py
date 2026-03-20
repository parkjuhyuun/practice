import streamlit as st

# =========================================================
# PAGE
# =========================================================
st.set_page_config(
    page_title="TONEME · 퍼스널 컬러 뷰티",
    page_icon="🌼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# STYLE
# =========================================================
st.markdown("""
<style>
:root{
    --bg:#FBF7EC;
    --surface:#FFFDF8;
    --surface-2:#F6F0DF;
    --line:#E7DDBD;
    --line-strong:#CDB671;
    --text:#231B10;
    --sub:#6A5A42;
    --muted:#8B7C66;
    --accent:#8E6B18;
    --accent-soft:#F3E7B8;
    --warm-bg:#FFF1E2;
    --warm-text:#8B4C16;
    --cool-bg:#EAF0FF;
    --cool-text:#405EA5;
    --new-bg:#1F6F54;
    --new-text:#F4FFF9;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"]{
    background:var(--bg) !important;
    color:var(--text);
    font-family: "Pretendard","Noto Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif;
}

[data-testid="stSidebar"]{
    display:none;
}

.block-container{
    max-width:1160px !important;
    padding:2.2rem 2.4rem 4rem !important;
}

/* hero */
.hero-wrap{
    margin-bottom:1.2rem;
}
.hero-kicker{
    display:inline-block;
    padding:0.35rem 0.8rem;
    border:1px solid var(--line-strong);
    border-radius:999px;
    background:rgba(255,255,255,0.65);
    color:var(--accent);
    font-size:0.78rem;
    font-weight:700;
}
.hero-title{
    margin-top:0.9rem;
    font-size:3rem;
    font-weight:800;
    line-height:1.08;
    letter-spacing:-0.03em;
    color:var(--text);
}
.hero-title .accent{
    color:var(--accent);
}
.hero-sub{
    margin-top:0.75rem;
    max-width:820px;
    font-size:0.96rem;
    line-height:1.8;
    color:var(--sub);
}

/* tabs */
.stTabs [data-baseweb="tab-list"]{
    gap:0.3rem;
    border-bottom:1px solid var(--line);
}
.stTabs [data-baseweb="tab"]{
    padding:0.85rem 1rem 0.8rem;
    border-radius:14px 14px 0 0;
    color:var(--sub);
    font-size:0.92rem;
    font-weight:800;
}
.stTabs [aria-selected="true"]{
    color:var(--text) !important;
    background:rgba(255,255,255,0.62) !important;
    border:1px solid var(--line) !important;
    border-bottom:1px solid var(--bg) !important;
}

/* headings */
.section-title{
    font-size:1.14rem;
    font-weight:800;
    color:var(--text);
    margin-bottom:0.2rem;
}
.section-sub{
    font-size:0.92rem;
    line-height:1.75;
    color:var(--sub);
    margin-bottom:1rem;
}

/* panels */
.panel{
    background:rgba(255,255,255,0.62);
    border:1px solid var(--line);
    border-radius:18px;
    padding:1rem;
    min-height:100%;
}
.panel-head{
    display:flex;
    align-items:center;
    gap:0.55rem;
    padding-bottom:0.75rem;
    margin-bottom:0.7rem;
    border-bottom:1px solid var(--line);
    font-size:0.92rem;
    font-weight:800;
    color:var(--text);
}
.panel-icon{
    width:1.9rem;
    height:1.9rem;
    border-radius:12px;
    display:flex;
    align-items:center;
    justify-content:center;
    background:var(--surface-2);
    font-size:1rem;
}
.panel-sub{
    color:var(--muted);
    font-size:0.78rem;
    margin-bottom:0.9rem;
    line-height:1.6;
}

/* select */
.stSelectbox > div > div{
    border-radius:12px !important;
    border-color:var(--line) !important;
    background:var(--surface) !important;
}
.stRadio label, .stCheckbox label{
    color:var(--text) !important;
    font-weight:700 !important;
}

/* tags */
.tag{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    height:1.55rem;
    padding:0 0.58rem;
    border-radius:999px;
    font-size:0.7rem;
    font-weight:800;
    white-space:nowrap;
}
.tag-warm{ background:var(--warm-bg); color:var(--warm-text); }
.tag-cool{ background:var(--cool-bg); color:var(--cool-text); }
.tag-season{ background:#F5EED9; color:#685839; }
.tag-cat{ background:#ECE4CF; color:#5E513A; }
.tag-new{ background:var(--new-bg); color:var(--new-text); }

/* picker summary */
.pick-box{
    margin-top:0.5rem;
    padding:0.8rem 0.9rem;
    border:1px solid var(--line);
    border-radius:12px;
    background:var(--surface);
}
.pick-empty{
    color:var(--muted);
    font-size:0.8rem;
    font-weight:600;
}
.pick-title{
    display:flex;
    align-items:center;
    flex-wrap:wrap;
    gap:0.38rem 0.38rem;
    color:var(--text);
    font-size:0.83rem;
    font-weight:800;
    line-height:1.5;
}
.pick-note{
    margin-top:0.35rem;
    color:var(--sub);
    font-size:0.76rem;
    line-height:1.65;
}
.swatch{
    display:inline-block;
    width:14px;
    height:14px;
    border-radius:50%;
    border:1.5px solid rgba(0,0,0,0.12);
    vertical-align:middle;
    margin-right:0.25rem;
}

/* result */
.result-box{
    border:1px solid var(--line);
    border-radius:20px;
    padding:1.3rem 1.4rem;
    margin-bottom:1rem;
}
.result-warm{
    background:linear-gradient(135deg,#FFF7DF 0%,#F8EDD0 100%);
}
.result-cool{
    background:linear-gradient(135deg,#EDF2FF 0%,#E1E9FF 100%);
}
.result-title{
    font-size:1.85rem;
    font-weight:900;
    letter-spacing:-0.03em;
    margin-bottom:0.35rem;
}
.result-desc{
    color:var(--sub);
    font-size:0.94rem;
    line-height:1.75;
}

/* cards */
.card{
    display:grid;
    grid-template-columns:16px 1fr auto;
    gap:0.75rem;
    align-items:start;
    padding:0.9rem;
    border:1px solid var(--line);
    border-radius:14px;
    background:var(--surface);
    margin-bottom:0.65rem;
}
.card-main{
    min-width:0;
}
.card-name{
    display:flex;
    align-items:center;
    flex-wrap:wrap;
    gap:0.38rem 0.38rem;
    font-size:0.84rem;
    font-weight:800;
    line-height:1.5;
    color:var(--text);
}
.card-shade{
    margin-top:0.2rem;
    color:var(--muted);
    font-size:0.78rem;
    line-height:1.55;
}
.card-note{
    margin-top:0.2rem;
    color:var(--sub);
    font-size:0.76rem;
    line-height:1.65;
}
.card-fit{
    color:var(--accent);
    font-size:0.72rem;
    font-weight:800;
    white-space:nowrap;
}

/* info */
.info-band{
    padding:1rem 1.1rem;
    border-radius:16px;
    border:1px solid var(--line);
    background:rgba(255,255,255,0.62);
    margin-bottom:1rem;
}
.info-band small{
    display:block;
    margin-top:0.3rem;
    color:var(--sub);
    font-size:0.84rem;
    line-height:1.7;
}

.footer{
    margin-top:2rem;
    text-align:center;
    color:var(--muted);
    font-size:0.75rem;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA
# 실제 사용 가능한 구조로 안정성 우선
# =========================================================
def item(tone, seasons, chroma, value, category, hex_col, note, available=True, new_2026=False):
    return {
        "tone": tone,
        "seasons": seasons,
        "chroma": chroma,
        "value": value,
        "category": category,
        "hex": hex_col,
        "note": note,
        "available": available,
        "new_2026": new_2026,
    }

DB = {
    "롬앤 더 쥬시 래스팅 틴트": {
        "01 포멜로 스킨": item("warm", ["spring", "autumn"], 1, 4, "lip", "#D9A788", "밝은 누드 코랄 계열"),
        "02 누카다미아": item("warm", ["autumn", "spring"], 1, 3, "lip", "#BB7E63", "잔잔한 MLBB 브릭 베이지"),
        "03 베어 그레이프": item("cool", ["summer"], 1, 4, "lip", "#C58FA1", "맑은 포도빛 핑크"),
        "04 피그 피그": item("cool", ["summer", "winter"], 2, 3, "lip", "#BD738E", "뮤트 로즈 계열"),
        "05 쥬쥬브": item("warm", ["autumn", "spring"], 2, 3, "lip", "#B96858", "웜 레드 브릭"),
        "06 필링 앵두": item("cool", ["winter"], 3, 2, "lip", "#A43E4E", "선명한 체리 레드"),
        "07 체리 밤": item("warm", ["autumn"], 3, 2, "lip", "#95453E", "브릭 체리"),
        "08 핑크 펌킨": item("warm", ["spring"], 3, 4, "lip", "#E19386", "산뜻한 핑크 코랄"),
        "09 멀드 피치": item("warm", ["spring", "autumn"], 2, 4, "lip", "#D6937C", "복숭아 누드"),
        "10 베어 애프리콧": item("warm", ["spring"], 2, 4, "lip", "#D9A27F", "밝은 살구 코랄"),
        "11 파파야 잼": item("warm", ["spring"], 3, 4, "lip", "#D87556", "생기있는 파파야 코랄"),
        "12 애플 브라운": item("warm", ["autumn"], 2, 2, "lip", "#9C5A47", "깊은 브라운 레드"),
        "13 잇 도토리": item("warm", ["autumn"], 1, 2, "lip", "#8C624F", "도토리 브라운 MLBB"),
        "14 아몬드 로즈": item("cool", ["summer", "winter"], 1, 3, "lip", "#9E7281", "차분한 로즈 브라운"),
        "15 베어 피그": item("cool", ["summer"], 1, 4, "lip", "#D29AA5", "부드러운 피그 핑크"),
        "16 플럼 콕": item("cool", ["winter"], 3, 2, "lip", "#8F4A67", "딥 플럼"),
    },
    "에뛰드 픽싱 틴트": {
        "01 아날로그 로즈": item("cool", ["summer"], 2, 3, "lip", "#B97886", "차분한 로즈 핑크"),
        "02 빈티지 레드": item("cool", ["winter"], 3, 2, "lip", "#9E434D", "깊은 레드"),
        "03 멜로우 피치": item("warm", ["spring"], 2, 4, "lip", "#D4947C", "복숭아 코랄"),
        "04 진저 밀크티": item("warm", ["autumn"], 1, 3, "lip", "#A67967", "부드러운 밀크티 브라운"),
        "05 미드나잇 모브": item("cool", ["winter", "summer"], 2, 2, "lip", "#8B667C", "모브 로즈"),
        "06 소프트 월넛": item("warm", ["autumn"], 1, 2, "lip", "#86604F", "차분한 월넛 브라운"),
        "07 크랜베리 플럼": item("cool", ["winter"], 3, 2, "lip", "#8F4258", "쿨 크랜베리"),
        "08 더스티 베이지": item("warm", ["autumn", "spring"], 1, 4, "lip", "#C3A08D", "누디 베이지"),
    },
    "페리페라 무드 글로이 틴트": {
        "21 쿨링 핑크": item("cool", ["summer"], 2, 4, "lip", "#D78FAE", "맑은 쿨 핑크", new_2026=True),
        "22 핑크 프라이즈": item("cool", ["summer"], 2, 4, "lip", "#DA91A8", "생기있는 핑크", new_2026=True),
        "23 코랄 케미스트리": item("warm", ["spring"], 3, 4, "lip", "#E88A73", "맑은 코랄", new_2026=True),
        "24 코랄 프라이드": item("warm", ["spring"], 3, 4, "lip", "#E37F62", "선명한 코랄 오렌지", new_2026=True),
        "25 핫 스트로베리": item("cool", ["winter"], 3, 3, "lip", "#C85271", "스트로베리 핑크", new_2026=True),
        "26 와이 소 베리": item("cool", ["winter"], 3, 2, "lip", "#A94D72", "베리 플럼", new_2026=True),
    },
    "롬앤 베러 댄 치크": {
        "C01 피치칩": item("warm", ["spring"], 2, 4, "blush", "#E6AF93", "맑은 피치 코랄"),
        "C02 블루베리칩": item("cool", ["summer"], 2, 4, "blush", "#C9A1B8", "부드러운 쿨 모브"),
        "C03 피그칩": item("cool", ["summer", "winter"], 2, 3, "blush", "#C98798", "피그 로즈"),
        "W01 오디 밀크": item("cool", ["winter"], 2, 3, "blush", "#A7748E", "오디빛 플럼"),
        "W02 스트로베리 밀크": item("cool", ["summer"], 1, 4, "blush", "#DDB5C4", "딸기우유 핑크"),
        "W03 애프리콧 밀크": item("warm", ["spring"], 1, 4, "blush", "#EDC0A4", "밀키 살구빛"),
        "N01 너티 누드": item("warm", ["autumn"], 1, 3, "blush", "#C2A28E", "누디 베이지"),
    },
    "페리페라 맑게 물든 선샤인 치크": {
        "025 반달입떡해": item("warm", ["spring"], 2, 4, "blush", "#E0A58A", "살짝 코랄 기운의 피치"),
        "026 달달베리해": item("cool", ["winter"], 3, 3, "blush", "#B46E86", "베리 핑크"),
        "029 모브낭낭해": item("cool", ["summer"], 2, 4, "blush", "#CEA1B8", "차분한 모브 핑크"),
        "030 장미멀멀해": item("cool", ["summer"], 2, 3, "blush", "#B98892", "말린 장미 느낌의 로즈"),
        "031 라떼달달해": item("warm", ["autumn"], 1, 3, "blush", "#C7A48D", "밀키한 라떼 베이지"),
    },
    "클리오 프로 아이 팔레트 에어": {
        "01 코랄 스튜디오": item("warm", ["spring"], 3, 4, "shadow", "#C98D66", "화사한 코랄/피치 팔레트"),
        "02 로즈 커넥트": item("cool", ["summer", "winter"], 2, 3, "shadow", "#B68593", "로즈 모브 계열 팔레트"),
        "03 뮤트 라이브러리": item("cool", ["summer"], 1, 3, "shadow", "#9B8A8F", "뮤트한 그레이시 로즈 브라운"),
    },
}

PC = {
    "봄 라이트 웜": {
        "tone": "warm",
        "season": "spring",
        "emoji": "🌼",
        "desc": "밝고 맑은 웜톤이에요. 살구·피치·라이트 코랄처럼 투명감 있는 컬러가 가장 자연스럽게 살아나요.",
        "best": ["피치", "살구", "라이트 코랄", "누디 베이지"],
        "avoid": ["푸른기 강한 핑크", "버건디", "차가운 그레이"],
    },
    "봄 비비드 웜": {
        "tone": "warm",
        "season": "spring",
        "emoji": "🌺",
        "desc": "맑고 선명한 색을 받는 타입이에요. 생기 있는 코랄 레드, 쨍한 웜 핑크가 얼굴을 또렷하게 보여줘요.",
        "best": ["비비드 코랄", "오렌지 레드", "웜 핑크"],
        "avoid": ["회끼 도는 모브", "탁한 브라운"],
    },
    "가을 뮤트 웜": {
        "tone": "warm",
        "season": "autumn",
        "emoji": "🍁",
        "desc": "채도가 낮고 부드러운 웜톤이에요. 브라운, 누드 베이지, 잔잔한 브릭 계열이 차분하게 어울려요.",
        "best": ["누드 베이지", "웜 브라운", "브릭", "카멜"],
        "avoid": ["형광기 코랄", "차가운 라일락"],
    },
    "가을 딥 웜": {
        "tone": "warm",
        "season": "autumn",
        "emoji": "🥮",
        "desc": "깊이감 있는 웜톤이에요. 도토리 브라운, 테라코타, 딥 브릭처럼 무게감 있는 색이 잘 맞아요.",
        "best": ["테라코타", "도토리 브라운", "딥 브릭", "카카오 브라운"],
        "avoid": ["아이스 핑크", "푸른 레드"],
    },
    "여름 라이트 쿨": {
        "tone": "cool",
        "season": "summer",
        "emoji": "🫧",
        "desc": "부드럽고 밝은 쿨톤이에요. 우유빛 핑크, 라일락, 라이트 로즈가 맑게 어울려요.",
        "best": ["베이비 핑크", "라일락", "라이트 로즈"],
        "avoid": ["노란 코랄", "짙은 브라운"],
    },
    "여름 뮤트 쿨": {
        "tone": "cool",
        "season": "summer",
        "emoji": "🌫️",
        "desc": "회끼와 부드러움이 있는 쿨톤이에요. 뮤트 로즈, 모브, 그레이시 핑크가 세련되게 맞아요.",
        "best": ["모브", "뮤트 로즈", "그레이시 핑크"],
        "avoid": ["쨍한 오렌지", "노란 브릭"],
    },
    "겨울 비비드 쿨": {
        "tone": "cool",
        "season": "winter",
        "emoji": "❄️",
        "desc": "선명하고 대비감이 강한 쿨톤이에요. 또렷한 베리 핑크, 체리 레드가 얼굴을 살려줘요.",
        "best": ["체리 레드", "비비드 핑크", "쿨 베리"],
        "avoid": ["누디 베이지", "오렌지 코랄"],
    },
    "겨울 딥 쿨": {
        "tone": "cool",
        "season": "winter",
        "emoji": "🌌",
        "desc": "깊고 선명한 쿨톤이에요. 플럼, 버건디, 딥 로즈처럼 밀도 있는 컬러가 특히 잘 어울려요.",
        "best": ["플럼", "버건디", "딥 로즈", "블랙 체리"],
        "avoid": ["웜 브라운", "살구 코랄"],
    },
}

PAIRING = {
    ("spring", "blush"): [
        ("롬앤 베러 댄 치크", "C01 피치칩"),
        ("롬앤 베러 댄 치크", "W03 애프리콧 밀크"),
        ("페리페라 맑게 물든 선샤인 치크", "025 반달입떡해"),
    ],
    ("spring", "shadow"): [
        ("클리오 프로 아이 팔레트 에어", "01 코랄 스튜디오"),
    ],
    ("autumn", "blush"): [
        ("롬앤 베러 댄 치크", "N01 너티 누드"),
        ("페리페라 맑게 물든 선샤인 치크", "031 라떼달달해"),
    ],
    ("autumn", "shadow"): [
        ("클리오 프로 아이 팔레트 에어", "03 뮤트 라이브러리"),
    ],
    ("summer", "blush"): [
        ("롬앤 베러 댄 치크", "W02 스트로베리 밀크"),
        ("페리페라 맑게 물든 선샤인 치크", "029 모브낭낭해"),
        ("페리페라 맑게 물든 선샤인 치크", "030 장미멀멀해"),
    ],
    ("summer", "shadow"): [
        ("클리오 프로 아이 팔레트 에어", "02 로즈 커넥트"),
        ("클리오 프로 아이 팔레트 에어", "03 뮤트 라이브러리"),
    ],
    ("winter", "blush"): [
        ("롬앤 베러 댄 치크", "W01 오디 밀크"),
        ("페리페라 맑게 물든 선샤인 치크", "026 달달베리해"),
    ],
    ("winter", "shadow"): [
        ("클리오 프로 아이 팔레트 에어", "02 로즈 커넥트"),
    ],
}

CAT_KR = {
    "lip": "립",
    "blush": "블러셔",
    "shadow": "섀도우",
}

SEA_KR = {
    "spring": "봄 웜",
    "summer": "여름 쿨",
    "autumn": "가을 웜",
    "winter": "겨울 쿨",
}

# =========================================================
# HELPERS
# =========================================================
def tone_tag(tone):
    if tone == "warm":
        return '<span class="tag tag-warm">웜톤</span>'
    return '<span class="tag tag-cool">쿨톤</span>'

def season_tag(season):
    return f'<span class="tag tag-season">{SEA_KR.get(season, season)}</span>'

def category_tag(category):
    return f'<span class="tag tag-cat">{CAT_KR.get(category, category)}</span>'

def new_tag(is_new):
    return '<span class="tag tag-new">NEW</span>' if is_new else ''

def swatch(hex_col, size=14):
    return f'<span class="swatch" style="width:{size}px;height:{size}px;background:{hex_col};"></span>'

def product_names(category=None):
    names = []
    for pname, shades in DB.items():
        for shade_name, d in shades.items():
            if category is None or d["category"] == category:
                names.append(pname)
                break
    return sorted(names)

def shade_names(pname):
    return list(DB[pname].keys())

def get_recs(tone, season, category=None, only_new=False, limit=8):
    primary = []
    secondary = []

    for pname, shades in DB.items():
        for shade, d in shades.items():
            if not d["available"]:
                continue
            if category and d["category"] != category:
                continue
            if only_new and not d.get("new_2026", False):
                continue

            row = (pname, shade, d)
            if d["tone"] == tone and season in d["seasons"]:
                primary.append(row)
            elif d["tone"] == tone:
                secondary.append(row)

    return (primary + secondary)[:limit]

def run_analysis(good_list, bad_list, best_list):
    tone_score = 0.0
    chroma_score = 0.0
    value_score = 0.0
    total = 0.0

    def acc(items, weight):
        nonlocal tone_score, chroma_score, value_score, total
        for entry in items:
            if not entry:
                continue
            pname, shade = entry
            d = DB[pname][shade]

            tone_score += (1 if d["tone"] == "warm" else -1) * weight
            chroma_score += d["chroma"] * weight
            value_score += d["value"] * weight
            total += abs(weight)

    acc(good_list, 1.0)
    acc(best_list, 2.0)
    acc(bad_list, -1.4)

    if total == 0:
        return None

    avg_c = chroma_score / total
    avg_v = value_score / total

    if tone_score >= 0:
        if avg_v >= 3.6:
            pc = "봄 비비드 웜" if avg_c >= 2.3 else "봄 라이트 웜"
        else:
            pc = "가을 딥 웜" if avg_c >= 1.8 else "가을 뮤트 웜"
    else:
        if avg_v >= 3.5:
            pc = "여름 라이트 쿨" if avg_c >= 1.8 else "여름 뮤트 쿨"
        else:
            pc = "겨울 비비드 쿨" if avg_c >= 2.5 else "겨울 딥 쿨"

    return {
        "pc": pc,
        "tone": PC[pc]["tone"],
        "season": PC[pc]["season"],
    }

def card_html(pname, shade, d, fit_text=""):
    fit_html = f'<div class="card-fit">{fit_text}</div>' if fit_text else '<div></div>'
    season_html = "".join([season_tag(s) for s in d["seasons"]])

    return f"""
    <div class="card">
        {swatch(d['hex'], 16)}
        <div class="card-main">
            <div class="card-name">
                <span>{pname}</span>
                {new_tag(d.get("new_2026", False))}
            </div>
            <div class="card-shade">
                {shade} · {CAT_KR[d["category"]]} · {tone_tag(d["tone"])} {season_html}
            </div>
            <div class="card-note">{d["note"]}</div>
        </div>
        {fit_html}
    </div>
    """

def selection_preview(entry):
    if not entry:
        return '<div class="pick-box"><div class="pick-empty">선택된 상품이 여기에 바로 표시됩니다.</div></div>'

    pname, shade = entry
    d = DB[pname][shade]
    season_html = "".join([season_tag(s) for s in d["seasons"]])

    return f"""
    <div class="pick-box">
        <div class="pick-title">
            {swatch(d["hex"], 14)}
            <span>{pname} · {shade}</span>
            {tone_tag(d["tone"])}
            {season_html}
            {category_tag(d["category"])}
            {new_tag(d.get("new_2026", False))}
        </div>
        <div class="pick-note">{d["note"]}</div>
    </div>
    """

# =========================================================
# PICKER
# =========================================================
def product_picker(prefix):
    category_map = {
        "전체": None,
        "립": "lip",
        "블러셔": "blush",
        "섀도우": "shadow",
    }

    c1, c2 = st.columns([1, 2])

    with c1:
        category_label = st.selectbox(
            "카테고리",
            list(category_map.keys()),
            key=f"{prefix}_cat",
            label_visibility="collapsed",
        )
    category = category_map[category_label]

    name_list = product_names(category)

    with c2:
        pname = st.selectbox(
            "제품명",
            options=[None] + name_list,
            format_func=lambda x: "제품명 선택" if x is None else x,
            key=f"{prefix}_pname",
            label_visibility="collapsed",
        )

    if pname is None:
        st.markdown(selection_preview(None), unsafe_allow_html=True)
        return None

    shades = shade_names(pname)
    shade = st.selectbox(
        "호수",
        options=[None] + shades,
        format_func=lambda x: "호수(컬러) 선택" if x is None else x,
        key=f"{prefix}_shade",
        label_visibility="collapsed",
    )

    if shade is None:
        st.markdown(f"""
        <div class="pick-box">
            <div class="pick-title"><span>{pname}</span></div>
            <div class="pick-note">제품명은 선택됐고, 아직 호수는 선택되지 않았어요.</div>
        </div>
        """, unsafe_allow_html=True)
        return None

    entry = (pname, shade)
    st.markdown(selection_preview(entry), unsafe_allow_html=True)
    return entry

# =========================================================
# RENDER RESULT
# =========================================================
def render_result(res):
    pc_name = res["pc"]
    info = PC[pc_name]

    result_class = "result-warm" if info["tone"] == "warm" else "result-cool"

    st.divider()
    st.markdown(f"""
    <div class="result-box {result_class}">
        <div class="result-title">{info["emoji"]} {pc_name}</div>
        <div class="result-desc">{info["desc"]}</div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("**잘 어울리는 컬러**")
        for x in info["best"]:
            st.markdown(f"- {x}")

    with c2:
        st.markdown("**피하면 좋은 컬러**")
        for x in info["avoid"]:
            st.markdown(f"- {x}")

    st.markdown("### 맞춤 추천 제품")

    f1, f2 = st.columns([2, 1])

    with f1:
        category_label = st.radio(
            "추천 카테고리",
            ["전체", "립", "블러셔", "섀도우"],
            horizontal=True,
            key="result_category",
            label_visibility="collapsed",
        )

    with f2:
        only_new = st.checkbox("NEW만 보기", key="result_only_new")

    category_map = {
        "전체": None,
        "립": "lip",
        "블러셔": "blush",
        "섀도우": "shadow",
    }

    recs = get_recs(
        tone=res["tone"],
        season=res["season"],
        category=category_map[category_label],
        only_new=only_new,
        limit=8,
    )

    if not recs:
        st.info("조건에 맞는 추천 제품이 없어요.")
        return

    cols = st.columns(2)

    for i, (pname, shade, d) in enumerate(recs):
        fit_text = "완벽 매칭" if res["season"] in d["seasons"] else "같은 톤 추천"
        with cols[i % 2]:
            st.markdown(card_html(pname, shade, d, fit_text), unsafe_allow_html=True)

# =========================================================
# TABS
# =========================================================
def tab_analysis():
    st.markdown('<div class="section-title">퍼스널 컬러 분석</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">사용해봤던 상품을 고르면, 선택한 상품 이름이 바로 아래에 보여서 빈칸처럼 보이지 않게 만들었어요. 제품명 → 호수 순서로 고르면 됩니다.</div>',
        unsafe_allow_html=True,
    )

    with st.expander("입력 기준 보기"):
        st.markdown("""
- **잘 맞았던 제품**: 얼굴 톤이 정돈되고 자연스럽게 예뻐 보였던 제품
- **안 맞았던 제품**: 칙칙해 보이거나 떠 보였던 제품
- **반응 좋았던 제품**: 주변 반응이 특히 좋았던 제품
        """)

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("""
        <div class="panel">
            <div class="panel-head">
                <div class="panel-icon">👍</div>
                <div>잘 맞았던 제품</div>
            </div>
            <div class="panel-sub">필수 · 1개 이상</div>
        </div>
        """, unsafe_allow_html=True)
        g1 = product_picker("g1")
        st.divider()
        g2 = product_picker("g2")
        st.divider()
        g3 = product_picker("g3")

    with col2:
        st.markdown("""
        <div class="panel">
            <div class="panel-head">
                <div class="panel-icon">👎</div>
                <div>안 맞았던 제품</div>
            </div>
            <div class="panel-sub">선택 · 0~3개</div>
        </div>
        """, unsafe_allow_html=True)
        b1 = product_picker("b1")
        st.divider()
        b2 = product_picker("b2")
        st.divider()
        b3 = product_picker("b3")

    with col3:
        st.markdown("""
        <div class="panel">
            <div class="panel-head">
                <div class="panel-icon">✨</div>
                <div>반응 좋았던 제품</div>
            </div>
            <div class="panel-sub">선택 · 0~3개</div>
        </div>
        """, unsafe_allow_html=True)
        t1 = product_picker("t1")
        st.divider()
        t2 = product_picker("t2")
        st.divider()
        t3 = product_picker("t3")

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    _, center, _ = st.columns([1.2, 1.6, 1.2])
    with center:
        clicked = st.button("🌼 퍼스널 컬러 분석하기", use_container_width=True)

    if clicked:
        goods = [x for x in [g1, g2, g3] if x]
        bads = [x for x in [b1, b2, b3] if x]
        bests = [x for x in [t1, t2, t3] if x]

        if not goods:
            st.warning("잘 맞았던 제품을 최소 1개 선택해 주세요.")
        else:
            st.session_state["result"] = run_analysis(goods, bads, bests)

    if st.session_state.get("result") is not None:
        render_result(st.session_state["result"])

def tab_pairing():
    st.markdown('<div class="section-title">연계 추천</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">분석 결과가 있으면 그 결과를 바탕으로 립, 블러셔, 섀도우 조합을 보여줍니다.</div>',
        unsafe_allow_html=True,
    )

    pc_list = list(PC.keys())
    default_pc = st.session_state.get("result", {}).get("pc", pc_list[0])
    selected_pc = st.selectbox("퍼스널 컬러", pc_list, index=pc_list.index(default_pc))

    info = PC[selected_pc]

    st.markdown(f"""
    <div class="info-band">
        <b>{info["emoji"]} {selected_pc}</b>
        <small>{info["desc"]}</small>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 립 추천")
    lips = get_recs(info["tone"], info["season"], category="lip", limit=6)

    lip_cols = st.columns(2)
    for i, (pname, shade, d) in enumerate(lips):
        with lip_cols[i % 2]:
            st.markdown(card_html(pname, shade, d), unsafe_allow_html=True)

    st.markdown("### 블러셔 연결 추천")
    blush_rows = [(pn, sh, DB[pn][sh]) for pn, sh in PAIRING.get((info["season"], "blush"), [])]
    blush_cols = st.columns(2)
    for i, (pname, shade, d) in enumerate(blush_rows):
        with blush_cols[i % 2]:
            st.markdown(card_html(pname, shade, d), unsafe_allow_html=True)

    st.markdown("### 섀도우 연결 추천")
    shadow_rows = [(pn, sh, DB[pn][sh]) for pn, sh in PAIRING.get((info["season"], "shadow"), [])]
    shadow_cols = st.columns(2)
    for i, (pname, shade, d) in enumerate(shadow_rows):
        with shadow_cols[i % 2]:
            st.markdown(card_html(pname, shade, d), unsafe_allow_html=True)

def tab_browse():
    st.markdown('<div class="section-title">제품 탐색</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">카테고리나 톤으로 필터링해서 전체 제품을 볼 수 있어요. NEW 표시는 2026 신제품에만 붙습니다.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        category_label = st.selectbox("카테고리", ["전체", "립", "블러셔", "섀도우"], key="browse_cat")
    with c2:
        tone_label = st.selectbox("톤", ["전체", "웜톤", "쿨톤"], key="browse_tone")
    with c3:
        only_new = st.checkbox("NEW만 보기", key="browse_new")

    category_map = {
        "전체": None,
        "립": "lip",
        "블러셔": "blush",
        "섀도우": "shadow",
    }
    tone_map = {
        "전체": None,
        "웜톤": "warm",
        "쿨톤": "cool",
    }

    rows = []
    for pname, shades in DB.items():
        for shade, d in shades.items():
            if category_map[category_label] and d["category"] != category_map[category_label]:
                continue
            if tone_map[tone_label] and d["tone"] != tone_map[tone_label]:
                continue
            if only_new and not d.get("new_2026", False):
                continue
            rows.append((pname, shade, d))

    st.caption(f"총 {len(rows)}개 항목")

    if not rows:
        st.info("조건에 맞는 제품이 없어요.")
        return

    cols = st.columns(2)
    for i, (pname, shade, d) in enumerate(rows):
        with cols[i % 2]:
            st.markdown(card_html(pname, shade, d), unsafe_allow_html=True)

def tab_guide():
    st.markdown('<div class="section-title">컬러 가이드</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">8개 세부톤의 특징을 한눈에 보게 정리했어요.</div>',
        unsafe_allow_html=True,
    )

    for name, info in PC.items():
        with st.expander(f"{info['emoji']} {name}"):
            c1, c2 = st.columns([1.3, 1])

            with c1:
                st.markdown(f"**설명**\n\n{info['desc']}")

            with c2:
                st.markdown("**잘 어울림**")
                for x in info["best"]:
                    st.markdown(f"- {x}")

                st.markdown("**주의 컬러**")
                for x in info["avoid"]:
                    st.markdown(f"- {x}")

# =========================================================
# MAIN
# =========================================================
def main():
    if "result" not in st.session_state:
        st.session_state["result"] = None

    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-kicker">🌼 TONEME · streamlit edition</div>
        <div class="hero-title">실사용 기준으로 고르는 <span class="accent">퍼스널 컬러 추천</span></div>
        <div class="hero-sub">
            제품명 먼저 고르고, 그다음 호수를 선택하도록 구성했어요.
            그리고 사용자가 고른 상품은 바로 아래 요약 박스에 떠서,
            하얗게 빈칸처럼 보이는 문제를 없앴습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    t1, t2, t3, t4 = st.tabs([
        "🎨 퍼스널 컬러 분석",
        "✨ 연계 추천",
        "🗂️ 제품 탐색",
        "📖 컬러 가이드",
    ])

    with t1:
        tab_analysis()

    with t2:
        tab_pairing()

    with t3:
        tab_browse()

    with t4:
        tab_guide()

    st.markdown(
        '<div class="footer">TONEME · 선택한 상품명 즉시 표시 · NEW는 2026 상품만 표기</div>',
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
