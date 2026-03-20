import streamlit as st

st.set_page_config(
    page_title="TONEME · 퍼스널 컬러 뷰티",
    page_icon="🌼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,500;1,400&family=Noto+Sans+KR:wght@300;400;500;700&display=swap');

:root {
    --bg:       #FEFAE8;
    --surface:  #FFFDF2;
    --border:   #DFCF00;
    --accent:   #7A5C00;   /* 진한 황갈색 — 개나리 위 최고 대비 */
    --text:     #1A1200;
    --sub:      #4A3C00;
    --muted:    #6B5400;
    --cool-bg:  #E8F0FF;
    --cool-bd:  #4060B0;
    --cool-txt: #0A1040;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: var(--bg) !important;
    font-family: 'Noto Sans KR', sans-serif;
    color: var(--text);
}
[data-testid="stSidebar"]  { display: none; }
.block-container { padding: 2.5rem 3rem 6rem !important; max-width: 1100px !important; }

/* HERO */
.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3rem; font-weight: 300; letter-spacing: 0.08em;
    color: var(--text); line-height: 1; text-transform: uppercase;
}
.hero-title em { font-style: italic; color: var(--accent); }
.hero-bar { width: 44px; height: 2px; background: var(--accent); margin: 0.6rem 0 0.65rem; border-radius: 2px; }
.hero-sub { font-size: 0.79rem; color: var(--sub); letter-spacing: 0.04em; margin-bottom: 2rem; font-weight: 500; }

/* TABS */
.stTabs [data-baseweb="tab-list"] {
    gap: 0; background: transparent; border-bottom: 2px solid var(--border);
}
.stTabs [data-baseweb="tab"] {
    font-size: 0.85rem; font-weight: 500; color: var(--sub);
    padding: 0.55rem 1.3rem; border-radius: 0; background: transparent; border: none;
}
.stTabs [aria-selected="true"] {
    color: var(--accent) !important; background: transparent !important;
    border-bottom: 2.5px solid var(--accent) !important; font-weight: 700 !important;
}

/* SECTION */
.sec-head { font-size: 1.1rem; font-weight: 700; color: var(--text); margin-bottom: 0.2rem; }
.sec-sub  { font-size: 0.81rem; color: var(--sub); line-height: 1.7; margin-bottom: 1.2rem; }
.col-label {
    font-size: 0.76rem; font-weight: 700; letter-spacing: 0.03em;
    color: var(--text); padding-bottom: 0.55rem;
    border-bottom: 1.5px solid var(--border); margin-bottom: 0.85rem;
}

/* SELECTBOX — 라벨 숨김, 깔끔한 테두리 */
.stSelectbox label { display: none !important; }
.stSelectbox > div > div {
    border-radius: 9px !important; border-color: var(--border) !important;
    font-size: 0.85rem !important; background: var(--surface) !important;
    color: var(--text) !important; font-weight: 500 !important;
}

/* 선택 후 미니 정보 줄 */
.mini-info {
    display: flex; align-items: center; gap: 0.45rem;
    padding: 0.42rem 0.75rem;
    background: #FFFBE0; border: 1.5px solid var(--accent);
    border-radius: 8px; margin-top: 0.28rem;
    font-size: 0.75rem; color: var(--sub); font-weight: 500;
    line-height: 1.4;
}
.mini-dot { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; border: 1.5px solid rgba(0,0,0,0.15); }

