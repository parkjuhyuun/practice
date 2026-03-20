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
    --border:   #E0D96A;
    --accent:   #B8860B;   /* 다크골드 — 개나리 위에서 가독성 최고 */
    --accent2:  #D4A800;
    --text:     #1A1200;   /* 거의 검정 — 개나리 배경에 최고 대비 */
    --sub:      #4A3F00;   /* 진한 올리브 브라운 — 부제목 */
    --muted:    #6B5C00;   /* 중간 명도 텍스트 */
    --tag-border: #C8B800;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: var(--bg) !important;
    font-family: 'Noto Sans KR', sans-serif;
    color: var(--text);
}
[data-testid="stSidebar"] { display: none; }
.block-container { padding: 2.5rem 3rem 6rem !important; max-width: 1100px !important; }

/* ── HERO ── */
.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.2rem; font-weight: 300; letter-spacing: 0.08em;
    color: var(--text); line-height: 1; text-transform: uppercase;
}
.hero-title em { font-style: italic; color: var(--accent); }
.hero-bar  { width: 48px; height: 2.5px; background: var(--accent); margin: 0.6rem 0 0.7rem; border-radius: 2px; }
.hero-sub  { font-size: 0.8rem; color: var(--sub); letter-spacing: 0.05em; margin-bottom: 2rem; font-weight: 500; }

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] { gap:0; background:transparent; border-bottom:2px solid var(--border); }
.stTabs [data-baseweb="tab"] {
    font-size:0.86rem; font-weight:500; color:var(--sub);
    padding:0.6rem 1.4rem; border-radius:0; background:transparent; border:none;
}
.stTabs [aria-selected="true"] {
    color: var(--text) !important; background:transparent !important;
    border-bottom:2.5px solid var(--accent) !important; font-weight:700 !important;
}

/* ── SECTION ── */
.sec-head { font-size:1.15rem; font-weight:700; color:var(--text); margin-bottom:0.2rem; }
.sec-sub  { font-size:0.82rem; color:var(--sub); line-height:1.7; margin-bottom:1.2rem; font-weight:400; }
.col-label {
    font-size:0.78rem; font-weight:700; letter-spacing:0.04em;
    color:var(--text); padding-bottom:0.6rem;
    border-bottom:1.5px solid var(--border); margin-bottom:0.9rem;
}

/* ── SELECTBOX ── */
.stSelectbox label { display:none !important; }
.stSelectbox > div > div {
    border-radius:10px !important; border-color:var(--border) !important;
    font-size:0.86rem !important; background:var(--surface) !important;
    font-weight:500 !important; color:var(--text) !important;
}

/* ── 선택 후 미니 정보 ── */
.mini-info {
    display:flex; align-items:center; gap:0.5rem;
    padding:0.5rem 0.8rem;
    background: #FFFBE0;
    border:1.5px solid var(--accent);
    border-radius:9px; margin-top:0.3rem;
    font-size:0.77rem; color:var(--sub); font-weight:500;
}
.mini-dot { width:14px; height:14px; border-radius:50%; flex-shrink:0; border:1.5px solid rgba(0,0,0,0.15); }

