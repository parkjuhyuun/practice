import streamlit as st
from typing import Dict, List, Optional, Tuple

st.set_page_config(
    page_title="TONEME · 퍼스널 컬러 뷰티",
    page_icon="🌼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Style
# -----------------------------
st.markdown(
    """
<style>
:root {
    --bg: #fbf7ea;
    --surface: #fffdf7;
    --surface-2: #f7f1dd;
    --line: #e6dcc0;
    --line-strong: #cfbc72;
    --text: #241c10;
    --sub: #66573e;
    --muted: #8b7a5c;
    --accent: #8e6f1f;
    --accent-soft: #efe3b0;
    --warm-chip: #7f4f22;
    --cool-chip: #445b9f;
    --ok: #305f47;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: var(--bg) !important;
    color: var(--text);
    font-family: Pretendard, "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic", sans-serif;
}
[data-testid="stSidebar"] { display:none; }
.block-container {
    max-width: 1160px !important;
    padding: 2.4rem 2.8rem 4rem !important;
}

.hero-wrap {
    padding: 1.2rem 0 1.8rem;
}
.hero-kicker {
    display:inline-flex;
    align-items:center;
    gap:0.45rem;
    padding:0.28rem 0.72rem;
    border:1px solid var(--line-strong);
    border-radius:999px;
    background:rgba(255,255,255,0.55);
    color:var(--accent);
    font-size:0.78rem;
    font-weight:700;
    letter-spacing:0.02em;
}
.hero-title {
    margin-top:1rem;
    font-size:3.1rem;
    line-height:1.02;
    letter-spacing:-0.03em;
    font-weight:800;
    color:var(--text);
}
.hero-title .accent { color:var(--accent); }
.hero-sub {
    margin-top:0.8rem;
    max-width:820px;
    font-size:0.97rem;
    line-height:1.8;
    color:var(--sub);
}

.stTabs [data-baseweb="tab-list"] {
    gap: 0.25rem;
    border-bottom:1px solid var(--line);
}
.stTabs [data-baseweb="tab"] {
    height:auto;
    padding:0.85rem 1rem 0.8rem;
    border-radius:12px 12px 0 0;
    color:var(--sub);
    font-size:0.92rem;
    font-weight:700;
}
.stTabs [aria-selected="true"] {
    color:var(--text) !important;
    background:rgba(255,255,255,0.56) !important;
    border:1px solid var(--line) !important;
    border-bottom:1px solid var(--bg) !important;
}

.section-title {
    font-size:1.16rem;
    font-weight:800;
    color:var(--text);
    margin-bottom:0.2rem;
}
.section-sub {
    font-size:0.92rem;
    line-height:1.75;
    color:var(--sub);
    margin-bottom:1.2rem;
}
.panel {
    background:rgba(255,255,255,0.58);
    border:1px solid var(--line);
    border-radius:18px;
    padding:1.1rem 1rem 1rem;
    height:100%;
}
.panel-head {
    display:flex;
    align-items:center;
    gap:0.55rem;
    margin-bottom:0.85rem;
    padding-bottom:0.75rem;
    border-bottom:1px solid var(--line);
    font-size:0.9rem;
    font-weight:800;
    color:var(--text);
}
.panel-icon {
    width:1.9rem;
    height:1.9rem;
    border-radius:12px;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    background:var(--surface-2);
    font-size:1rem;
    flex:0 0 1.9rem;
}
.panel-sub {
    margin-top:-0.15rem;
    margin-bottom:0.85rem;
    color:var(--muted);
    font-size:0.78rem;
    line-height:1.65;
}

[data-testid="stSelectbox"] label,
[data-testid="stRadio"] label,
[data-testid="stCheckbox"] label {
    color:var(--text) !important;
    font-weight:700 !important;
}
[data-testid="stSelectbox"] > div > div {
    border-radius:12px !important;
    border-color:var(--line) !important;
    background:var(--surface) !important;
}

.mini-row {
    display:grid;
    grid-template-columns: 18px 1fr;
    gap:0.72rem;
    align-items:start;
    margin-top:0.55rem;
    padding:0.78rem 0.86rem;
    background:var(--surface);
    border:1px solid var(--line);
    border-radius:12px;
}
.swatch {
    width:18px;
    height:18px;
    border-radius:50%;
    border:1.5px solid rgba(0,0,0,0.12);
    margin-top:0.1rem;
}
.mini-main {
    min-width:0;
}
.mini-title {
    display:flex;
    align-items:center;
    flex-wrap:wrap;
    gap:0.45rem 0.4rem;
    color:var(--text);
    font-size:0.83rem;
    font-weight:800;
    line-height:1.45;
}
.mini-note {
    margin-top:0.3rem;
    color:var(--sub);
    font-size:0.76rem;
    line-height:1.6;
}

.tag {
    display:inline-flex;
    align-items:center;
    justify-content:center;
    height:1.52rem;
    padding:0 0.58rem;
    border-radius:999px;
    font-size:0.7rem;
    font-weight:800;
    white-space:nowrap;
}
.tag-warm { background:#fff0de; color:#8a4d11; }
.tag-cool { background:#e9efff; color:#3f5da8; }
.tag-spring, .tag-autumn, .tag-summer, .tag-winter {
    background:#f6f0de; color:#6b5a32;
}
.tag-cat { background:#efe8d1; color:#5e4f34; }
.tag-new { background:#1f6f54; color:#effff7; }
.tag-disc { background:#ece9e2; color:#73685a; }

.result-box {
    border-radius:22px;
    padding:1.45rem 1.5rem;
    margin-bottom:1rem;
    border:1px solid var(--line);
}
.result-warm { background:linear-gradient(135deg, #fff7dd 0%, #f8edc9 100%); }
.result-cool { background:linear-gradient(135deg, #edf2ff 0%, #e2e9ff 100%); }
.result-title {
    font-size:1.9rem;
    font-weight:900;
    letter-spacing:-0.03em;
    margin-bottom:0.35rem;
}
.result-desc {
    color:var(--sub);
    font-size:0.95rem;
    line-height:1.75;
}

.card {
    display:grid;
    grid-template-columns: 18px 1fr auto;
    gap:0.75rem;
    align-items:start;
    padding:0.88rem 0.95rem;
    border:1px solid var(--line);
    border-radius:14px;
    background:var(--surface);
    margin-bottom:0.6rem;
}
.card-main { min-width:0; }
.card-name {
    display:flex;
    align-items:center;
    flex-wrap:wrap;
    gap:0.4rem;
    font-size:0.84rem;
    font-weight:800;
    line-height:1.45;
    color:var(--text);
}
.card-shade {
    color:var(--muted);
    font-size:0.78rem;
    margin-top:0.2rem;
    line-height:1.5;
}
.card-note {
    color:var(--sub);
    font-size:0.76rem;
    margin-top:0.2rem;
    line-height:1.6;
}
.card-fit {
    color:var(--accent);
    font-size:0.73rem;
    font-weight:800;
    white-space:nowrap;
    padding-top:0.1rem;
}

.info-band {
    padding:1rem 1.15rem;
    border-radius:16px;
    border:1px solid var(--line);
    background:rgba(255,255,255,0.58);
    margin-bottom:1rem;
}
.info-band b { color:var(--text); }
.info-band small {
    display:block;
    color:var(--sub);
    font-size:0.84rem;
    line-height:1.7;
    margin-top:0.28rem;
}

.footer {
    margin-top:2.2rem;
    text-align:center;
    color:var(--muted);
    font-size:0.75rem;
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Helpers / data model
# -----------------------------

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


DB: Dict[str, Dict[str, dict]] = {
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
        "17 다크 코코넛": item("warm", ["autumn"], 1, 2, "lip", "#7F5648", "다크 브라운 누드"),
        "19 썸머 센트": item("cool", ["summer"], 2, 4, "lip", "#D28CA4", "맑은 쿨 핑크"),
        "20 쥬쥬 피그": item("cool", ["summer"], 2, 3, "lip", "#C37B94", "로지 피그 핑크"),
        "21 그레이프 밤": item("cool", ["winter"], 3, 2, "lip", "#995272", "포도빛 베리"),
        "22 도토리 밤": item("warm", ["autumn"], 1, 2, "lip", "#835B49", "딥 도토리 브라운"),
        "23 피치 피치 미": item("warm", ["spring"], 3, 4, "lip", "#EA9A87", "맑은 피치 핑크"),
        "24 베어 쥬시 오": item("warm", ["spring"], 2, 4, "lip", "#DEA08A", "누디한 살구빛"),
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
        "10 스모키 체리": item("cool", ["winter"], 3, 2, "lip", "#8D4150", "스모키 체리 레드"),
        "11 로즈 블렌딩": item("cool", ["summer"], 2, 3, "lip", "#B77B8E", "뮤트 로즈"),
        "12 살몬 브릭": item("warm", ["autumn", "spring"], 2, 3, "lip", "#B66C5E", "살몬 브릭"),
        "13 멜란지 로즈": item("cool", ["summer"], 1, 3, "lip", "#A37A84", "그레이시 로즈"),
        "14 로즈 라일락": item("cool", ["summer", "winter"], 2, 4, "lip", "#B28CA7", "라일락 로즈"),
        "15 우디 핑크": item("warm", ["spring", "autumn"], 1, 3, "lip", "#B88782", "따뜻한 우디 핑크"),
        "16 베이크드 피칸": item("warm", ["autumn"], 1, 2, "lip", "#89634E", "딥 피칸 브라운"),
    },
    "페리페라 무드 글로이 틴트": {
        "21 쿨링 핑크": item("cool", ["summer"], 2, 4, "lip", "#D78FAE", "맑은 쿨 핑크", new_2026=True),
        "22 핑크 프라이즈": item("cool", ["summer"], 2, 4, "lip", "#DA91A8", "생기있는 핑크", new_2026=True),
        "23 코랄 케미스트리": item("warm", ["spring"], 3, 4, "lip", "#E88A73", "맑은 코랄", new_2026=True),
        "24 코랄 프라이드": item("warm", ["spring"], 3, 4, "lip", "#E37F62", "선명한 코랄 오렌지", new_2026=True),
        "25 핫 스트로베리": item("cool", ["winter"], 3, 3, "lip", "#C85271", "스트로베리 핑크", new_2026=True),
        "26 와이 소 베리": item("cool", ["winter"], 3, 2, "lip", "#A94D72", "베리 플럼", new_2026=True),
        "27 조킹 핑크": item("cool", ["summer"], 3, 4, "lip", "#D56A9A", "선명한 쿨 핑크", new_2026=True),
        "28 로즈 스탠다드": item("cool", ["summer", "winter"], 2, 3, "lip", "#B77488", "기본 로즈 MLBB", new_2026=True),
        "29 허리 업 핑크": item("cool", ["summer"], 3, 4, "lip", "#DD7DA9", "밝고 화사한 핑크", new_2026=True),
    },
    "롬앤 베러 댄 치크": {
        "C01 피치칩": item("warm", ["spring"], 2, 4, "blush", "#E6AF93", "맑은 피치 코랄"),
        "C02 블루베리칩": item("cool", ["summer"], 2, 4, "blush", "#C9A1B8", "부드러운 쿨 모브"),
        "C03 피그칩": item("cool", ["summer", "winter"], 2, 3, "blush", "#C98798", "피그 로즈"),
        "C04 페어칩": item("warm", ["spring"], 1, 4, "blush", "#DFC2A1", "라이트 베이지 피치"),
        "W01 오디 밀크": item("cool", ["winter"], 2, 3, "blush", "#A7748E", "오디빛 플럼"),
        "W02 스트로베리 밀크": item("cool", ["summer"], 1, 4, "blush", "#DDB5C4", "딸기우유 핑크"),
        "W03 애프리콧 밀크": item("warm", ["spring"], 1, 4, "blush", "#EDC0A4", "밀키 살구빛"),
        "N01 너티 누드": item("warm", ["autumn"], 1, 3, "blush", "#C2A28E", "누디 베이지"),
        "N02 바인 누드": item("cool", ["summer"], 1, 3, "blush", "#B59A9C", "그레이시 누드 모브"),
    },
    "페리페라 맑게 물든 선샤인 치크": {
        "029 모브낭낭해": item("cool", ["summer"], 2, 4, "blush", "#CEA1B8", "차분한 모브 핑크"),
        "030 장미멀멀해": item("cool", ["summer"], 2, 3, "blush", "#B98892", "말린 장미 느낌의 로즈"),
        "031 라떼달달해": item("warm", ["autumn"], 1, 3, "blush", "#C7A48D", "밀키한 라떼 베이지"),
        "026 달달베리해": item("cool", ["winter"], 3, 3, "blush", "#B46E86", "베리 핑크"),
        "025 반달입떡해": item("warm", ["spring"], 2, 4, "blush", "#E0A58A", "살짝 코랄 기운의 피치"),
        "달방아콩콩해": item("cool", ["summer"], 2, 4, "blush", "#D6A9B3", "맑은 핑크 블러셔"),
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
        ("페리페라 맑게 물든 선샤인 치크", "달방아콩콩해"),
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

CAT_KR = {"lip": "립", "blush": "블러셔", "shadow": "섀도우"}
SEA_KR = {"spring": "봄 웜", "summer": "여름 쿨", "autumn": "가을 웜", "winter": "겨울 쿨"}


def tone_tag(t: str) -> str:
    klass = "tag-warm" if t == "warm" else "tag-cool"
    text = "웜톤" if t == "warm" else "쿨톤"
    return f'<span class="tag {klass}">{text}</span>'


def season_tag(s: str) -> str:
    return f'<span class="tag tag-{s}">{SEA_KR.get(s, s)}</span>'


def category_tag(c: str) -> str:
    return f'<span class="tag tag-cat">{CAT_KR.get(c, c)}</span>'


def new_tag(is_new: bool) -> str:
    return '<span class="tag tag-new">NEW · 2026</span>' if is_new else ''


def swatch(hex_col: str) -> str:
    return f'<span class="swatch" style="background:{hex_col};"></span>'


def card_html(pname: str, shade: str, d: dict, fit: str = "") -> str:
    fit_html = f'<div class="card-fit">{fit}</div>' if fit else '<div></div>'
    return f"""
    <div class="card">
        {swatch(d['hex'])}
        <div class="card-main">
            <div class="card-name">{pname} {new_tag(d.get('new_2026', False))}</div>
            <div class="card-shade">{shade} · {CAT_KR[d['category']]} · {tone_tag(d['tone'])} {' '.join(season_tag(s) for s in d['seasons'])}</div>
            <div class="card-note">{d['note']}</div>
        </div>
        {fit_html}
    </div>
    """


def mini_info_html(pname: str, shade: str, d: dict) -> str:
    return f"""
    <div class="mini-row">
        {swatch(d['hex'])}
        <div class="mini-main">
            <div class="mini-title">
                <span>{pname} · {shade}</span>
                {tone_tag(d['tone'])}
                {''.join(season_tag(s) for s in d['seasons'])}
                {category_tag(d['category'])}
                {new_tag(d.get('new_2026', False))}
            </div>
            <div class="mini-note">{d['note']}</div>
        </div>
    </div>
    """


def product_names(category: Optional[str], include_discontinued: bool = True) -> List[str]:
    names = []
    for pname, shades in DB.items():
        any_ok = False
        for d in shades.values():
            if category and d["category"] != category:
                continue
            if include_discontinued or d["available"]:
                any_ok = True
                break
        if any_ok:
            names.append(pname)
    return sorted(names)


def shades_for_product(pname: str, include_discontinued: bool = True) -> List[str]:
    shades = []
    for shade, d in DB[pname].items():
        if include_discontinued or d["available"]:
            shades.append(shade)
    return list(shades)


def get_recs(tone: str, season: str, category: Optional[str] = None, only_new_2026: bool = False, limit: int = 8):
    primary, secondary = [], []
    for pname, shades in DB.items():
        for shade, d in shades.items():
            if not d["available"]:
                continue
            if category and d["category"] != category:
                continue
            if only_new_2026 and not d.get("new_2026", False):
                continue
            row = (pname, shade, d)
            if d["tone"] == tone and season in d["seasons"]:
                primary.append(row)
            elif d["tone"] == tone:
                secondary.append(row)
    return (primary + secondary)[:limit]


def run_analysis(good_list, bad_list, best_list):
    tone_score = chroma_score = value_score = total = 0.0

    def accumulate(items, weight):
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

    accumulate(good_list, 1.0)
    accumulate(best_list, 2.0)
    accumulate(bad_list, -1.4)

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

    return {"pc": pc, "tone": PC[pc]["tone"], "season": PC[pc]["season"]}


# -----------------------------
# UI widgets
# -----------------------------

def product_picker(prefix: str, include_disc: bool = True):
    cat_map = {"전체": None, "립": "lip", "블러셔": "blush", "섀도우": "shadow"}
    c1, c2 = st.columns([1.0, 2.0])
    with c1:
        cat_label = st.selectbox(
            "카테고리",
            list(cat_map.keys()),
            key=f"{prefix}_cat",
            label_visibility="collapsed",
        )
    category = cat_map[cat_label]

    with c2:
        pname = st.selectbox(
            "제품명",
            product_names(category, include_discontinued=include_disc),
            index=None,
            placeholder="제품명 선택",
            key=f"{prefix}_pname",
            label_visibility="collapsed",
        )
    if not pname:
        return None

    shade = st.selectbox(
        "호수",
        shades_for_product(pname, include_discontinued=include_disc),
        index=None,
        placeholder="호수(컬러) 선택",
        key=f"{prefix}_shade",
        label_visibility="collapsed",
    )
    if not shade:
        return None

    d = DB[pname][shade]
    st.markdown(mini_info_html(pname, shade, d), unsafe_allow_html=True)
    return (pname, shade)


# -----------------------------
# Tabs
# -----------------------------

def render_result(res):
    pc = res["pc"]
    info = PC[pc]
    result_class = "result-warm" if info["tone"] == "warm" else "result-cool"

    st.divider()
    st.markdown(
        f"""
        <div class="result-box {result_class}">
            <div class="result-title">{info['emoji']} {pc}</div>
            <div class="result-desc">{info['desc']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
        cat_label = st.radio(
            "추천 카테고리",
            ["전체", "립", "블러셔", "섀도우"],
            horizontal=True,
            label_visibility="collapsed",
            key="result_cat",
        )
    with f2:
        new_only = st.checkbox("2026 NEW만 보기", key="result_new_only")

    cat_map = {"전체": None, "립": "lip", "블러셔": "blush", "섀도우": "shadow"}
    recs = get_recs(res["tone"], res["season"], category=cat_map[cat_label], only_new_2026=new_only, limit=8)
    if not recs:
        st.info("조건에 맞는 추천 제품이 없어요.")
        return

    cols = st.columns(2)
    for i, (pname, shade, d) in enumerate(recs):
        fit = "완벽 매칭" if res["season"] in d["seasons"] else "같은 톤 추천"
        with cols[i % 2]:
            st.markdown(card_html(pname, shade, d, fit), unsafe_allow_html=True)


def tab_analysis():
    st.markdown('<div class="section-title">퍼스널 컬러 분석</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">실제 판매 중인 제품과 실제 호수명으로 입력할 수 있게 정리해두었어요. 잘 맞았던 제품 1개만 있어도 분석은 가능하고, 안 맞았던 제품과 반응 좋았던 제품은 선택 입력이에요.</div>',
        unsafe_allow_html=True,
    )

    with st.expander("입력 기준 보기"):
        st.markdown(
            """
- **잘 맞았던 제품**: 혼자 봐도 안정감 있고 피부가 좋아 보였던 제품
- **안 맞았던 제품**: 얼굴이 칙칙하거나 뜬다고 느꼈던 제품
- **반응 좋았던 제품**: 주변 반응이 특히 좋았던 제품
            """
        )

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown('<div class="panel"><div class="panel-head"><span class="panel-icon">👍</span><span>잘 맞았던 제품</span></div><div class="panel-sub">필수 · 1개 이상</div>', unsafe_allow_html=True)
        g1 = product_picker("g1")
        st.divider()
        g2 = product_picker("g2")
        st.divider()
        g3 = product_picker("g3")
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="panel"><div class="panel-head"><span class="panel-icon">👎</span><span>안 맞았던 제품</span></div><div class="panel-sub">선택 · 0~3개</div>', unsafe_allow_html=True)
        b1 = product_picker("b1")
        st.divider()
        b2 = product_picker("b2")
        st.divider()
        b3 = product_picker("b3")
        st.markdown('</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="panel"><div class="panel-head"><span class="panel-icon">✨</span><span>반응 좋았던 제품</span></div><div class="panel-sub">선택 · 0~3개</div>', unsafe_allow_html=True)
        t1 = product_picker("t1")
        st.divider()
        t2 = product_picker("t2")
        st.divider()
        t3 = product_picker("t3")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    _, center, _ = st.columns([1.3, 1.5, 1.3])
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

    if st.session_state.get("result"):
        render_result(st.session_state["result"])


def tab_pairing():
    st.markdown('<div class="section-title">연계 추천</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">립을 찾는 사람에게 블러셔와 섀도우까지 자연스럽게 이어지는 조합을 보여줘요. 분석 결과가 있으면 자동으로 맞춰집니다.</div>',
        unsafe_allow_html=True,
    )

    pc_list = list(PC.keys())
    default_pc = st.session_state.get("result", {}).get("pc", pc_list[0])
    selected_pc = st.selectbox("퍼스널 컬러", pc_list, index=pc_list.index(default_pc))
    info = PC[selected_pc]

    st.markdown(
        f'<div class="info-band"><b>{info["emoji"]} {selected_pc}</b><small>{info["desc"]}</small></div>',
        unsafe_allow_html=True,
    )

    st.markdown("### 립 추천")
    lips = get_recs(info["tone"], info["season"], category="lip", limit=6)
    cols = st.columns(2)
    for i, (pname, shade, d) in enumerate(lips):
        with cols[i % 2]:
            st.markdown(card_html(pname, shade, d), unsafe_allow_html=True)

    st.markdown("### 블러셔 연결 추천")
    blushes = [(pn, sh, DB[pn][sh]) for pn, sh in PAIRING.get((info["season"], "blush"), [])]
    cols = st.columns(2)
    for i, (pname, shade, d) in enumerate(blushes):
        with cols[i % 2]:
            st.markdown(card_html(pname, shade, d), unsafe_allow_html=True)

    st.markdown("### 섀도우 연결 추천")
    shadows = [(pn, sh, DB[pn][sh]) for pn, sh in PAIRING.get((info["season"], "shadow"), [])]
    cols = st.columns(2)
    for i, (pname, shade, d) in enumerate(shadows):
        with cols[i % 2]:
            st.markdown(card_html(pname, shade, d), unsafe_allow_html=True)


def tab_browse():
    st.markdown('<div class="section-title">제품 탐색</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">실제 제품명과 실제 호수명으로 정리한 목록이에요. 2026 NEW 표시가 붙은 항목만 따로 볼 수도 있어요.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        cat_label = st.selectbox("카테고리", ["전체", "립", "블러셔", "섀도우"])
    with c2:
        tone_label = st.selectbox("톤", ["전체", "웜톤", "쿨톤"])
    with c3:
        new_only = st.checkbox("2026 NEW만 보기")

    cat_map = {"전체": None, "립": "lip", "블러셔": "blush", "섀도우": "shadow"}
    tone_map = {"전체": None, "웜톤": "warm", "쿨톤": "cool"}

    rows = []
    for pname, shades in DB.items():
        for shade, d in shades.items():
            if cat_map[cat_label] and d["category"] != cat_map[cat_label]:
                continue
            if tone_map[tone_label] and d["tone"] != tone_map[tone_label]:
                continue
            if new_only and not d.get("new_2026", False):
                continue
            rows.append((pname, shade, d))

    st.caption(f"총 {len(rows)}개 항목")
    cols = st.columns(2)
    for i, (pname, shade, d) in enumerate(rows):
        with cols[i % 2]:
            st.markdown(card_html(pname, shade, d), unsafe_allow_html=True)


def tab_guide():
    st.markdown('<div class="section-title">컬러 가이드</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">8개 세부톤의 분위기를 빠르게 확인할 수 있게 정리했어요.</div>',
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


def main():
    if "result" not in st.session_state:
        st.session_state["result"] = None

    st.markdown(
        """
        <div class="hero-wrap">
            <div class="hero-kicker">🌼 TONEME · curated for Korea</div>
            <div class="hero-title">실사용 기준으로 고르는 <span class="accent">퍼스널 컬러 추천</span></div>
            <div class="hero-sub">
                제품명 먼저 고르고, 그다음 실제 호수를 고르는 흐름으로 정리했어요. 화면 안 아이콘·태그·칩 정렬도 다시 맞춰서,
                전체적으로 한 줄 한 줄이 고르게 보이도록 다듬은 버전입니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
        '<div class="footer">TONEME · 실제 판매 페이지에서 확인한 제품명/호수 기준으로 재정리 · NEW 표시는 2026 기준 확인된 항목에만 표시</div>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