/* TAGS — 개나리 배경 위 가독성 우선 */
.tag { display: inline-block; padding: 0.14rem 0.58rem; border-radius: 100px; font-size: 0.68rem; font-weight: 600; margin: 0.04rem; vertical-align: middle; }
.t-warm   { background: #5C3800; color: #FFE5A8; }
.t-cool   { background: #1A3070; color: #C8DDFF; }
.t-spring { background: #7A3000; color: #FFD8B0; }
.t-summer { background: #282070; color: #C8C8FF; }
.t-autumn { background: #623000; color: #FFD8A0; }
.t-winter { background: #1E2870; color: #C0CCFF; }
.t-cat    { background: #3A2E00; color: #FFE89A; }
.t-disc   { background: #555;    color: #EEE;   }
.t-new    { background: #0D4A28; color: #A8FFD0; }   /* 2026 NEW — 다크그린 배경 */

/* DOT */
.dot { display: inline-block; border-radius: 50%; border: 1.5px solid rgba(0,0,0,0.15); vertical-align: middle; flex-shrink: 0; }

/* PRODUCT CARD */
.pcard {
    display: flex; align-items: flex-start; gap: 0.65rem;
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 11px; padding: 0.78rem 0.95rem; margin-bottom: 0.45rem;
}
.pcard > .dot { margin-top: 0.15rem; flex-shrink: 0; }
.pcard-info { flex: 1; min-width: 0; }
.pcard-name  { font-weight: 600; font-size: 0.85rem; line-height: 1.35; color: var(--text); }
.pcard-shade { font-size: 0.76rem; color: var(--muted); font-weight: 500; margin-top: 0.1rem; }
.pcard-note  { font-size: 0.71rem; color: var(--sub); margin-top: 0.08rem; line-height: 1.4; }
.pcard-fit   { font-size: 0.68rem; color: var(--accent); white-space: nowrap; font-weight: 600; margin-top: 0.1rem; flex-shrink: 0; }

/* RESULT BOX */
.rbox-warm {
    background: linear-gradient(135deg, #FFF9D0, #FFE650);
    border: 2px solid #C09000; border-radius: 16px;
    padding: 1.7rem 2rem; margin-bottom: 1.2rem;
}
.rbox-cool {
    background: linear-gradient(135deg, #E8F0FF, #C0D4FF);
    border: 2px solid var(--cool-bd); border-radius: 16px;
    padding: 1.7rem 2rem; margin-bottom: 1.2rem;
}
.rbox-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2rem; font-weight: 500; line-height: 1.2; margin-bottom: 0.4rem;
}
.rbox-warm .rbox-title { color: #1A1000; }
.rbox-cool .rbox-title { color: #060C30; }
.rbox-warm .rbox-desc  { font-size: 0.87rem; color: #2A1E00; line-height: 1.75; font-weight: 400; }
.rbox-cool .rbox-desc  { font-size: 0.87rem; color: #101840; line-height: 1.75; font-weight: 400; }

/* INFO BAND */
.info-band { border-radius: 11px; padding: 0.9rem 1.2rem; margin-bottom: 1rem; }
.ib-warm   { background: linear-gradient(135deg, #FFF9D0, #FFE650); border: 1.5px solid #C09000; }
.ib-cool   { background: linear-gradient(135deg, #E8F0FF, #C0D4FF); border: 1.5px solid var(--cool-bd); }
.ib-warm b, .ib-warm small { color: #1A1000 !important; }
.ib-cool b, .ib-cool small { color: #060C30 !important; }

/* BUTTON */
.stButton > button {
    background: var(--accent) !important; color: #FFFBE0 !important;
    border: none !important; border-radius: 9px !important;
    padding: 0.62rem 1.8rem !important; font-size: 0.86rem !important;
    font-weight: 700 !important; width: 100% !important; letter-spacing: 0.02em !important;
}
.stButton > button:hover { filter: brightness(1.12) !important; }

/* RADIO / CHECKBOX */
.stRadio > div { gap: 0.4rem !important; }
.stRadio label, .stCheckbox label { color: var(--text) !important; font-weight: 500 !important; font-size: 0.83rem !important; }

/* EXPANDER */
details summary { font-size: 0.83rem !important; color: var(--text) !important; font-weight: 600 !important; }

hr { border-color: var(--border) !important; margin: 1.3rem 0 !important; }
.stSuccess, .stWarning, .stInfo { border-radius: 10px !important; font-size: 0.84rem !important; }
.footer { text-align: center; font-size: 0.72rem; color: var(--muted); padding: 1.5rem 0 2rem; font-weight: 500; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# DB  — 실제 출시 제품 기반, 검증된 데이터
# year=2026 인 경우만 "NEW" 뱃지 표시
# ══════════════════════════════════════════════════════════════
def p(tone, season, chroma, value, category, hex_col, avail, note, year=None):
    return dict(tone=tone, season=season, chroma=chroma, value=value,
                category=category, hex=hex_col, avail=avail, note=note, year=year)

DB = {
    # ═══ LIP ════════════════════════════════════════════════
    "롬앤 쥬시 래스팅 틴트": {
        "06 피그피그":         p("cool",["summer","winter"],  2,2,"lip","#C47090",True, "물광 마감 뮤트 로즈"),
        "07 쥬쥬브":           p("warm",["spring","autumn"],  3,2,"lip","#C45858",True, "생기 있는 레드베리"),
        "08 애플브라운":       p("warm",["autumn"],           2,2,"lip","#A85040",True, "깊은 테라코타 브라운"),
        "17 딸기우유":         p("cool",["spring","summer"],  2,3,"lip","#D88090",True, "투명감 딸기밀크 핑크"),
        "20 레드벨벳":         p("cool",["winter"],           4,2,"lip","#B83040",True, "딥레드, 강렬한 존재감"),
        "23 피칸브라운":       p("warm",["autumn"],           1,2,"lip","#885040",True, "일상 내추럴 누드브라운"),
        "25 스트로베리초크":   p("cool",["summer"],           2,3,"lip","#D07890",True, "차분한 쿨 딸기핑크"),
        "28 핑크핑크":         p("cool",["summer"],           3,3,"lip","#E070A8",True, "발랄한 쿨핑크"),
        "29 브릭베이지":       p("warm",["autumn"],           2,2,"lip","#A06850",True, "웜 브릭베이지"),
    },
    "에뛰드 픽싱 틴트": {
        "03 멜로우피치":       p("warm",["spring"],           2,3,"lip","#E09068",True, "복숭아빛 코랄"),
        "05 미드나잇모브":     p("cool",["winter","summer"],  2,2,"lip","#987090",True, "보랏빛 뮤트 핑크"),
        "06 소프트월넛":       p("warm",["autumn"],           1,2,"lip","#906858",True, "웜 누드, 피부 밀착"),
        "08 베리핑크":         p("cool",["summer"],           3,3,"lip","#C870A0",True, "선명 핑크"),
        "11 진저브라운":       p("warm",["autumn"],           2,2,"lip","#8A5040",False,"깊은 진저브라운 ★단종"),
    },
    "페리페라 잉크 무드 글로이 틴트": {
        "01 쿨오프코랄":       p("warm",["spring"],           3,3,"lip","#E07860",True, "밝은 코랄오렌지"),
        "03 맘찍로즈":         p("cool",["summer"],           2,3,"lip","#D088A0",True, "뮤트 로즈핑크"),
        "06 초코브릭":         p("warm",["autumn"],           2,2,"lip","#8A4838",True, "초콜릿 브릭 레드"),
        "09 코랄프레쉬":       p("warm",["spring"],           3,3,"lip","#E06848",True, "생생한 코랄"),
        "14 누드로즈우드":     p("cool",["summer","winter"],  1,2,"lip","#A87888",True, "쿨 누드로즈우드"),
    },
    "클리오 쉬폰 블러 틴트": {
        "03 피치퍼즐":         p("warm",["spring","autumn"],  2,3,"lip","#D89080",True, "스모키 피치"),
        "05 코랄":             p("warm",["spring"],           2,3,"lip","#DC7060",True, "클래식 코랄"),
        "07 로즈":             p("cool",["summer","winter"],  3,3,"lip","#C86890",True, "청량한 로즈"),
        "09 레드브릭":         p("warm",["autumn"],           3,2,"lip","#A03830",True, "벽돌빛 레드"),
    },
    "3CE 벨벳 립 틴트": {
        "파우더핑크":          p("cool",["summer"],           1,3,"lip","#D8A8B8",True, "파우더리 쿨핑크 누드"),
        "두메":                p("cool",["winter"],           2,2,"lip","#B06888",True, "뮤트 로즈브라운, 겨울 정석"),
        "러스티로즈":          p("cool",["summer","winter"],  2,2,"lip","#A87080",True, "빈티지 로즈"),
        "퍼스트데이트":        p("warm",["spring"],           2,3,"lip","#E09898",True, "밝은 베이비핑크"),
        "누드플럼":            p("cool",["winter"],           2,1,"lip","#7A5068",True, "딥 누드 플럼"),
    },
    "맥 리프스틱": {
        "Whirl":               p("warm",["autumn"],           1,2,"lip","#906060",True, "국민 누드브라운, 가을 완벽템"),
        "Ruby Woo":            p("cool",["winter"],           4,2,"lip","#C02030",True, "클래식 블루베이스 레드"),
        "Velvet Teddy":        p("warm",["autumn"],           1,2,"lip","#8A5848",True, "따뜻한 뮤트 누드"),
        "Brave":               p("warm",["spring","autumn"],  1,3,"lip","#C09080",True, "피치 누드"),
        "Flat Out Fabulous":   p("cool",["winter"],           3,1,"lip","#803060",True, "다크 플럼"),
    },
    "롬앤 한올한올 뉴립스틱": {
        "04 베어릭":           p("warm",["autumn"],           1,2,"lip","#9A6858",True, "워터리 피부색 누드"),
        "07 코럴하이":         p("warm",["spring"],           3,3,"lip","#E07060",True, "코랄 레드"),
        "11 스트로베리파우더": p("cool",["summer"],           2,3,"lip","#D08898",True, "파우더리 딸기 핑크"),
        "14 라즈베리무드":     p("cool",["winter"],           3,2,"lip","#B04870",True, "선명한 라즈베리"),
        "17 코코넛누드":       p("warm",["spring","autumn"],  1,3,"lip","#C8A080",True, "밀크누드, 일상용"),
    },
    "헤라 립 컨디셔닝 누드밤 (2025 리뉴얼)": {
        "01 쉬어누드":         p("warm",["spring","autumn"],  1,3,"lip","#D8B090",True, "촉촉한 웜 누드밤"),
        "02 로즈누드":         p("cool",["summer"],           1,3,"lip","#C8A0A8",True, "촉촉한 쿨 로즈누드"),
        "03 코랄누드":         p("warm",["spring"],           2,3,"lip","#D89878",True, "생기 있는 코랄 누드"),
    },
    # 2026 실제 출시 제품
    "에스쁘아 꾸뛰르 립틴트 글레이즈 (로젤라이트 컬렉션)": {
        "로젤라이트":          p("warm",["spring","autumn"],  2,3,"lip","#D09088",True, "티로즈+골드 쉬머, 2026 한정", 2026),
    },
    "NARS 에프터글로우 립밤": {
        "돌체비타":            p("warm",["spring","autumn"],  1,3,"lip","#C89080",True, "버터 텍스처, 투명 광채", 2026),
        "오가즘":              p("warm",["spring","summer"],  2,3,"lip","#D09088",True, "골드쉬머 피치 립밤", 2026),
        "미스에듀케이션":      p("cool",["summer","winter"],  1,2,"lip","#B08088",True, "쿨 뮤트 핑크 립밤", 2026),
    },
    "롬앤 글래시 워터 틴트": {
        "01 글래시피치":       p("warm",["spring"],           2,3,"lip","#E8A888",True, "젤리 광택 피치 웜", 2026),
        "02 글래시로즈":       p("cool",["summer","winter"],  2,3,"lip","#D088A8",True, "젤리 광택 쿨로즈", 2026),
        "03 글래시코랄":       p("warm",["spring","autumn"],  3,3,"lip","#E87858",True, "젤리 광택 코랄 웜", 2026),
        "04 글래시베리":       p("cool",["winter"],           3,2,"lip","#A84878",True, "젤리 광택 딥베리 쿨", 2026),
    },

    # ═══ BLUSH ══════════════════════════════════════════════
    "롬앤 베러 댄 치크": {
        "피치칩":              p("warm",["spring","autumn"],  2,3,"blush","#E8A878",True, "황금 피치, 웜 피부 생기"),
        "스트로베리밀크":      p("cool",["summer"],           2,3,"blush","#D898A8",True, "딸기우유빛 쿨 핑크"),
        "코랄리프":            p("warm",["spring"],           3,3,"blush","#E89070",True, "생생한 코랄"),
        "쿨로즈":              p("cool",["winter","summer"],  2,2,"blush","#C880A0",True, "블루베이스 쿨 로즈"),
        "누디피치":            p("warm",["autumn"],           1,2,"blush","#D0988A",True, "웜 누디 피치"),
    },
    "에뛰드 러블리 쿠키 블러셔": {
        "1호 피치":            p("warm",["spring"],           2,3,"blush","#EDA880",True, "부드러운 피치"),
        "2호 핑크":            p("cool",["summer"],           2,3,"blush","#E0A0B8",True, "밝은 쿨핑크"),
        "3호 오렌지":          p("warm",["autumn","spring"],  3,3,"blush","#E89060",True, "선명한 오렌지"),
        "5호 베이지":          p("warm",["autumn"],           1,2,"blush","#C8A888",True, "내추럴 베이지 음영"),
    },
    "클리오 킬 커버 더 뉴 치크": {
        "02 다이닝로즈":       p("cool",["summer","winter"],  2,3,"blush","#D890A8",True, "뮤트 쿨 로즈"),
        "03 캐시미어":         p("warm",["autumn"],           1,2,"blush","#C8A090",True, "웜 캐시미어 베이지"),
        "05 보나피치":         p("warm",["spring","summer"],  2,3,"blush","#E8A890",True, "따뜻한 코랄피치"),
        "07 쿨모브":           p("cool",["winter"],           2,2,"blush","#B880A8",True, "딥 쿨모브"),
    },
    "NARS 블러쉬": {
        "오가즘":              p("warm",["spring","summer"],  2,3,"blush","#E09888",True, "골드쉬머 피치핑크, 국민템"),
        "딥트로트":            p("warm",["autumn"],           2,2,"blush","#C07860",True, "깊은 테라코타"),
        "카마수트라":          p("cool",["winter"],           3,2,"blush","#B86080",True, "딥 쿨로즈"),
        "부에노스아이레스":    p("cool",["summer"],           2,3,"blush","#D898B0",True, "소프트 쿨핑크"),
    },
    "페리페라 블러블러 페이스 블러셔": {
        "01 코코피치":         p("warm",["spring","autumn"],  2,3,"blush","#E0A080",True, "코코넛 피치"),
        "02 쿨로즈퍼지":       p("cool",["summer"],           2,3,"blush","#D8A0B8",True, "퍼지 쿨 로즈핑크"),
        "03 미드나잇플럼":     p("cool",["winter"],           3,2,"blush","#A06888",True, "딥 쿨 플럼"),
    },
    "헤라 센슈얼 파우더 블러셔": {
        "01 로즈코랄":         p("warm",["spring","summer"],  2,3,"blush","#E09888",True, "로즈코랄 쉬머"),
        "02 쿨핑크":           p("cool",["summer"],           2,3,"blush","#D898B8",True, "쿨핑크 쉬머"),
        "03 딥테라":           p("warm",["autumn"],           2,2,"blush","#B07060",True, "딥 테라코타 쉬머"),
        "04 뉴드로즈":         p("cool",["summer","winter"],  1,3,"blush","#C8A0B0",True, "뉴드 로즈 쉬머"),
    },
    "투쿨포스쿨 체크 체크 블러셔": {
        "01 코튼피치":         p("warm",["spring"],           2,3,"blush","#EDB090",True, "코튼 피치"),
        "02 플럼체크":         p("cool",["winter"],           2,2,"blush","#B07890",True, "플럼 쿨"),
    },
    # 2026 실제 출시
    "에스쁘아 스트로빙 하이라이터 (로젤라이트)": {
        "로젤라이트":          p("warm",["spring","summer"],  2,3,"blush","#E0C0A8",True, "로즈골드 쉬머 하이라이터", 2026),
    },
    "NARS 라지즈 블러쉬 (2026)": {
        "오가즘":              p("warm",["spring","summer"],  2,3,"blush","#E09888",True, "국민 블러셔 2026 리뉴얼", 2026),
        "미스에듀케이션":      p("cool",["summer","winter"],  2,3,"blush","#C898B0",True, "쿨 뮤트로즈 리뉴얼", 2026),
    },

    # ═══ SHADOW ═════════════════════════════════════════════
    "클리오 프로 아이 팔레트": {
        "03 앤틱핑크":         p("cool",["summer","winter"],  2,3,"shadow","#D8A8B8",True, "쿨톤 핑크 멀티"),
        "04 브라운브릭":       p("warm",["autumn"],           2,2,"shadow","#987060",True, "웜 브라운 전문"),
        "06 어텀테라":         p("warm",["autumn","spring"],  2,2,"shadow","#B07858",True, "테라코타 어텀"),
        "09 스모키쿨":         p("cool",["winter"],           2,1,"shadow","#706880",True, "쿨톤 스모키 전문"),
    },
    "에뛰드 플레이 컬러 아이즈": {
        "베어누드":            p("warm",["autumn","spring"],  1,3,"shadow","#C8B098",True, "웜 베이지 데일리"),
        "라즈베리초콜릿":      p("cool",["winter","summer"],  2,2,"shadow","#907880",True, "쿨 다크베리"),
        "핑크쉐이드":          p("cool",["summer"],           2,3,"shadow","#D8A8B8",True, "소프트 쿨핑크"),
        "브라운토피":          p("warm",["autumn"],           2,2,"shadow","#987060",False,"웜 토피브라운 ★단종"),
    },
    "에뛰드 플레이 멀티 아이즈": {
        "01 로즈브라운":       p("warm",["autumn","spring"],  2,2,"shadow","#C09878",True, "로즈브라운 웜 멀티"),
        "02 쿨핑크모브":       p("cool",["summer","winter"],  2,3,"shadow","#C090B0",True, "쿨 핑크모브 멀티"),
    },
    "어반디케이 네이키드 팔레트": {
        "NAKED3":              p("cool",["summer","winter"],  2,3,"shadow","#C090A0",True, "쿨 로즈 뉴트럴 — 국내 온라인 구매가능"),
        "NAKED RELOADED":      p("warm",["autumn","spring"],  2,2,"shadow","#B09070",True, "웜 뉴트럴 — 국내 온라인 구매가능"),
    },
    "맥 아이섀도우 단품": {
        "코퍼스파크":          p("warm",["autumn"],           3,2,"shadow","#C07840",True, "쉬머 구리빛"),
        "브라운다운":          p("warm",["autumn","spring"],  2,2,"shadow","#906050",True, "클래식 웜 브라운"),
        "스노우화이트":        p("cool",["winter","summer"],  1,4,"shadow","#E8E0E8",True, "쿨 하이라이트 섀도우"),
    },
    "롬앤 한올한올 아이섀도우": {
        "03 로즈핑크":         p("cool",["summer"],           2,3,"shadow","#D890A8",True, "맑은 쿨 로즈"),
        "06 코퍼브라운":       p("warm",["autumn"],           2,2,"shadow","#A07058",True, "구리빛 브라운"),
        "10 테라핑크":         p("warm",["spring"],           2,3,"shadow","#D89080",True, "코랄핑크 섀도우"),
        "13 스모키그레이":     p("cool",["winter"],           1,2,"shadow","#888098",True, "쿨 스모키 그레이"),
    },
    "페리페라 인크 더 아이섀도우 팔레트": {
        "01 웜어스":           p("warm",["autumn"],           2,2,"shadow","#A07858",True, "어스톤 웜 팔레트"),
        "02 쿨로즈":           p("cool",["summer","winter"],  2,3,"shadow","#C090A8",True, "쿨 로즈 팔레트"),
        "03 코랄핑크":         p("warm",["spring"],           3,3,"shadow","#E09078",True, "코랄핑크 팔레트"),
    },
    "투쿨포스쿨 아트클래스 팔레트": {
        "웜누드":              p("warm",["spring","autumn"],  1,3,"shadow","#C8A888",True, "웜 누드 아트 팔레트"),
        "쿨모브":              p("cool",["summer","winter"],  2,2,"shadow","#9888A8",True, "쿨 모브 아트 팔레트"),
    },
    "힌스 뉴 뎁스 싱글 섀도우": {
        "리플렉션":            p("cool",["summer","winter"],  1,4,"shadow","#D0C8D8",True, "쿨 하이라이트 반사"),
        "비 마이 얼루어":      p("warm",["spring","autumn"],  2,3,"shadow","#C0A880",True, "웜 골드 쉬머"),
        "어니스티":            p("warm",["autumn"],           2,2,"shadow","#9A7858",True, "웜 브라운 매트"),
        "얼루어 인 모션":      p("cool",["winter"],           2,2,"shadow","#8878A0",True, "쿨 모브 글리터"),
    },

    # ═══ BASE ═══════════════════════════════════════════════
    "롬앤 그램 글로잉 사틴 파운데이션": {
        "13N 아이보리":        p("warm",["spring","autumn"],  1,3,"base","#E8C8A8",True, "웜 밝은 피부"),
        "21N 라이트베이지":    p("warm",["autumn"],           1,3,"base","#DEC0A0",True, "웜 자연 피부"),
        "23C 쿨내추럴":        p("cool",["summer"],           1,3,"base","#D8C0B0",True, "쿨 밝은 피부"),
        "25C 쿨베이지":        p("cool",["winter"],           1,2,"base","#D0B8A8",True, "쿨 중간 피부"),
    },
    "에스쁘아 프로 태일러 파운데이션": {
        "1W 아이보리":         p("warm",["spring","autumn"],  1,3,"base","#EAD0B0",True, "웜 피부, 자연 밀착"),
        "2N 내추럴":           p("warm",["autumn"],           1,3,"base","#DEC0A0",True, "웜 중간 피부"),
        "3C 쿨베이지":         p("cool",["summer","winter"],  1,3,"base","#D0B8A8",True, "쿨 베이지"),
    },
    "클리오 킬 커버 파운웨어 쿠션": {
        "1W 워너비아이보리":   p("warm",["spring","autumn"],  1,3,"base","#EED0A8",True, "웜 아이보리 쿠션"),
        "2N 내추럴베이지":     p("warm",["autumn"],           1,3,"base","#E0C0A0",True, "웜 내추럴 쿠션"),
        "3C 쿨샌드":           p("cool",["summer","winter"],  1,3,"base","#D8C0B0",True, "쿨 샌드 쿠션"),
    },
    "겔랑 메쉬 쿠션 (2026)": {
        "송혜교 에디션 W00":   p("warm",["spring","autumn"],  1,3,"base","#EAD0A8",True, "은은한 광채 웜 쿠션", 2026),
        "C00 쿨아이보리":      p("cool",["summer","winter"],  1,3,"base","#DCCAB8",True, "은은한 광채 쿨 쿠션", 2026),
    },
    "에스쁘아 비글로우 파운데이션 (로젤라이트)": {
        "21N 라이트베이지":    p("warm",["spring","autumn"],  1,3,"base","#EAD0B0",True, "광채 웜 파운데이션", 2026),
        "23C 쿨내추럴":        p("cool",["summer","winter"],  1,3,"base","#D8C0B0",True, "광채 쿨 파운데이션", 2026),
    },
}

PC = {
    "봄 라이트 웜":   dict(tone="warm",season="spring",emoji="🌸",kw=["맑음","생기","복숭아","산뜻 코랄"],      desc="피부가 밝고 투명감이 있어요. 밝고 산뜻한 코랄·피치 계열이 잘 어울려요.",               best=["코랄","피치","살구","밝은 오렌지","라이트 브라운"],       avoid=["쿨 로즈","버건디","딥 퍼플","그레이"],  bg="linear-gradient(135deg,#FFF9D0,#FFE650)",bd="#B09000"),
    "봄 비비드 웜":   dict(tone="warm",season="spring",emoji="🌺",kw=["선명함","활기","코랄레드","오렌지"],      desc="맑고 선명한 컬러가 피부에 생기를 더해요. 비비드 코랄~레드가 특히 잘 어울려요.",            best=["코랄레드","오렌지레드","밝은 핑크"],                       avoid=["뮤트 컬러","다크 브라운","그레이"],     bg="linear-gradient(135deg,#FFF5C0,#FFE040)",bd="#A08000"),
    "가을 딥 웜":     dict(tone="warm",season="autumn",emoji="🍂",kw=["깊이","테라코타","어스톤","내추럴"],      desc="황금빛이 도는 깊고 풍부한 웜톤이에요. 테라코타·브릭·카멜이 완벽하게 어울려요.",             best=["테라코타","브릭레드","머스타드","카멜","올리브"],           avoid=["형광","네온","아이시 컬러"],             bg="linear-gradient(135deg,#FFF3B0,#FFD820)",bd="#907000"),
    "가을 뮤트 웜":   dict(tone="warm",season="autumn",emoji="🌾",kw=["차분함","뮤트","누드","내추럴"],         desc="채도가 낮고 부드러운 웜톤이에요. 뮤트한 브라운~누드 계열이 자연스러워요.",                   best=["카멜누드","웜베이지","머스타드뮤트","로즈브라운"],         avoid=["비비드","형광","쿨 핑크"],              bg="linear-gradient(135deg,#FFF8C8,#FFE850)",bd="#A09000"),
    "여름 라이트 쿨": dict(tone="cool",season="summer",emoji="🌊",kw=["부드러움","로맨틱","파스텔","파우더리"], desc="밝고 부드러운 쿨톤이에요. 파스텔 핑크·라벤더·뮤트 로즈가 우아하게 어울려요.",                best=["파스텔핑크","라벤더","소프트 로즈"],                       avoid=["오렌지","옐로우","골드 쉬머"],          bg="linear-gradient(135deg,#E8F0FF,#C0D4FF)",bd="#4060B0"),
    "여름 뮤트 쿨":   dict(tone="cool",season="summer",emoji="🩵",kw=["차분함","뮤트","로즈브라운","그레이시"], desc="채도가 낮고 세련된 쿨톤이에요. 뮤트 로즈·그레이핑크 계열이 지적으로 어울려요.",               best=["뮤트 로즈","그레이핑크","라이트 퍼플"],                   avoid=["오렌지","테라코타","골드"],             bg="linear-gradient(135deg,#E0EAFF,#B8CEFF)",bd="#3858B0"),
    "겨울 딥 쿨":     dict(tone="cool",season="winter",emoji="❄️",kw=["선명함","대비","딥레드","플럼"],         desc="선명하고 강한 쿨톤이에요. 딥레드·플럼·버건디가 드라마틱하게 어울려요.",                      best=["딥레드","플럼","버건디","쿨 핑크"],                        avoid=["오렌지","코랄","웜 브라운","베이지"],   bg="linear-gradient(135deg,#D8E4FF,#A8C0FF)",bd="#3050B8"),
    "겨울 비비드 쿨": dict(tone="cool",season="winter",emoji="💙",kw=["대담함","비비드","블루베이스","강렬함"], desc="강렬하고 비비드한 쿨톤이에요. 블루베이스 레드·선명한 핑크가 빛나요.",                          best=["블루베이스 레드","비비드 핑크","퓨어 블랙","퓨어 화이트"], avoid=["파스텔","피치","코랄","웜 브라운"],     bg="linear-gradient(135deg,#D0DCFF,#98B4FF)",bd="#2848B8"),
}

PAIRING = {
    ("spring","blush"):  [("롬앤 베러 댄 치크","코랄리프"),("에뛰드 러블리 쿠키 블러셔","1호 피치"),("NARS 블러쉬","오가즘"),("헤라 센슈얼 파우더 블러셔","01 로즈코랄")],
    ("spring","shadow"): [("클리오 프로 아이 팔레트","06 어텀테라"),("에뛰드 플레이 컬러 아이즈","베어누드"),("페리페라 인크 더 아이섀도우 팔레트","03 코랄핑크"),("롬앤 한올한올 아이섀도우","10 테라핑크")],
    ("autumn","blush"):  [("NARS 블러쉬","딥트로트"),("클리오 킬 커버 더 뉴 치크","03 캐시미어"),("페리페라 블러블러 페이스 블러셔","01 코코피치"),("헤라 센슈얼 파우더 블러셔","03 딥테라")],
    ("autumn","shadow"): [("클리오 프로 아이 팔레트","04 브라운브릭"),("어반디케이 네이키드 팔레트","NAKED RELOADED"),("맥 아이섀도우 단품","코퍼스파크"),("페리페라 인크 더 아이섀도우 팔레트","01 웜어스")],
    ("summer","blush"):  [("롬앤 베러 댄 치크","스트로베리밀크"),("에뛰드 러블리 쿠키 블러셔","2호 핑크"),("NARS 블러쉬","부에노스아이레스"),("투쿨포스쿨 체크 체크 블러셔","02 플럼체크")],
    ("summer","shadow"): [("클리오 프로 아이 팔레트","03 앤틱핑크"),("에뛰드 플레이 컬러 아이즈","핑크쉐이드"),("어반디케이 네이키드 팔레트","NAKED3"),("페리페라 인크 더 아이섀도우 팔레트","02 쿨로즈")],
    ("winter","blush"):  [("NARS 블러쉬","카마수트라"),("롬앤 베러 댄 치크","쿨로즈"),("페리페라 블러블러 페이스 블러셔","03 미드나잇플럼"),("클리오 킬 커버 더 뉴 치크","07 쿨모브")],
    ("winter","shadow"): [("클리오 프로 아이 팔레트","09 스모키쿨"),("어반디케이 네이키드 팔레트","NAKED3"),("투쿨포스쿨 아트클래스 팔레트","쿨모브"),("힌스 뉴 뎁스 싱글 섀도우","얼루어 인 모션")],
}

CAT_KR = {"lip":"립","blush":"블러셔","shadow":"섀도우","base":"베이스"}
SEA_KR = {"spring":"봄 웜","autumn":"가을 웜","summer":"여름 쿨","winter":"겨울 쿨"}

def new_tag():
    return '<span class="tag t-new">2026 NEW</span>'

def dot_html(hex_col, size=16):
    return f'<span class="dot" style="width:{size}px;height:{size}px;background:{hex_col};"></span>'

def tag_html(t, cls):
    return f'<span class="tag {cls}">{t}</span>'

def tone_tag(t):
    return tag_html("🌞 웜톤" if t=="warm" else "❄️ 쿨톤", f"t-{t}")

def sea_tag(s):
    return tag_html(SEA_KR.get(s,""), f"t-{s}")

def pcard_html(pname, shade, d, fit=""):
    nt = (" " + new_tag()) if d.get("year")==2026 else ""
    disc = " <span class='tag t-disc'>단종</span>" if not d["avail"] else ""
    fp = f'<div class="pcard-fit">{fit}</div>' if fit else ""
    return f"""
<div class="pcard">
    {dot_html(d['hex'],20)}
    <div class="pcard-info">
        <div class="pcard-name">{pname}{disc}{nt}</div>
        <div class="pcard-shade">{shade} · {CAT_KR.get(d['category'],'')}</div>
        <div class="pcard-note">{d['note']}</div>
    </div>{fp}
</div>"""


def run_analysis(good_list, bad_list, best_list):
    ts=cs=vs=wt=0.0
    def acc(items, w):
        nonlocal ts,cs,vs,wt
        for item in items:
            if not item: continue
            pn,sh=item; d=DB[pn][sh]
            ts+=(1 if d["tone"]=="warm" else -1)*w
            cs+=d["chroma"]*w; vs+=d["value"]*w; wt+=abs(w)
    acc(good_list,1.0); acc(best_list,2.0); acc(bad_list,-1.5)
    if wt==0: return None
    ac,av=cs/wt,vs/wt
    if ts>0:
        pc=("봄 비비드 웜" if ac>=2.5 else "봄 라이트 웜") if av>=2.8 \
        else("가을 딥 웜"  if ac>=2.0 else "가을 뮤트 웜")
    else:
        pc=("여름 라이트 쿨" if ac>=2.3 else "여름 뮤트 쿨") if av>=2.8 \
        else("겨울 비비드 쿨" if ac>=2.5 else "겨울 딥 쿨")
    return {"pc":pc,"tone":"warm" if ts>0 else "cool","season":PC[pc]["season"]}

def get_recs(tone, season, cat=None, limit=8, only_2026=False):
    p,g=[],[]
    for pn,shades in DB.items():
        for sh,d in shades.items():
            if not d["avail"]: continue
            if cat and d["category"]!=cat: continue
            if only_2026 and d.get("year")!=2026: continue
            if d["tone"]==tone and season in d["season"]: p.append((pn,sh,d))
            elif d["tone"]==tone: g.append((pn,sh,d))
    return (p+g)[:limit]


# ── 제품 선택 위젯 ──────────────────────────────────────────
def product_picker(prefix, include_disc=False):
    cat_labels = ["전체","립","블러셔","섀도우","베이스"]
    cat_map    = {"전체":None,"립":"lip","블러셔":"blush","섀도우":"shadow","베이스":"base"}

    cc, cp = st.columns([1, 2])
    with cc:
        lbl = st.selectbox("카", cat_labels, key=f"{prefix}_cat",
                           label_visibility="collapsed")
    chosen_cat = cat_map[lbl]

    pnames = sorted({
        pn for pn, shades in DB.items()
        for sh, d in shades.items()
        if (chosen_cat is None or d["category"]==chosen_cat)
        and (include_disc or d["avail"])
    })

    with cp:
        pname = st.selectbox("제품명", pnames, index=None,
                             placeholder="제품명 선택",
                             key=f"{prefix}_pname",
                             label_visibility="collapsed")
    if not pname:
        return None

    shade_opts = [sh for sh, d in DB[pname].items() if include_disc or d["avail"]]
    shade = st.selectbox("호수", shade_opts, index=None,
                         placeholder="호수(컬러) 선택",
                         key=f"{prefix}_shade",
                         label_visibility="collapsed")
    if not shade:
        return None

    d = DB[pname][shade]
    disc = " <span class='tag t-disc'>단종</span>" if not d["avail"] else ""
    nt   = (" " + new_tag()) if d.get("year")==2026 else ""
    st.markdown(
        f'<div class="mini-info">'
        f'<span class="mini-dot" style="background:{d["hex"]};"></span>'
        f'{tone_tag(d["tone"])} {"".join(sea_tag(s) for s in d["season"])}'
        f'{disc}{nt}'
        f'<span style="color:var(--muted)"> {d["note"]}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )
    return (pname, shade)


# ══════════════════════════════════════════════════════════════
# TAB 1  분석
# ══════════════════════════════════════════════════════════════
def tab_analysis():
    st.markdown('<p class="sec-head">퍼스널 컬러 분석</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sec-sub">사용해봤던 제품들을 입력하면 세부 8톤 퍼스널 컬러를 분석해드려요. '
        '<b>잘 맞았던 제품 1개</b>만 있어도 분석 가능해요.</p>',
        unsafe_allow_html=True,
    )
    with st.expander("💡 입력 팁 보기"):
        st.markdown("""
| 구분 | 기준 | 가중치 |
|---|---|---|
| 👍 잘 맞았던 | 피부가 환해지거나 칭찬을 많이 받은 제품 | × 1 |
| 👎 안 맞았던 | 칙칙해지거나 뜬다는 느낌을 받은 제품 | × −1.5 |
| 🔥 반응 좋았던 | SNS·일상에서 특히 호평받은 제품 | × 2 |
단종 제품도 입력 기록용으로 선택 가능해요.
        """)

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown('<div class="col-label">👍 잘 맞았던 제품 · 필수 1–3개</div>', unsafe_allow_html=True)
        g1 = product_picker("g1", include_disc=True)
        st.divider()
        g2 = product_picker("g2", include_disc=True)
        st.divider()
        g3 = product_picker("g3", include_disc=True)
    with c2:
        st.markdown('<div class="col-label">👎 안 맞았던 제품 · 선택 1–3개</div>', unsafe_allow_html=True)
        b1 = product_picker("b1", include_disc=True)
        st.divider()
        b2 = product_picker("b2", include_disc=True)
        st.divider()
        b3 = product_picker("b3", include_disc=True)
    with c3:
        st.markdown('<div class="col-label">🔥 반응 좋았던 제품 · 선택 1–3개</div>', unsafe_allow_html=True)
        t1 = product_picker("t1", include_disc=True)
        st.divider()
        t2 = product_picker("t2", include_disc=True)
        st.divider()
        t3 = product_picker("t3", include_disc=True)

    st.markdown("<br>", unsafe_allow_html=True)
    _, bc, _ = st.columns([2,2,2])
    with bc:
        clicked = st.button("🌼 퍼스널 컬러 분석하기", use_container_width=True)

    if clicked:
        goods = [x for x in [g1,g2,g3] if x]
        bads  = [x for x in [b1,b2,b3] if x]
        bests = [x for x in [t1,t2,t3] if x]
        if not goods:
            st.warning("잘 맞았던 제품을 최소 1개 선택해주세요 😊")
            return
        st.session_state["result"] = run_analysis(goods, bads, bests)

    if st.session_state.get("result"):
        _render_result(st.session_state["result"])


def _render_result(res):
    pc=res["pc"]; info=PC[pc]; tone=res["tone"]
    st.divider()
    box = "rbox-warm" if tone=="warm" else "rbox-cool"
    kw  = "".join(f"<span class='tag t-{tone}'>{k}</span>" for k in info["kw"])
    st.markdown(f"""
<div class="{box}">
    <div class="rbox-title">{info['emoji']} {pc}</div>
    <div class="rbox-desc">{info['desc']}</div>
    <div style="margin-top:0.85rem">{kw}</div>
</div>""", unsafe_allow_html=True)

    r1, r2 = st.columns(2)
    with r1:
        st.markdown("**✅ 잘 어울리는 컬러**")
        for c in info["best"]:  st.markdown(f"· {c}")
    with r2:
        st.markdown("**⛔ 피하면 좋은 컬러**")
        for c in info["avoid"]: st.markdown(f"· {c}")

    st.markdown("#### 🎁 맞춤 추천 제품")
    cc, cy = st.columns([3, 2])
    with cc:
        cat_ch = st.radio("", ["전체","립","블러셔","섀도우"], horizontal=True,
                          key="res_cat", label_visibility="collapsed")
    with cy:
        only26 = st.checkbox("2026 NEW만 보기", key="res_26")
    cmap = {"전체":None,"립":"lip","블러셔":"blush","섀도우":"shadow"}
    recs = get_recs(res["tone"], res["season"], cat=cmap[cat_ch], limit=8, only_2026=only26)
    if not recs:
        st.info("해당 조건의 추천 제품이 없어요."); return
    cols = st.columns(2)
    for i, (pn, sh, d) in enumerate(recs):
        fit = "✨ 완벽 매칭" if res["season"] in d["season"] else "👍 어울려요"
        with cols[i%2]:
            st.markdown(pcard_html(pn, sh, d, fit), unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TAB 2  연계 추천
# ══════════════════════════════════════════════════════════════
def tab_pairing():
    st.markdown('<p class="sec-head">연계 추천 서비스</p>', unsafe_allow_html=True)
    st.markdown('<p class="sec-sub">퍼스널 컬러를 선택하면 립·블러셔·섀도우를 함께 큐레이션해드려요.</p>',
                unsafe_allow_html=True)

    pc_list = list(PC.keys())
    auto = st.session_state.get("result",{}).get("pc", pc_list[0])
    idx  = pc_list.index(auto) if auto in pc_list else 0
    pc_sel = st.selectbox("퍼스널 컬러 선택", pc_list, index=idx, key="pair_pc")
    if st.session_state.get("result"):
        if st.button("🎯 분석 결과 자동 적용"):
            st.session_state["pair_pc"] = st.session_state["result"]["pc"]
            st.rerun()

    info = PC[pc_sel]; tone = info["tone"]; season = info["season"]
    ib = "ib-warm" if tone=="warm" else "ib-cool"
    st.markdown(f"""
<div class="info-band {ib}">
    <b>{info['emoji']} {pc_sel}</b> &nbsp; {tone_tag(tone)} {sea_tag(season)}<br>
    <small>{info['desc']}</small>
</div>""", unsafe_allow_html=True)

    st.markdown("### 💄 추천 립")
    lr = get_recs(tone, season, cat="lip", limit=6)
    lc = st.columns(3)
    for i, (pn, sh, d) in enumerate(lr):
        with lc[i%3]:
            nt = (" " + new_tag()) if d.get("year")==2026 else ""
            st.markdown(f"""
<div class="pcard" style="flex-direction:column;align-items:flex-start;gap:0.25rem;">
    <div style="display:flex;align-items:center;gap:0.5rem">
        {dot_html(d['hex'],20)}
        <span class="pcard-name">{pn}{nt}</span>
    </div>
    <div style="padding-left:26px">
        <div class="pcard-shade">{sh}</div>
        <div class="pcard-note">{d['note']}</div>
    </div>
</div>""", unsafe_allow_html=True)

    st.divider()
    st.markdown("### 🌸 어울리는 블러셔")
    bk = (season, "blush")
    bi = [(pn,sh,DB[pn][sh]) for pn,sh in PAIRING.get(bk,[])
          if pn in DB and sh in DB[pn] and DB[pn][sh]["avail"]] \
         or [(pn,sh,d) for pn,sh,d in get_recs(tone,season,cat="blush",limit=4)]
    bc = st.columns(2)
    for i,(pn,sh,d) in enumerate(bi[:4]):
        with bc[i%2]: st.markdown(pcard_html(pn,sh,d), unsafe_allow_html=True)

    st.divider()
    st.markdown("### ✨ 어울리는 섀도우")
    sk = (season, "shadow")
    si = [(pn,sh,DB[pn][sh]) for pn,sh in PAIRING.get(sk,[])
          if pn in DB and sh in DB[pn] and DB[pn][sh]["avail"]] \
         or [(pn,sh,d) for pn,sh,d in get_recs(tone,season,cat="shadow",limit=4)]
    sc = st.columns(2)
    for i,(pn,sh,d) in enumerate(si[:4]):
        with sc[i%2]: st.markdown(pcard_html(pn,sh,d), unsafe_allow_html=True)

    st.divider()
    tips = {"spring":"봄 웜톤은 **밝고 산뜻한 코랄·피치 조합**이 최고예요. 골드 액세서리와도 찰떡이에요.",
            "autumn":"가을 웜톤은 **어스톤·테라코타 팔레트**로 풍부한 매력을 살려보세요.",
            "summer":"여름 쿨톤은 **뮤트 핑크·라벤더 조합**이 세련돼요.",
            "winter":"겨울 쿨톤은 **강렬한 컨트라스트**가 매력이에요. 선명한 레드 립 하나로 완성!"}
    st.info(tips.get(season,""))


# ══════════════════════════════════════════════════════════════
# TAB 3  오늘의 조합
# ══════════════════════════════════════════════════════════════
def tab_today():
    st.markdown('<p class="sec-head">오늘의 뷰티 조합</p>', unsafe_allow_html=True)
    st.markdown('<p class="sec-sub">상황·무드를 선택하면 퍼스널 컬러에 맞는 오늘의 메이크업 세트를 추천해드려요.</p>',
                unsafe_allow_html=True)

    pc_list = list(PC.keys())
    auto = st.session_state.get("result",{}).get("pc", pc_list[0])
    idx  = pc_list.index(auto) if auto in pc_list else 0

    co1, co2, co3 = st.columns(3)
    with co1: pc_sel   = st.selectbox("내 퍼스널 컬러", pc_list, index=idx, key="today_pc")
    with co2: mood      = st.selectbox("오늘의 무드",   ["데일리 내추럴","오피스 룩","데이트 메이크업","파티·이벤트","페스티벌"], key="today_mood")
    with co3: intensity = st.selectbox("강도",          ["라이트","미디엄","스트롱"], key="today_int")

    info = PC[pc_sel]; tone = info["tone"]; season = info["season"]
    ci   = {"라이트":1,"미디엄":2,"스트롱":3}[intensity]
    cmin, cmax = max(1,ci-1), min(4,ci+1)

    def filtered(cat, limit=3):
        r = []
        for pn, shades in DB.items():
            for sh, d in shades.items():
                if not d["avail"] or d["category"]!=cat: continue
                if not (cmin<=d["chroma"]<=cmax): continue
                if d["tone"]==tone and season in d["season"]: r.append((pn,sh,d))
                elif d["tone"]==tone: r.append((pn,sh,d))
        return r[:limit] or [(pn,sh,d) for pn,sh,d in get_recs(tone,season,cat=cat,limit=limit)]

    ib = "ib-warm" if tone=="warm" else "ib-cool"
    st.markdown(f"""
<div class="info-band {ib}">
    <b>{info['emoji']} {pc_sel} &nbsp;·&nbsp; {mood} &nbsp;·&nbsp; {intensity}</b><br>
    <small>아래 조합으로 오늘 메이크업을 완성해보세요 ✨</small>
</div>""", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)
    for col, title, cat in [(m1,"💄 립","lip"),(m2,"🌸 블러셔","blush"),(m3,"✨ 섀도우","shadow")]:
        with col:
            st.markdown(f"**{title}**")
            for pn, sh, d in filtered(cat):
                nt = (" " + new_tag()) if d.get("year")==2026 else ""
                st.markdown(f"""
<div class="pcard" style="flex-direction:column;align-items:flex-start;gap:0.22rem;margin-bottom:0.4rem;">
    <div style="display:flex;align-items:center;gap:0.5rem">
        {dot_html(d['hex'],18)}
        <span class="pcard-name" style="font-size:0.8rem">{pn}{nt}</span>
    </div>
    <div style="padding-left:24px">
        <div class="pcard-shade">{sh}</div>
        <div class="pcard-note">{d['note']}</div>
    </div>
</div>""", unsafe_allow_html=True)

    st.divider()
    tips = {"데일리 내추럴":"💡 베이스를 가볍게 하고 립 하나로 생기를 더해보세요.",
            "오피스 룩":"💡 뮤트 컬러로 통일감을 주세요. 매트 마감이 프로페셔널해 보여요.",
            "데이트 메이크업":"💡 립과 블러셔를 같은 계열로 맞추면 얼굴이 화사해 보여요.",
            "파티·이벤트":"💡 포인트를 한 곳에만 주면 과하지 않고 세련돼 보여요.",
            "페스티벌":"💡 방수 제품 먼저 선택하세요. 글리터를 눈꼬리에 살짝 올리면 화려함 UP!"}
    st.info(tips.get(mood,""))


# ══════════════════════════════════════════════════════════════
# TAB 4  제품 탐색
# ══════════════════════════════════════════════════════════════
def tab_browse():
    st.markdown('<p class="sec-head">제품 탐색</p>', unsafe_allow_html=True)
    st.markdown('<p class="sec-sub">카테고리·톤·계절·출시연도로 필터링해서 전체 제품을 살펴보세요.</p>',
                unsafe_allow_html=True)

    f1, f2, f3, f4 = st.columns(4)
    with f1: fcat  = st.selectbox("카테고리", ["전체","립","블러셔","섀도우","베이스"], key="br_cat")
    with f2: ftone = st.selectbox("톤",       ["전체","웜톤","쿨톤"],                    key="br_tone")
    with f3: fsea  = st.selectbox("계절",     ["전체","봄 웜","가을 웜","여름 쿨","겨울 쿨"], key="br_sea")
    with f4: fyr   = st.selectbox("출시",     ["전체","2026 NEW","클래식"],              key="br_yr")
    show_disc = st.checkbox("단종 제품도 보기", value=False)

    cmap={"전체":None,"립":"lip","블러셔":"blush","섀도우":"shadow","베이스":"base"}
    tmap={"전체":None,"웜톤":"warm","쿨톤":"cool"}
    smap={"전체":None,"봄 웜":"spring","가을 웜":"autumn","여름 쿨":"summer","겨울 쿨":"winter"}
    fc, ft, fs = cmap[fcat], tmap[ftone], smap[fsea]

    rows = []
    for pn, shades in DB.items():
        for sh, d in shades.items():
            if not show_disc and not d["avail"]: continue
            if fc and d["category"]!=fc:         continue
            if ft and d["tone"]!=ft:             continue
            if fs and fs not in d["season"]:     continue
            if fyr=="2026 NEW" and d.get("year")!=2026: continue
            if fyr=="클래식"   and d.get("year") is not None: continue
            rows.append((pn, sh, d))

    st.markdown(f"<small style='color:var(--muted);font-weight:600'>{len(rows)}개 제품</small>",
                unsafe_allow_html=True)
    if not rows: st.info("조건에 맞는 제품이 없어요."); return

    for i in range(0, len(rows), 3):
        cols = st.columns(3)
        for j, (pn, sh, d) in enumerate(rows[i:i+3]):
            with cols[j]:
                disc = " <span class='tag t-disc'>단종</span>" if not d["avail"] else ""
                nt   = (" " + new_tag()) if d.get("year")==2026 else ""
                st.markdown(f"""
<div class="pcard" style="flex-direction:column;align-items:flex-start;border-radius:11px;padding:0.85rem;gap:0.32rem;">
    <div style="display:flex;align-items:center;gap:0.55rem">
        {dot_html(d['hex'],22)}
        <div>
            <div class="pcard-name">{pn}{disc}{nt}</div>
            <div class="pcard-shade">{sh}</div>
        </div>
    </div>
    <div class="pcard-note">{d['note']}</div>
    <div style="margin-top:0.1rem">{tone_tag(d['tone'])} {"".join(sea_tag(s) for s in d['season'])} {tag_html(CAT_KR.get(d['category'],''),'t-cat')}</div>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TAB 5  컬러 가이드
# ══════════════════════════════════════════════════════════════
def tab_guide():
    st.markdown('<p class="sec-head">퍼스널 컬러 가이드</p>', unsafe_allow_html=True)
    st.markdown('<p class="sec-sub">세부 8톤의 특징과 뷰티 스타일링 팁을 한눈에 확인하세요.</p>',
                unsafe_allow_html=True)

    for pc_name, info in PC.items():
        tone = info["tone"]
        with st.expander(f"{info['emoji']}  {pc_name}"):
            a, b = st.columns([3, 2])
            with a:
                kw = "".join(f"<span class='tag t-{tone}'>{k}</span>" for k in info["kw"])
                tc = "#1A1000" if tone=="warm" else "#060C30"
                st.markdown(f"""
<div style="background:{info['bg']};border:2px solid {info['bd']};border-radius:13px;padding:1.1rem 1.4rem;">
    <b style="font-size:0.98rem;color:{tc}">{info['emoji']} {pc_name}</b><br>
    <div style="font-size:0.84rem;color:{tc};margin:0.4rem 0;line-height:1.7;opacity:0.88">{info['desc']}</div>
    <div>{kw}</div>
</div>""", unsafe_allow_html=True)
            with b:
                st.markdown("**✅ 어울리는 컬러**")
                for c in info["best"]:  st.markdown(f"· {c}")
                st.markdown("**⛔ 피할 컬러**")
                for c in info["avoid"]: st.markdown(f"· {c}")

            st.markdown("**🛍️ 대표 추천 제품**")
            recs = get_recs(tone, info["season"], limit=4)
            gc = st.columns(4)
            for i, (pn, sh, d) in enumerate(recs):
                with gc[i]:
                    st.markdown(f"""
<div style="text-align:center;padding:0.4rem 0.1rem;">
    <div style="width:28px;height:28px;border-radius:50%;background:{d['hex']};
                margin:0 auto 0.28rem;border:2px solid rgba(0,0,0,0.12);"></div>
    <div style="font-size:0.71rem;font-weight:600;color:var(--text);line-height:1.3">{pn}</div>
    <div style="font-size:0.65rem;color:var(--muted)">{sh}</div>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════
def main():
    st.markdown("""
<div class="hero-title">TONE<em>ME</em></div>
<div class="hero-bar"></div>
<div class="hero-sub">퍼스널 컬러 기반 뷰티 큐레이터 · 세부 8톤 분석 · 국내 구매 가능 · 2026 신제품 포함</div>
""", unsafe_allow_html=True)

    t1, t2, t3, t4, t5 = st.tabs([
        "🎨 퍼스널 컬러 분석",
        "✨ 연계 추천",
        "🌼 오늘의 조합",
        "🗂️ 제품 탐색",
        "📖 컬러 가이드",
    ])
    with t1: tab_analysis()
    with t2: tab_pairing()
    with t3: tab_today()
    with t4: tab_browse()
    with t5: tab_guide()

    st.markdown('<div class="footer">TONEME · 단종 제품은 추천 제외 · 국내 구매 가능 · 2026 신제품 포함</div>',
                unsafe_allow_html=True)


if __name__ == "__main__":
    main()