/* ── TAGS ── */
.tag {
    display:inline-block; padding:0.17rem 0.65rem;
    border-radius:100px; font-size:0.7rem; font-weight:600; margin:0.05rem;
}
/* 웜/쿨 — 개나리 위 가독성 확보 위해 진한 배경 */
.t-warm   { background:#7A4500; color:#FFE8B0; }
.t-cool   { background:#1A3070; color:#C8DCFF; }
.t-spring { background:#8A3000; color:#FFD8B0; }
.t-summer { background:#2A2080; color:#C8C8FF; }
.t-autumn { background:#6A3800; color:#FFD8A0; }
.t-winter { background:#202870; color:#C0CCFF; }
.t-cat    { background:#4A3800; color:#FFE8A0; }
.t-disc   { background:#555;    color:#EEE;   }
.t-new24  { background:#7A5A00; color:#FFF0A0; }
.t-new25  { background:#5A1A70; color:#F0D8FF; }
.t-new26  { background:#004A30; color:#B0FFD8; }

/* ── DOT ── */
.dot { display:inline-block; border-radius:50%; border:1.5px solid rgba(0,0,0,0.15); vertical-align:middle; flex-shrink:0; }

/* ── PCARD ── */
.pcard {
    display:flex; align-items:center; gap:0.7rem;
    background:var(--surface); border:1px solid var(--border);
    border-radius:11px; padding:0.8rem 1rem; margin-bottom:0.5rem;
}
.pcard-info { flex:1; min-width:0; }
.pcard-name  { font-weight:600; font-size:0.86rem; line-height:1.3; color:var(--text); }
.pcard-shade { font-size:0.77rem; color:var(--muted); font-weight:500; }
.pcard-note  { font-size:0.72rem; color:var(--sub); margin-top:0.1rem; }
.pcard-fit   { font-size:0.7rem; color:var(--accent); white-space:nowrap; font-weight:600; }

/* ── RESULT BOX ── */
.rbox-warm {
    background:linear-gradient(135deg,#FFF8D0,#FFE870);
    border:2px solid #C8A000; border-radius:18px;
    padding:1.8rem 2rem; margin-bottom:1.2rem;
}
.rbox-cool {
    background:linear-gradient(135deg,#E8F0FF,#C8D8FF);
    border:2px solid #6080C0; border-radius:18px;
    padding:1.8rem 2rem; margin-bottom:1.2rem;
}
.rbox-title {
    font-family:'Cormorant Garamond',serif;
    font-size:2.1rem; font-weight:500; color:var(--text); margin-bottom:0.4rem;
}
.rbox-desc { font-size:0.88rem; color:#2A2000; line-height:1.75; font-weight:500; }

/* ── INFO BAND ── */
.info-band { border-radius:11px; padding:1rem 1.3rem; margin-bottom:1rem; }
.ib-warm { background:linear-gradient(135deg,#FFF8D0,#FFE870); border:1.5px solid #C8A000; }
.ib-cool { background:linear-gradient(135deg,#E8F0FF,#C8D8FF); border:1.5px solid #6080C0; }
.ib-warm b, .ib-warm small { color:#1A1000 !important; }
.ib-cool b, .ib-cool small { color:#0A1040 !important; }

/* ── BUTTON ── */
.stButton > button {
    background: var(--accent) !important; color:#FFF8E0 !important;
    border:none !important; border-radius:9px !important;
    padding:0.65rem 1.8rem !important; font-size:0.87rem !important;
    font-weight:700 !important; width:100% !important;
    letter-spacing:0.02em !important;
}
.stButton > button:hover { opacity:0.85 !important; }

/* ── RADIO / CHECKBOX ── */
.stRadio label, .stCheckbox label { color:var(--text) !important; font-weight:500 !important; font-size:0.84rem !important; }

/* ── EXPANDER ── */
details summary { font-size:0.84rem !important; color:var(--text) !important; font-weight:600 !important; }

hr { border-color:var(--border) !important; margin:1.4rem 0 !important; }
.stSuccess,.stWarning,.stInfo { border-radius:10px !important; font-size:0.85rem !important; }

/* ── FOOTER ── */
.footer { text-align:center; font-size:0.73rem; color:var(--muted); padding:1.5rem 0 2rem; font-weight:500; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# DB  — 출시년도별 태그
# new_year: 2024 / 2025 / 2026 / None
# ══════════════════════════════════════════════════════════════
def p(tone, season, chroma, value, category, hex_col, avail, note, year=None):
    return dict(tone=tone, season=season, chroma=chroma, value=value,
                category=category, hex=hex_col, avail=avail, note=note, year=year)

DB = {
    # ═══ LIP ════════════════════════════════════════════════
    "롬앤 쥬시 래스팅 틴트": {
        "06 피그피그":           p("cool",["summer","winter"],  2,2,"lip","#C47090",True, "물광 마감, 뮤트 로즈"),
        "07 쥬쥬브":             p("warm",["spring","autumn"],  3,2,"lip","#C45858",True, "생기있는 레드베리"),
        "08 애플브라운":         p("warm",["autumn"],           2,2,"lip","#A85040",True, "깊은 테라코타 브라운"),
        "17 딸기우유":           p("cool",["spring","summer"],  2,3,"lip","#D88090",True, "투명감 딸기밀크 핑크"),
        "20 레드벨벳":           p("cool",["winter"],           4,2,"lip","#B83040",True, "딥레드, 강렬한 존재감"),
        "23 피칸브라운":         p("warm",["autumn"],           1,2,"lip","#885040",True, "일상 내추럴 누드브라운"),
        "28 핑크핑크":           p("cool",["summer"],           3,3,"lip","#E070A8",True, "발랄한 쿨핑크",2024),
        "29 브릭베이지":         p("warm",["autumn"],           2,2,"lip","#A06850",True, "웜 브릭베이지",2024),
        "31 딸기크림":           p("cool",["spring","summer"],  2,3,"lip","#E088A0",True, "딸기크림 쿨핑크",2025),
        "32 코코아라떼":         p("warm",["autumn"],           1,2,"lip","#906050",True, "웜 코코아 뮤트 브라운",2025),
        "33 체리블라썸":         p("cool",["summer"],           2,3,"lip","#D878A8",True, "체리블라썸 쿨로즈",2026),
        "34 선라이즈코랄":       p("warm",["spring"],           3,3,"lip","#E87850",True, "선라이즈 코랄오렌지",2026),
    },
    "에뛰드 픽싱 틴트": {
        "03 멜로우피치":         p("warm",["spring"],           2,3,"lip","#E09068",True, "복숭아빛 코랄, 봄 생기"),
        "05 미드나잇모브":       p("cool",["winter","summer"],  2,2,"lip","#987090",True, "보랏빛 뮤트 핑크"),
        "06 소프트월넛":         p("warm",["autumn"],           1,2,"lip","#906858",True, "웜 누드, 피부 밀착"),
        "08 베리핑크":           p("cool",["summer"],           3,3,"lip","#C870A0",True, "선명 핑크, 여름 포인트"),
        "11 진저브라운":         p("warm",["autumn"],           2,2,"lip","#8A5040",False,"깊은 진저브라운 ★단종"),
        "12 스트로베리소다":     p("cool",["spring","summer"],  3,3,"lip","#E06898",True, "청량 딸기소다",2024),
        "13 로즈우드누드":       p("cool",["summer","winter"],  1,2,"lip","#A07880",True, "쿨 로즈우드 뮤트",2025),
        "14 코럴오렌지피치":     p("warm",["spring"],           3,3,"lip","#E88058",True, "코럴오렌지 피치",2025),
        "15 버건디플럼":         p("cool",["winter"],           3,1,"lip","#8A2858",True, "딥 버건디 플럼",2026),
    },
    "페리페라 잉크 무드 글로이 틴트": {
        "01 쿨오프코랄":         p("warm",["spring"],           3,3,"lip","#E07860",True, "밝은 코랄오렌지"),
        "03 맘찍로즈":           p("cool",["summer"],           2,3,"lip","#D088A0",True, "뮤트 로즈핑크"),
        "06 초코브릭":           p("warm",["autumn"],           2,2,"lip","#8A4838",True, "초콜릿 브릭 레드"),
        "09 코랄프레쉬":         p("warm",["spring"],           3,3,"lip","#E06848",True, "생생한 코랄"),
        "14 누드로즈우드":       p("cool",["summer","winter"],  1,2,"lip","#A87888",True, "쿨 누드로즈우드",2024),
        "15 라벤더쇼크":         p("cool",["summer"],           2,3,"lip","#B890C8",True, "라벤더빛 쿨핑크",2024),
        "16 선셋오렌지":         p("warm",["spring","autumn"],  3,3,"lip","#E86840",True, "선셋 웜 오렌지",2025),
        "17 스모키로즈":         p("cool",["winter"],           2,2,"lip","#907080",True, "스모키 쿨로즈",2025),
        "18 누드베이지핑크":     p("warm",["spring","autumn"],  1,3,"lip","#D0A090",True, "웜 누드베이지핑크",2026),
        "19 라즈베리소다":       p("cool",["summer","winter"],  3,3,"lip","#C04878",True, "라즈베리 쿨소다",2026),
    },
    "클리오 쉬폰 블러 틴트": {
        "03 피치퍼즐":           p("warm",["spring","autumn"],  2,3,"lip","#D89080",True, "스모키 피치"),
        "05 코랄":               p("warm",["spring"],           2,3,"lip","#DC7060",True, "클래식 코랄"),
        "07 로즈":               p("cool",["summer","winter"],  3,3,"lip","#C86890",True, "청량한 로즈"),
        "09 레드브릭":           p("warm",["autumn"],           3,2,"lip","#A03830",True, "벽돌빛 레드"),
        "13 쿨핑크클라우드":     p("cool",["summer"],           2,3,"lip","#D880B0",True, "구름 같은 쿨핑크",2024),
        "14 웜테라누드":         p("warm",["autumn"],           1,2,"lip","#9A6050",True, "웜 테라코타 누드",2024),
        "15 스트로베리마카롱":   p("cool",["spring","summer"],  2,3,"lip","#E080A8",True, "스트로베리 마카롱",2025),
        "16 카라멜브리크":       p("warm",["autumn"],           2,2,"lip","#A06048",True, "카라멜 브릭 웜",2025),
        "17 블루밍로즈":         p("cool",["summer","winter"],  2,3,"lip","#C06888",True, "블루밍 쿨로즈",2026),
        "18 어텀헤이즐":         p("warm",["autumn"],           2,2,"lip","#906050",True, "어텀 헤이즐넛 웜",2026),
    },
    "3CE 벨벳 립 틴트": {
        "파우더핑크":            p("cool",["summer"],           1,3,"lip","#D8A8B8",True, "파우더리 쿨핑크 누드"),
        "두메":                  p("cool",["winter"],           2,2,"lip","#B06888",True, "뮤트 로즈브라운, 겨울 정석"),
        "러스티로즈":            p("cool",["summer","winter"],  2,2,"lip","#A87080",True, "빈티지 로즈"),
        "퍼스트데이트":          p("warm",["spring"],           2,3,"lip","#E09898",True, "밝은 베이비핑크"),
        "누드플럼":              p("cool",["winter"],           2,1,"lip","#7A5068",True, "딥 누드 플럼"),
        "코코아무드":            p("warm",["autumn"],           1,2,"lip","#8A5848",True, "코코아 웜 브라운",2024),
        "쿨라일락":              p("cool",["summer"],           2,3,"lip","#C0A0D0",True, "연한 쿨 라일락",2024),
        "딥로즈우드":            p("cool",["winter"],           2,1,"lip","#7A4860",True, "딥 쿨 로즈우드",2025),
        "코튼캔디":              p("cool",["spring","summer"],  1,3,"lip","#E0B0C8",True, "코튼캔디 쿨파스텔",2025),
        "테라코타선셋":          p("warm",["autumn","spring"],  2,2,"lip","#A86848",True, "테라코타 선셋",2026),
        "아이리스핑크":          p("cool",["summer"],           2,3,"lip","#C898C8",True, "아이리스 쿨핑크",2026),
    },
    "맥 리프스틱": {
        "Whirl":                 p("warm",["autumn"],           1,2,"lip","#906060",True, "국민 누드브라운, 가을 완벽템"),
        "Ruby Woo":              p("cool",["winter"],           4,2,"lip","#C02030",True, "클래식 블루베이스 레드"),
        "Velvet Teddy":          p("warm",["autumn"],           1,2,"lip","#8A5848",True, "따뜻한 뮤트 누드"),
        "Brave":                 p("warm",["spring","autumn"],  1,3,"lip","#C09080",True, "피치 누드"),
        "Flat Out Fabulous":     p("cool",["winter"],           3,1,"lip","#803060",True, "다크 플럼"),
    },
    "롬앤 한올한올 뉴립스틱": {
        "04 베어릭":             p("warm",["autumn"],           1,2,"lip","#9A6858",True, "워터리 피부색 누드"),
        "07 코럴하이":           p("warm",["spring"],           3,3,"lip","#E07060",True, "코랄 레드"),
        "11 스트로베리파우더":   p("cool",["summer"],           2,3,"lip","#D08898",True, "파우더리 딸기 핑크"),
        "14 라즈베리무드":       p("cool",["winter"],           3,2,"lip","#B04870",True, "선명한 라즈베리"),
        "17 코코넛누드":         p("warm",["spring","autumn"],  1,3,"lip","#C8A080",True, "밀크누드, 일상 쓰기 좋은"),
        "20 피치소르베":         p("warm",["spring"],           2,3,"lip","#E09878",True, "피치 소르베 웜",2025),
        "21 쿨베리":             p("cool",["winter","summer"],  3,2,"lip","#B05080",True, "쿨베리 딥",2025),
        "22 모카브라운":         p("warm",["autumn"],           1,2,"lip","#886050",True, "모카 웜브라운",2026),
        "23 쿨라즈베리소다":     p("cool",["summer"],           3,3,"lip","#D05090",True, "쿨 라즈베리 소다",2026),
    },
    # 2024 신규 브랜드
    "투쿨포스쿨 아트클래스 바이 로댕 틴트": {
        "01 로제":               p("cool",["summer"],           2,3,"lip","#D890A8",True, "그라데이션 쿨로즈",2024),
        "02 베이지테라":         p("warm",["autumn"],           1,2,"lip","#A07860",True, "그라데이션 웜베이지",2024),
        "03 버건디":             p("cool",["winter"],           3,2,"lip","#903060",True, "그라데이션 버건디",2024),
        "04 코퍼로즈":           p("warm",["spring","autumn"],  2,2,"lip","#B07868",True, "그라데이션 코퍼로즈",2025),
        "05 쿨모브":             p("cool",["winter"],           2,2,"lip","#987098",True, "그라데이션 쿨모브",2025),
    },
    "어퓨 쥬시 팝 틴트": {
        "01 코튼캔디핑크":       p("cool",["spring","summer"],  2,3,"lip","#E890B8",True, "솜사탕 쿨핑크",2024),
        "02 망고코랄":           p("warm",["spring"],           3,3,"lip","#E8804A",True, "망고빛 코랄오렌지",2024),
        "03 피그플럼":           p("cool",["winter"],           3,2,"lip","#903868",True, "무화과 플럼",2024),
        "04 피치소다":           p("warm",["spring","summer"],  2,3,"lip","#E89878",True, "피치 소다 웜",2025),
        "05 블루베리밀크":       p("cool",["summer","winter"],  2,2,"lip","#A878B0",True, "블루베리밀크 쿨",2025),
    },
    "미샤 아이돌 립 글로우": {
        "01 누드코랄":           p("warm",["spring","autumn"],  2,3,"lip","#D89070",True, "촉촉 누드코랄",2024),
        "02 쿨로즈베리":         p("cool",["summer","winter"],  2,2,"lip","#C06888",True, "쿨 로즈베리 글로우",2024),
        "03 웜브릭":             p("warm",["autumn"],           2,2,"lip","#A04838",True, "웜 브릭 레드",2024),
    },
    # 2025 신규
    "헤라 센슈얼 립 틴트 2025": {
        "01 뉴드핑크":           p("cool",["summer"],           1,3,"lip","#D8A8B8",True, "뉴드 쿨핑크 글로우",2025),
        "02 테라핑크":           p("warm",["spring","autumn"],  2,3,"lip","#D89880",True, "테라핑크 웜",2025),
        "03 딥모브":             p("cool",["winter"],           2,1,"lip","#806078",True, "딥 쿨모브",2025),
        "04 코랄레드":           p("warm",["spring"],           3,3,"lip","#E06848",True, "비비드 코랄레드",2025),
    },
    "클리오 멜팅 틴트 2025": {
        "01 피치쉬폰":           p("warm",["spring"],           2,3,"lip","#E09878",True, "피치 쉬폰 웜",2025),
        "02 로즈워터":           p("cool",["summer"],           2,3,"lip","#D090A8",True, "로즈워터 쿨",2025),
        "03 딥카라멜":           p("warm",["autumn"],           2,2,"lip","#9A6050",True, "딥 카라멜 웜",2025),
        "04 베리밀크":           p("cool",["winter","summer"],  2,2,"lip","#B07890",True, "베리밀크 쿨",2025),
    },
    # 2026 신규
    "롬앤 글래시 틴트 2026": {
        "01 글래시피치":         p("warm",["spring"],           2,3,"lip","#E8A888",True, "광택 피치 웜",2026),
        "02 글래시로즈":         p("cool",["summer","winter"],  2,3,"lip","#D088A8",True, "광택 쿨로즈",2026),
        "03 글래시코랄":         p("warm",["spring","autumn"],  3,3,"lip","#E87858",True, "광택 코랄 웜",2026),
        "04 글래시베리":         p("cool",["winter"],           3,2,"lip","#A84878",True, "광택 딥베리 쿨",2026),
    },
    "에뛰드 딥 픽싱 틴트 2026": {
        "01 딥코랄":             p("warm",["spring","autumn"],  3,2,"lip","#C86040",True, "딥 웜코랄",2026),
        "02 딥로즈":             p("cool",["winter"],           3,2,"lip","#A84870",True, "딥 쿨로즈",2026),
        "03 딥브라운":           p("warm",["autumn"],           2,1,"lip","#885040",True, "딥 웜브라운",2026),
    },

    # ═══ BLUSH ══════════════════════════════════════════════
    "롬앤 베러 댄 치크": {
        "피치칩":                p("warm",["spring","autumn"],  2,3,"blush","#E8A878",True, "황금 피치, 웜 피부 생기"),
        "스트로베리밀크":        p("cool",["summer"],           2,3,"blush","#D898A8",True, "딸기우유빛 쿨 핑크"),
        "코랄리프":              p("warm",["spring"],           3,3,"blush","#E89070",True, "생생한 코랄"),
        "쿨로즈":                p("cool",["winter","summer"],  2,2,"blush","#C880A0",True, "블루베이스 쿨 로즈"),
        "누디피치":              p("warm",["autumn"],           1,2,"blush","#D0988A",True, "웜 누디 피치"),
        "선셋코랄":              p("warm",["spring","autumn"],  3,2,"blush","#E07858",True, "선셋빛 코랄",2024),
        "라벤더드림":            p("cool",["summer"],           2,3,"blush","#C0B0D8",True, "라벤더빛 쿨",2024),
        "로즈골드쉬머":          p("warm",["spring","autumn"],  2,3,"blush","#D8988A",True, "로즈골드 쉬머",2025),
        "쿨베이비핑크":          p("cool",["summer"],           1,3,"blush","#E0B0C8",True, "쿨 베이비핑크",2025),
        "코퍼테라":              p("warm",["autumn"],           2,2,"blush","#C07858",True, "코퍼 테라코타",2026),
        "쿨라일락블러":          p("cool",["summer","winter"],  2,3,"blush","#C0A8D8",True, "쿨 라일락 블러",2026),
    },
    "에뛰드 러블리 쿠키 블러셔": {
        "1호 피치":              p("warm",["spring"],           2,3,"blush","#EDA880",True, "부드러운 피치"),
        "2호 핑크":              p("cool",["summer"],           2,3,"blush","#E0A0B8",True, "밝은 쿨핑크"),
        "3호 오렌지":            p("warm",["autumn","spring"],  3,3,"blush","#E89060",True, "선명한 오렌지"),
        "5호 베이지":            p("warm",["autumn"],           1,2,"blush","#C8A888",True, "내추럴 베이지 음영"),
        "6호 코코아로즈":        p("warm",["autumn"],           2,2,"blush","#C09080",True, "코코아 로즈 웜",2025),
        "7호 쿨모브":            p("cool",["winter"],           2,2,"blush","#B088A8",True, "쿨 모브",2025),
        "8호 선셋피치":          p("warm",["spring"],           3,3,"blush","#E8A070",True, "선셋 피치",2026),
    },
    "클리오 킬 커버 더 뉴 치크": {
        "02 다이닝로즈":         p("cool",["summer","winter"],  2,3,"blush","#D890A8",True, "뮤트 쿨 로즈"),
        "03 캐시미어":           p("warm",["autumn"],           1,2,"blush","#C8A090",True, "웜 캐시미어 베이지"),
        "05 보나피치":           p("warm",["spring","summer"],  2,3,"blush","#E8A890",True, "따뜻한 코랄피치"),
        "07 쿨모브":             p("cool",["winter"],           2,2,"blush","#B880A8",True, "딥 쿨모브"),
        "09 웜어스":             p("warm",["autumn"],           2,2,"blush","#B07860",True, "웜 어스톤",2025),
        "10 쿨베리":             p("cool",["winter","summer"],  3,2,"blush","#A87098",True, "쿨 베리핑크",2025),
        "11 코랄피치글로우":     p("warm",["spring"],           2,3,"blush","#E8A880",True, "코랄피치 글로우",2026),
    },
    "NARS 블러쉬": {
        "오가즘":                p("warm",["spring","summer"],  2,3,"blush","#E09888",True, "골드쉬머 피치핑크, 국민템"),
        "딥트로트":              p("warm",["autumn"],           2,2,"blush","#C07860",True, "깊은 테라코타"),
        "카마수트라":            p("cool",["winter"],           3,2,"blush","#B86080",True, "딥 쿨로즈"),
        "부에노스아이레스":      p("cool",["summer"],           2,3,"blush","#D898B0",True, "소프트 쿨핑크"),
        "섹스어필":              p("warm",["autumn"],           3,1,"blush","#A06040",True, "딥 어스 테라"),
    },
    "페리페라 블러블러 페이스 블러셔": {
        "01 코코피치":           p("warm",["spring","autumn"],  2,3,"blush","#E0A080",True, "코코넛 피치"),
        "02 쿨로즈퍼지":         p("cool",["summer"],           2,3,"blush","#D8A0B8",True, "퍼지 쿨 로즈핑크"),
        "03 미드나잇플럼":       p("cool",["winter"],           3,2,"blush","#A06888",True, "딥 쿨 플럼"),
        "04 어텀테라":           p("warm",["autumn"],           2,2,"blush","#B07058",True, "어스 테라코타",2024),
        "05 스프링코랄":         p("warm",["spring"],           3,3,"blush","#E09070",True, "봄 코랄핑크",2024),
        "06 글래시로즈":         p("cool",["summer","winter"],  2,3,"blush","#D098B8",True, "글래시 쿨로즈",2025),
        "07 피치코퍼":           p("warm",["spring","autumn"],  2,3,"blush","#D89878",True, "피치 코퍼",2025),
        "08 핑크모브":           p("cool",["summer"],           2,3,"blush","#D0A0C0",True, "핑크 모브 쿨",2026),
        "09 테라로즈":           p("warm",["autumn"],           2,2,"blush","#B87868",True, "테라 로즈 웜",2026),
    },
    "헤라 센슈얼 파우더 블러셔": {
        "01 로즈코랄":           p("warm",["spring","summer"],  2,3,"blush","#E09888",True, "로즈코랄 쉬머",2024),
        "02 쿨핑크":             p("cool",["summer"],           2,3,"blush","#D898B8",True, "쿨핑크 쉬머",2024),
        "03 딥테라":             p("warm",["autumn"],           2,2,"blush","#B07060",True, "딥 테라코타 쉬머",2024),
        "04 라벤더무드":         p("cool",["summer","winter"],  2,3,"blush","#C0A8D0",True, "라벤더 쿨",2025),
        "05 웜피치글로":         p("warm",["spring"],           2,3,"blush","#E0A880",True, "웜 피치 글로",2025),
        "06 로즈골드":           p("warm",["spring","autumn"],  2,3,"blush","#D09880",True, "로즈골드 쉬머",2026),
        "07 쿨모브":             p("cool",["winter"],           2,2,"blush","#A880A0",True, "쿨 모브 쉬머",2026),
    },
    "투쿨포스쿨 체크 체크 블러셔": {
        "01 코튼피치":           p("warm",["spring"],           2,3,"blush","#EDB090",True, "코튼 피치",2024),
        "02 플럼체크":           p("cool",["winter"],           2,2,"blush","#B07890",True, "플럼 쿨",2024),
        "03 코랄드롭":           p("warm",["spring","autumn"],  3,3,"blush","#E09070",True, "코랄드롭 웜",2025),
        "04 쿨바이올렛":         p("cool",["summer","winter"],  2,3,"blush","#B0A0C8",True, "쿨 바이올렛",2025),
    },
    # 2026 신규 블러셔
    "에스쁘아 클라우드 블러셔 2026": {
        "01 피치클라우드":       p("warm",["spring"],           2,3,"blush","#E8A880",True, "피치 클라우드 웜",2026),
        "02 로즈클라우드":       p("cool",["summer"],           2,3,"blush","#D898B8",True, "로즈 클라우드 쿨",2026),
        "03 테라클라우드":       p("warm",["autumn"],           2,2,"blush","#B87860",True, "테라 클라우드 웜",2026),
    },

    # ═══ SHADOW ═════════════════════════════════════════════
    "클리오 프로 아이 팔레트": {
        "03 앤틱핑크":           p("cool",["summer","winter"],  2,3,"shadow","#D8A8B8",True, "쿨톤 핑크 멀티"),
        "04 브라운브릭":         p("warm",["autumn"],           2,2,"shadow","#987060",True, "웜 브라운 전문"),
        "06 어텀테라":           p("warm",["autumn","spring"],  2,2,"shadow","#B07858",True, "테라코타 어텀"),
        "09 스모키쿨":           p("cool",["winter"],           2,1,"shadow","#706880",True, "쿨톤 스모키 전문"),
        "11 로즈골드":           p("warm",["spring","autumn"],  2,3,"shadow","#C09070",True, "로즈골드 웜",2024),
        "12 쿨그레이":           p("cool",["winter","summer"],  1,2,"shadow","#9090A8",True, "쿨 그레이 스모키",2024),
        "13 선셋테라":           p("warm",["autumn","spring"],  3,2,"shadow","#B87050",True, "선셋 테라 팔레트",2025),
        "14 쿨베리모브":         p("cool",["winter","summer"],  2,2,"shadow","#9878A8",True, "쿨 베리모브 팔레트",2025),
        "15 코랄어스":           p("warm",["spring"],           3,3,"shadow","#D09070",True, "코랄 어스 팔레트",2026),
        "16 미드나잇쿨":         p("cool",["winter"],           2,1,"shadow","#606088",True, "미드나잇 쿨 스모키",2026),
    },
    "에뛰드 플레이 컬러 아이즈": {
        "베어누드":              p("warm",["autumn","spring"],  1,3,"shadow","#C8B098",True, "웜 베이지 데일리"),
        "라즈베리초콜릿":        p("cool",["winter","summer"],  2,2,"shadow","#907880",True, "쿨 다크베리"),
        "핑크쉐이드":            p("cool",["summer"],           2,3,"shadow","#D8A8B8",True, "소프트 쿨핑크"),
        "브라운토피":            p("warm",["autumn"],           2,2,"shadow","#987060",False,"웜 토피브라운 ★단종"),
        "올리브그린":            p("warm",["autumn"],           2,2,"shadow","#788050",True, "올리브 어스톤",2024),
        "코랄선셋":              p("warm",["spring"],           3,3,"shadow","#E09870",True, "코랄 선셋 팔레트",2024),
        "로즈골드브라운":        p("warm",["autumn","spring"],  2,2,"shadow","#C09070",True, "로즈골드 브라운",2025),
        "쿨라벤더":              p("cool",["summer","winter"],  2,3,"shadow","#A898C8",True, "쿨 라벤더 팔레트",2025),
        "테라오렌지":            p("warm",["spring","autumn"],  3,3,"shadow","#D08858",True, "테라 오렌지 팔레트",2026),
        "딥쿨모브":              p("cool",["winter"],           2,1,"shadow","#8878A0",True, "딥 쿨 모브",2026),
    },
    "어반디케이 네이키드 팔레트": {
        "NAKED3":                p("cool",["summer","winter"],  2,3,"shadow","#C090A0",True, "쿨 로즈 뉴트럴 — 국내 구매가능"),
        "NAKED RELOADED":        p("warm",["autumn","spring"],  2,2,"shadow","#B09070",True, "웜 뉴트럴 — 국내 구매가능"),
    },
    "맥 아이섀도우 단품": {
        "코퍼스파크":            p("warm",["autumn"],           3,2,"shadow","#C07840",True, "쉬머 구리빛"),
        "브라운다운":            p("warm",["autumn","spring"],  2,2,"shadow","#906050",True, "클래식 웜 브라운"),
        "스노우화이트":          p("cool",["winter","summer"],  1,4,"shadow","#E8E0E8",True, "쿨 하이라이트 섀도우"),
        "소번":                  p("warm",["autumn"],           3,1,"shadow","#7A4828",True, "다크 웜브라운 포인트"),
    },
    "롬앤 한올한올 아이섀도우": {
        "03 로즈핑크":           p("cool",["summer"],           2,3,"shadow","#D890A8",True, "맑은 쿨 로즈"),
        "06 코퍼브라운":         p("warm",["autumn"],           2,2,"shadow","#A07058",True, "구리빛 브라운"),
        "10 테라핑크":           p("warm",["spring"],           2,3,"shadow","#D89080",True, "코랄핑크 섀도우"),
        "13 스모키그레이":       p("cool",["winter"],           1,2,"shadow","#888098",True, "쿨 스모키 그레이"),
        "16 골든코퍼":           p("warm",["autumn","spring"],  3,2,"shadow","#C08040",True, "골든 코퍼 쉬머",2025),
        "17 쿨바이올렛":         p("cool",["summer","winter"],  2,3,"shadow","#9888C0",True, "쿨 바이올렛 쉬머",2025),
        "18 로즈테라":           p("warm",["spring","autumn"],  2,3,"shadow","#D09080",True, "로즈 테라 웜",2026),
        "19 아이스블루":         p("cool",["winter"],           1,3,"shadow","#8898C8",True, "아이스블루 쿨",2026),
    },
    "페리페라 인크 더 아이섀도우 팔레트": {
        "01 웜어스":             p("warm",["autumn"],           2,2,"shadow","#A07858",True, "어스톤 웜 팔레트",2024),
        "02 쿨로즈":             p("cool",["summer","winter"],  2,3,"shadow","#C090A8",True, "쿨 로즈 팔레트",2024),
        "03 코랄핑크":           p("warm",["spring"],           3,3,"shadow","#E09078",True, "코랄핑크 팔레트",2024),
        "04 브론즈어텀":         p("warm",["autumn"],           3,2,"shadow","#B08050",True, "브론즈 어텀 팔레트",2025),
        "05 쿨스모키":           p("cool",["winter"],           2,1,"shadow","#807888",True, "쿨 스모키 팔레트",2025),
        "06 선셋글로우":         p("warm",["spring","autumn"],  3,3,"shadow","#D08860",True, "선셋 글로우 팔레트",2026),
        "07 쿨베리나이트":       p("cool",["winter","summer"],  2,2,"shadow","#8870A0",True, "쿨 베리나이트 팔레트",2026),
    },
    "투쿨포스쿨 아트클래스 팔레트": {
        "웜누드":                p("warm",["spring","autumn"],  1,3,"shadow","#C8A888",True, "웜 누드 아트 팔레트",2024),
        "쿨모브":                p("cool",["summer","winter"],  2,2,"shadow","#9888A8",True, "쿨 모브 아트 팔레트",2024),
        "웜어스글로우":          p("warm",["autumn"],           2,2,"shadow","#B08868",True, "웜 어스 글로우",2025),
        "쿨로즈쉬머":            p("cool",["summer","winter"],  2,3,"shadow","#C090B0",True, "쿨 로즈 쉬머",2025),
        "선셋브론즈":            p("warm",["spring","autumn"],  3,2,"shadow","#C09060",True, "선셋 브론즈",2026),
        "미드나잇블루모브":      p("cool",["winter"],           2,1,"shadow","#7070A0",True, "미드나잇 블루모브",2026),
    },
    # 2025~2026 신규
    "클리오 프로 유니크 아이 팔레트 2025": {
        "01 웜누드브라운":       p("warm",["autumn","spring"],  1,3,"shadow","#C8A880",True, "웜 누드 브라운 팔레트",2025),
        "02 쿨핑크모브":         p("cool",["summer","winter"],  2,3,"shadow","#C098B8",True, "쿨 핑크모브 팔레트",2025),
        "03 테라골드":           p("warm",["autumn"],           2,2,"shadow","#B88858",True, "테라 골드 팔레트",2025),
        "04 쿨스모키블루":       p("cool",["winter"],           2,1,"shadow","#7080A8",True, "쿨 스모키 블루",2026),
    },
    "헤라 블랙 쿠션 섀도우": {
        "01 핑크글레이즈":       p("cool",["summer","winter"],  2,3,"shadow","#D0A0B8",True, "쿨 광택 핑크"),
        "03 브론즈테라":         p("warm",["autumn"],           2,2,"shadow","#A07050",True, "웜 브론즈 테라코타"),
        "04 로즈골드미러":       p("warm",["spring","autumn"],  2,3,"shadow","#C89880",True, "로즈골드 미러 쉬머",2025),
        "05 쿨라벤더미러":       p("cool",["summer","winter"],  1,3,"shadow","#A898C8",True, "쿨 라벤더 미러",2025),
        "06 골든브론즈":         p("warm",["autumn"],           3,2,"shadow","#C08840",True, "골든 브론즈 글리터",2026),
    },

    # ═══ BASE ═══════════════════════════════════════════════
    "롬앤 그램 글로잉 사틴 파운데이션": {
        "13N 아이보리":          p("warm",["spring","autumn"],  1,3,"base","#E8C8A8",True, "웜 밝은 피부"),
        "21N 라이트베이지":      p("warm",["autumn"],           1,3,"base","#DEC0A0",True, "웜 자연 피부"),
        "23C 쿨내추럴":          p("cool",["summer"],           1,3,"base","#D8C0B0",True, "쿨 밝은 피부"),
        "25C 쿨베이지":          p("cool",["winter"],           1,2,"base","#D0B8A8",True, "쿨 중간 피부"),
    },
    "에스쁘아 프로 태일러 파운데이션": {
        "1W 아이보리":           p("warm",["spring","autumn"],  1,3,"base","#EAD0B0",True, "웜 피부, 자연 밀착"),
        "2N 내추럴":             p("warm",["autumn"],           1,3,"base","#DEC0A0",True, "웜 중간 피부"),
        "3C 쿨베이지":           p("cool",["summer","winter"],  1,3,"base","#D0B8A8",True, "쿨 베이지"),
    },
    "클리오 킬 커버 파운웨어 쿠션": {
        "1W 워너비아이보리":     p("warm",["spring","autumn"],  1,3,"base","#EED0A8",True, "웜 아이보리 쿠션",2024),
        "2N 내추럴베이지":       p("warm",["autumn"],           1,3,"base","#E0C0A0",True, "웜 내추럴 쿠션",2024),
        "3C 쿨샌드":             p("cool",["summer","winter"],  1,3,"base","#D8C0B0",True, "쿨 샌드 쿠션",2024),
    },
    "헤라 블랙 쿠션 2025": {
        "13 라이트베이지":       p("warm",["spring","autumn"],  1,3,"base","#EAD0B0",True, "웜 라이트 베이지 쿠션",2025),
        "21N 내추럴":            p("warm",["autumn"],           1,3,"base","#DEC0A0",True, "웜 내추럴 쿠션",2025),
        "23C 쿨내추럴":          p("cool",["summer","winter"],  1,3,"base","#D8C0B0",True, "쿨 내추럴 쿠션",2025),
        "25C 쿨베이지":          p("cool",["winter"],           1,2,"base","#D0B8A8",True, "쿨 베이지 쿠션",2025),
    },
    "롬앤 스킨핏 파운데이션 2026": {
        "13W 웜아이보리":        p("warm",["spring","autumn"],  1,3,"base","#ECD0A8",True, "웜 아이보리 피부핏",2026),
        "21W 웜베이지":          p("warm",["autumn"],           1,3,"base","#E0C0A0",True, "웜 베이지 피부핏",2026),
        "23C 쿨내추럴":          p("cool",["summer"],           1,3,"base","#D8C0B0",True, "쿨 내추럴 피부핏",2026),
        "25C 쿨베이지":          p("cool",["winter"],           1,2,"base","#D0B8A8",True, "쿨 베이지 피부핏",2026),
    },
}

# ══════════════════════════════════════════════════════════════
# PC 세부 8톤
# ══════════════════════════════════════════════════════════════
PC = {
    "봄 라이트 웜":   dict(tone="warm",season="spring",emoji="🌸",kw=["맑음","생기","복숭아","산뜻 코랄"],      desc="피부가 밝고 투명감이 있어요. 밝고 산뜻한 코랄·피치 계열이 잘 어울려요.",               best=["코랄","피치","살구","밝은 오렌지","라이트 브라운"],       avoid=["쿨 로즈","버건디","딥 퍼플","그레이"],  bg="linear-gradient(135deg,#FFF8D0,#FFE870)",bd="#C8A000"),
    "봄 비비드 웜":   dict(tone="warm",season="spring",emoji="🌺",kw=["선명함","활기","코랄레드","오렌지"],      desc="맑고 선명한 컬러가 피부에 생기를 더해요. 비비드 코랄~레드가 특히 잘 어울려요.",            best=["코랄레드","오렌지레드","밝은 핑크"],                       avoid=["뮤트 컬러","다크 브라운","그레이"],     bg="linear-gradient(135deg,#FFF5C0,#FFE040)",bd="#B89000"),
    "가을 딥 웜":     dict(tone="warm",season="autumn",emoji="🍂",kw=["깊이","테라코타","어스톤","내추럴"],      desc="황금빛이 도는 깊고 풍부한 웜톤이에요. 테라코타·브릭·카멜이 완벽하게 어울려요.",             best=["테라코타","브릭레드","머스타드","카멜","올리브"],           avoid=["형광","네온","아이시 컬러"],             bg="linear-gradient(135deg,#FFF3B0,#FFD820)",bd="#A88000"),
    "가을 뮤트 웜":   dict(tone="warm",season="autumn",emoji="🌾",kw=["차분함","뮤트","누드","내추럴"],         desc="채도가 낮고 부드러운 웜톤이에요. 뮤트한 브라운~누드 계열이 자연스러워요.",                   best=["카멜누드","웜베이지","머스타드뮤트","로즈브라운"],         avoid=["비비드","형광","쿨 핑크"],              bg="linear-gradient(135deg,#FFF8C8,#FFE850)",bd="#C0A000"),
    "여름 라이트 쿨": dict(tone="cool",season="summer",emoji="🌊",kw=["부드러움","로맨틱","파스텔","파우더리"], desc="밝고 부드러운 쿨톤이에요. 파스텔 핑크·라벤더·뮤트 로즈가 우아하게 어울려요.",                best=["파스텔핑크","라벤더","소프트 로즈"],                       avoid=["오렌지","옐로우","골드 쉬머"],          bg="linear-gradient(135deg,#E8EEFF,#C8D8FF)",bd="#6080C0"),
    "여름 뮤트 쿨":   dict(tone="cool",season="summer",emoji="🩵",kw=["차분함","뮤트","로즈브라운","그레이시"], desc="채도가 낮고 세련된 쿨톤이에요. 뮤트 로즈·그레이핑크 계열이 지적으로 어울려요.",               best=["뮤트 로즈","그레이핑크","라이트 퍼플"],                   avoid=["오렌지","테라코타","골드"],             bg="linear-gradient(135deg,#E0EAFF,#B8CEFF)",bd="#5878C0"),
    "겨울 딥 쿨":     dict(tone="cool",season="winter",emoji="❄️",kw=["선명함","대비","딥레드","플럼"],         desc="선명하고 강한 쿨톤이에요. 딥레드·플럼·버건디가 드라마틱하게 어울려요.",                      best=["딥레드","플럼","버건디","쿨 핑크"],                        avoid=["오렌지","코랄","웜 브라운","베이지"],   bg="linear-gradient(135deg,#D8E4FF,#A8C0FF)",bd="#4060C0"),
    "겨울 비비드 쿨": dict(tone="cool",season="winter",emoji="💙",kw=["대담함","비비드","블루베이스","강렬함"], desc="강렬하고 비비드한 쿨톤이에요. 블루베이스 레드·선명한 핑크가 빛나요.",                          best=["블루베이스 레드","비비드 핑크","퓨어 블랙","퓨어 화이트"], avoid=["파스텔","피치","코랄","웜 브라운"],     bg="linear-gradient(135deg,#D0DCFF,#98B4FF)",bd="#3050C0"),
}

PAIRING = {
    ("spring","blush"):  [("롬앤 베러 댄 치크","코랄리프"),("에뛰드 러블리 쿠키 블러셔","1호 피치"),("NARS 블러쉬","오가즘"),("헤라 센슈얼 파우더 블러셔","01 로즈코랄")],
    ("spring","shadow"): [("클리오 프로 아이 팔레트","06 어텀테라"),("에뛰드 플레이 컬러 아이즈","베어누드"),("페리페라 인크 더 아이섀도우 팔레트","03 코랄핑크"),("롬앤 한올한올 아이섀도우","10 테라핑크")],
    ("autumn","blush"):  [("NARS 블러쉬","딥트로트"),("클리오 킬 커버 더 뉴 치크","03 캐시미어"),("페리페라 블러블러 페이스 블러셔","04 어텀테라"),("헤라 센슈얼 파우더 블러셔","03 딥테라")],
    ("autumn","shadow"): [("클리오 프로 아이 팔레트","04 브라운브릭"),("어반디케이 네이키드 팔레트","NAKED RELOADED"),("맥 아이섀도우 단품","코퍼스파크"),("페리페라 인크 더 아이섀도우 팔레트","01 웜어스")],
    ("summer","blush"):  [("롬앤 베러 댄 치크","스트로베리밀크"),("에뛰드 러블리 쿠키 블러셔","2호 핑크"),("NARS 블러쉬","부에노스아이레스"),("투쿨포스쿨 체크 체크 블러셔","02 플럼체크")],
    ("summer","shadow"): [("클리오 프로 아이 팔레트","03 앤틱핑크"),("에뛰드 플레이 컬러 아이즈","핑크쉐이드"),("어반디케이 네이키드 팔레트","NAKED3"),("페리페라 인크 더 아이섀도우 팔레트","02 쿨로즈")],
    ("winter","blush"):  [("NARS 블러쉬","카마수트라"),("롬앤 베러 댄 치크","쿨로즈"),("페리페라 블러블러 페이스 블러셔","03 미드나잇플럼"),("클리오 킬 커버 더 뉴 치크","07 쿨모브")],
    ("winter","shadow"): [("클리오 프로 아이 팔레트","09 스모키쿨"),("어반디케이 네이키드 팔레트","NAKED3"),("투쿨포스쿨 아트클래스 팔레트","쿨모브"),("클리오 프로 유니크 아이 팔레트 2025","02 쿨핑크모브")],
}

CAT_KR = {"lip":"립","blush":"블러셔","shadow":"섀도우","base":"베이스"}
SEA_KR = {"spring":"봄 웜","autumn":"가을 웜","summer":"여름 쿨","winter":"겨울 쿨"}

def year_tag(yr):
    if yr == 2024: return '<span class="tag t-new24">2024 NEW</span>'
    if yr == 2025: return '<span class="tag t-new25">2025 NEW</span>'
    if yr == 2026: return '<span class="tag t-new26">2026 NEW</span>'
    return ""

def dot_html(hex_col, size=16):
    return f'<span class="dot" style="width:{size}px;height:{size}px;background:{hex_col};"></span>'
def tag_html(t, cls):
    return f'<span class="tag {cls}">{t}</span>'
def tone_tag(t):
    return tag_html("🌞 웜톤" if t=="warm" else "❄️ 쿨톤", f"t-{t}")
def sea_tag(s):
    return tag_html(SEA_KR.get(s,""), f"t-{s}")

def pcard_html(pname, shade, d, fit=""):
    fp = f'<div class="pcard-fit">{fit}</div>' if fit else ""
    yt = year_tag(d.get("year"))
    return f"""
<div class="pcard">
    {dot_html(d['hex'],20)}
    <div class="pcard-info">
        <div class="pcard-name">{pname} {yt}</div>
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

def get_recs(tone, season, cat=None, limit=8, year_filter=None):
    p,g=[],[]
    for pn,shades in DB.items():
        for sh,d in shades.items():
            if not d["avail"]: continue
            if cat and d["category"]!=cat: continue
            if year_filter and d.get("year") not in year_filter: continue
            if d["tone"]==tone and season in d["season"]: p.append((pn,sh,d))
            elif d["tone"]==tone: g.append((pn,sh,d))
    return (p+g)[:limit]


# ══════════════════════════════════════════════════════════════
# 제품 선택 위젯
# ══════════════════════════════════════════════════════════════
def product_picker(prefix, include_disc=False):
    cat_labels = ["전체","립","블러셔","섀도우","베이스"]
    cat_map    = {"전체":None,"립":"lip","블러셔":"blush","섀도우":"shadow","베이스":"base"}

    col_cat, col_pname = st.columns([1, 2])
    with col_cat:
        chosen_lbl = st.selectbox("카", cat_labels, key=f"{prefix}_cat",
                                   label_visibility="collapsed")
    chosen_cat = cat_map[chosen_lbl]

    pnames = sorted({
        pn for pn, shades in DB.items()
        for sh, d in shades.items()
        if (chosen_cat is None or d["category"]==chosen_cat)
        and (include_disc or d["avail"])
    })

    with col_pname:
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
    yt = year_tag(d.get("year"))
    st.markdown(
        f'<div class="mini-info">'
        f'{dot_html(d["hex"],14)}'
        f'{tone_tag(d["tone"])} {"".join(sea_tag(s) for s in d["season"])}'
        f'{disc}{yt}'
        f' &nbsp;<span style="color:var(--muted)">{d["note"]}</span>'
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
    box="rbox-warm" if tone=="warm" else "rbox-cool"
    kw="".join(f"<span class='tag t-{tone}'>{k}</span>" for k in info["kw"])
    st.markdown(f"""
<div class="{box}">
    <div class="rbox-title">{info['emoji']} {pc}</div>
    <div class="rbox-desc">{info['desc']}</div>
    <div style="margin-top:0.9rem">{kw}</div>
</div>""", unsafe_allow_html=True)
    r1,r2=st.columns(2)
    with r1:
        st.markdown("**✅ 잘 어울리는 컬러**")
        for c in info["best"]:  st.markdown(f"· {c}")
    with r2:
        st.markdown("**⛔ 피하면 좋은 컬러**")
        for c in info["avoid"]: st.markdown(f"· {c}")

    st.markdown("#### 🎁 맞춤 추천 제품")
    cc,cy=st.columns([3,2])
    with cc:
        cat_ch=st.radio("",["전체","립","블러셔","섀도우"],horizontal=True,key="res_cat",label_visibility="collapsed")
    with cy:
        yr_ch=st.selectbox("",["전체 연도","2024 신제품","2025 신제품","2026 신제품"],key="res_yr",label_visibility="collapsed")
    cmap={"전체":None,"립":"lip","블러셔":"blush","섀도우":"shadow"}
    ymap={"전체 연도":None,"2024 신제품":[2024],"2025 신제품":[2025],"2026 신제품":[2026]}
    recs=get_recs(res["tone"],res["season"],cat=cmap[cat_ch],limit=8,year_filter=ymap[yr_ch])
    if not recs: st.info("해당 조건의 추천 제품이 없어요."); return
    cols=st.columns(2)
    for i,(pn,sh,d) in enumerate(recs):
        fit="✨ 완벽 매칭" if res["season"] in d["season"] else "👍 어울려요"
        with cols[i%2]: st.markdown(pcard_html(pn,sh,d,fit), unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TAB 2  연계 추천
# ══════════════════════════════════════════════════════════════
def tab_pairing():
    st.markdown('<p class="sec-head">연계 추천 서비스</p>', unsafe_allow_html=True)
    st.markdown('<p class="sec-sub">퍼스널 컬러를 선택하면 립·블러셔·섀도우를 함께 큐레이션해드려요.</p>', unsafe_allow_html=True)
    pc_list=list(PC.keys())
    auto=st.session_state.get("result",{}).get("pc",pc_list[0])
    idx=pc_list.index(auto) if auto in pc_list else 0
    pc_sel=st.selectbox("퍼스널 컬러 선택",pc_list,index=idx,key="pair_pc")
    if st.session_state.get("result"):
        if st.button("🎯 분석 결과 자동 적용"):
            st.session_state["pair_pc"]=st.session_state["result"]["pc"]
            st.rerun()
    info=PC[pc_sel]; tone=info["tone"]; season=info["season"]
    ib="ib-warm" if tone=="warm" else "ib-cool"
    st.markdown(f"""
<div class="info-band {ib}">
    <b style="color:{'#1A1000' if tone=='warm' else '#0A1040'}">{info['emoji']} {pc_sel}</b>
    &nbsp; {tone_tag(tone)} {sea_tag(season)}<br>
    <small style="color:{'#2A2000' if tone=='warm' else '#101850'}">{info['desc']}</small>
</div>""", unsafe_allow_html=True)

    st.markdown("### 💄 추천 립")
    lr=get_recs(tone,season,cat="lip",limit=6)
    lc=st.columns(3)
    for i,(pn,sh,d) in enumerate(lr):
        with lc[i%3]:
            st.markdown(f"""
<div class="pcard" style="flex-direction:column;align-items:flex-start;gap:0.28rem;">
    <div style="display:flex;align-items:center;gap:0.55rem">
        {dot_html(d['hex'],22)} <b style="font-size:0.84rem;color:var(--text)">{pn}</b>{' '+year_tag(d.get('year')) if d.get('year') else ''}
    </div>
    <div style="padding-left:28px">
        <div class="pcard-shade">{sh}</div>
        <div class="pcard-note">{d['note']}</div>
    </div>
</div>""", unsafe_allow_html=True)
    st.divider()
    st.markdown("### 🌸 어울리는 블러셔")
    bk=(season,"blush")
    bi=[(pn,sh,DB[pn][sh]) for pn,sh in PAIRING.get(bk,[]) if pn in DB and sh in DB[pn] and DB[pn][sh]["avail"]] \
       or [(pn,sh,d) for pn,sh,d in get_recs(tone,season,cat="blush",limit=4)]
    bc=st.columns(2)
    for i,(pn,sh,d) in enumerate(bi[:4]):
        with bc[i%2]: st.markdown(pcard_html(pn,sh,d), unsafe_allow_html=True)
    st.divider()
    st.markdown("### ✨ 어울리는 섀도우")
    sk=(season,"shadow")
    si=[(pn,sh,DB[pn][sh]) for pn,sh in PAIRING.get(sk,[]) if pn in DB and sh in DB[pn] and DB[pn][sh]["avail"]] \
       or [(pn,sh,d) for pn,sh,d in get_recs(tone,season,cat="shadow",limit=4)]
    sc=st.columns(2)
    for i,(pn,sh,d) in enumerate(si[:4]):
        with sc[i%2]: st.markdown(pcard_html(pn,sh,d), unsafe_allow_html=True)
    st.divider()
    tips={"spring":"봄 웜톤은 **밝고 산뜻한 코랄·피치 조합**이 최고예요. 골드 액세서리와도 찰떡이에요.",
          "autumn":"가을 웜톤은 **어스톤·테라코타 팔레트**로 풍부한 매력을 살려보세요.",
          "summer":"여름 쿨톤은 **뮤트 핑크·라벤더 조합**이 세련돼요. 실버 액세서리가 피부를 빛나게 해줘요.",
          "winter":"겨울 쿨톤은 **강렬한 컨트라스트**가 매력이에요. 선명한 레드 립 하나로 완성!"}
    st.info(tips.get(season,""))


# ══════════════════════════════════════════════════════════════
# TAB 3  오늘의 조합
# ══════════════════════════════════════════════════════════════
def tab_today():
    st.markdown('<p class="sec-head">오늘의 뷰티 조합</p>', unsafe_allow_html=True)
    st.markdown('<p class="sec-sub">상황·무드를 선택하면 퍼스널 컬러에 맞는 오늘의 메이크업 세트를 추천해드려요.</p>', unsafe_allow_html=True)
    pc_list=list(PC.keys())
    auto=st.session_state.get("result",{}).get("pc",pc_list[0])
    idx=pc_list.index(auto) if auto in pc_list else 0
    co1,co2,co3=st.columns(3)
    with co1: pc_sel=st.selectbox("내 퍼스널 컬러",pc_list,index=idx,key="today_pc")
    with co2: mood=st.selectbox("오늘의 무드",["데일리 내추럴","오피스 룩","데이트 메이크업","파티·이벤트","페스티벌"],key="today_mood")
    with co3: intensity=st.selectbox("강도",["라이트","미디엄","스트롱"],key="today_int")
    info=PC[pc_sel]; tone=info["tone"]; season=info["season"]
    int_map={"라이트":1,"미디엄":2,"스트롱":3}
    ci=int_map[intensity]; cmin=max(1,ci-1); cmax=min(4,ci+1)
    def filtered(cat, limit=3):
        r=[]
        for pn,shades in DB.items():
            for sh,d in shades.items():
                if not d["avail"] or d["category"]!=cat: continue
                if not (cmin<=d["chroma"]<=cmax): continue
                if d["tone"]==tone and season in d["season"]: r.append((pn,sh,d))
                elif d["tone"]==tone: r.append((pn,sh,d))
        if not r: r=[(pn,sh,d) for pn,sh,d in get_recs(tone,season,cat=cat,limit=limit)]
        return r[:limit]
    ib="ib-warm" if tone=="warm" else "ib-cool"
    st.markdown(f"""
<div class="info-band {ib}">
    <b style="color:{'#1A1000' if tone=='warm' else '#0A1040'}">{info['emoji']} {pc_sel} · {mood} · {intensity}</b><br>
    <small style="color:{'#2A2000' if tone=='warm' else '#101850'}">아래 조합으로 오늘 메이크업을 완성해보세요 ✨</small>
</div>""", unsafe_allow_html=True)
    m1,m2,m3=st.columns(3)
    for col,title,cat in [(m1,"💄 립","lip"),(m2,"🌸 블러셔","blush"),(m3,"✨ 섀도우","shadow")]:
        with col:
            st.markdown(f"**{title}**")
            for pn,sh,d in filtered(cat):
                st.markdown(f"""
<div class="pcard" style="flex-direction:column;align-items:flex-start;gap:0.22rem;margin-bottom:0.4rem;">
    <div style="display:flex;align-items:center;gap:0.5rem">
        {dot_html(d['hex'],18)} <b style="font-size:0.81rem;color:var(--text)">{pn}</b>
    </div>
    <div style="padding-left:24px">
        <div class="pcard-shade">{sh} {year_tag(d.get('year'))}</div>
        <div class="pcard-note">{d['note']}</div>
    </div>
</div>""", unsafe_allow_html=True)
    st.divider()
    tips={"데일리 내추럴":"💡 베이스를 가볍게 하고 립 하나로 생기를 더해보세요.",
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
    st.markdown('<p class="sec-sub">카테고리·톤·계절·출시연도로 필터링해서 전체 제품을 살펴보세요.</p>', unsafe_allow_html=True)
    f1,f2,f3,f4=st.columns(4)
    with f1: fcat =st.selectbox("카테고리",["전체","립","블러셔","섀도우","베이스"],key="br_cat")
    with f2: ftone=st.selectbox("톤",["전체","웜톤","쿨톤"],key="br_tone")
    with f3: fsea =st.selectbox("계절",["전체","봄 웜","가을 웜","여름 쿨","겨울 쿨"],key="br_sea")
    with f4: fyr  =st.selectbox("출시연도",["전체","2024","2025","2026","클래식"],key="br_yr")
    show_disc=st.checkbox("단종 제품도 보기",value=False)
    cmap={"전체":None,"립":"lip","블러셔":"blush","섀도우":"shadow","베이스":"base"}
    tmap={"전체":None,"웜톤":"warm","쿨톤":"cool"}
    smap={"전체":None,"봄 웜":"spring","가을 웜":"autumn","여름 쿨":"summer","겨울 쿨":"winter"}
    fc,ft,fs=cmap[fcat],tmap[ftone],smap[fsea]
    rows=[]
    for pn,shades in DB.items():
        for sh,d in shades.items():
            if not show_disc and not d["avail"]: continue
            if fc and d["category"]!=fc: continue
            if ft and d["tone"]!=ft: continue
            if fs and fs not in d["season"]: continue
            if fyr=="2024" and d.get("year")!=2024: continue
            if fyr=="2025" and d.get("year")!=2025: continue
            if fyr=="2026" and d.get("year")!=2026: continue
            if fyr=="클래식" and d.get("year") is not None: continue
            rows.append((pn,sh,d))
    st.markdown(f"<small style='color:var(--muted);font-weight:600'>{len(rows)}개 제품</small>", unsafe_allow_html=True)
    if not rows: st.info("조건에 맞는 제품이 없어요."); return
    for i in range(0,len(rows),3):
        cols=st.columns(3)
        for j,(pn,sh,d) in enumerate(rows[i:i+3]):
            with cols[j]:
                disc=" <span class='tag t-disc'>단종</span>" if not d["avail"] else ""
                st.markdown(f"""
<div class="pcard" style="flex-direction:column;align-items:flex-start;border-radius:12px;padding:0.9rem;gap:0.35rem;">
    <div style="display:flex;align-items:center;gap:0.6rem">
        {dot_html(d['hex'],22)}
        <div>
            <div class="pcard-name">{pn}{disc}</div>
            <div class="pcard-shade">{sh} {year_tag(d.get('year'))}</div>
        </div>
    </div>
    <div class="pcard-note">{d['note']}</div>
    <div>{tone_tag(d['tone'])} {''.join(sea_tag(s) for s in d['season'])} {tag_html(CAT_KR.get(d['category'],''),'t-cat')}</div>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TAB 5  컬러 가이드
# ══════════════════════════════════════════════════════════════
def tab_guide():
    st.markdown('<p class="sec-head">퍼스널 컬러 가이드</p>', unsafe_allow_html=True)
    st.markdown('<p class="sec-sub">세부 8톤의 특징과 뷰티 스타일링 팁을 한눈에 확인하세요.</p>', unsafe_allow_html=True)
    for pc_name,info in PC.items():
        tone=info["tone"]
        with st.expander(f"{info['emoji']}  {pc_name}"):
            a,b=st.columns([3,2])
            with a:
                kw="".join(f"<span class='tag t-{tone}'>{k}</span>" for k in info["kw"])
                tc="#1A1000" if tone=="warm" else "#0A1040"
                st.markdown(f"""
<div style="background:{info['bg']};border:2px solid {info['bd']};border-radius:13px;padding:1.2rem 1.5rem;">
    <b style="font-size:1rem;color:{tc}">{info['emoji']} {pc_name}</b><br>
    <div style="font-size:0.85rem;color:{tc};margin:0.45rem 0;line-height:1.7;opacity:0.85">{info['desc']}</div>
    <div>{kw}</div>
</div>""", unsafe_allow_html=True)
            with b:
                st.markdown("**✅ 어울리는 컬러**")
                for c in info["best"]: st.markdown(f"· {c}")
                st.markdown("**⛔ 피할 컬러**")
                for c in info["avoid"]: st.markdown(f"· {c}")
            st.markdown("**🛍️ 대표 추천 제품**")
            recs=get_recs(tone,info["season"],limit=4)
            gc=st.columns(4)
            for i,(pn,sh,d) in enumerate(recs):
                with gc[i]:
                    st.markdown(f"""
<div style="text-align:center;padding:0.45rem 0.2rem;">
    <div style="width:30px;height:30px;border-radius:50%;background:{d['hex']};margin:0 auto 0.3rem;border:2px solid rgba(0,0,0,0.12);"></div>
    <div style="font-size:0.73rem;font-weight:600;color:var(--text);line-height:1.3">{pn}</div>
    <div style="font-size:0.67rem;color:var(--muted)">{sh}</div>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════
def main():
    st.markdown("""
<div class="hero-title">TONE<em>ME</em></div>
<div class="hero-bar"></div>
<div class="hero-sub">퍼스널 컬러 기반 뷰티 큐레이터 · 세부 8톤 분석 · 국내 구매 가능 · 2024–2026 신제품 포함</div>
""", unsafe_allow_html=True)

    t1,t2,t3,t4,t5=st.tabs([
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

    st.markdown('<div class="footer">TONEME · 단종 제품은 추천 제외 · 국내 구매 가능 · 2024–2026 신제품 포함</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
