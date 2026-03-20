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
    --bg:      #FEFAE8;
    --surface: #FFFEF5;
    --border:  #D8CC50;
    --accent:  #7A5E0A;
    --text:    #1C1400;
    --sub:     #3E3200;
    --muted:   #5A4A00;
    --div:     #E4D860;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: var(--bg) !important;
    font-family: 'Noto Sans KR', sans-serif;
    color: var(--text);
}
[data-testid="stSidebar"] { display: none; }
.block-container { padding: 2.5rem 3rem 6rem !important; max-width: 1060px !important; }

/* HERO */
.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3rem; font-weight: 300; letter-spacing: 0.1em;
    color: var(--text); line-height: 1; text-transform: uppercase;
}
.hero-title em { font-style: italic; color: var(--accent); }
.hero-bar { width: 44px; height: 2px; background: var(--accent); margin: 0.65rem 0 0.7rem; border-radius: 2px; }
.hero-sub { font-size: 0.78rem; color: var(--sub); letter-spacing: 0.04em; margin-bottom: 2rem; }

/* TABS */
.stTabs [data-baseweb="tab-list"] { gap:0; background:transparent; border-bottom:1.5px solid var(--div); }
.stTabs [data-baseweb="tab"] {
    font-size:0.85rem; font-weight:500; color:var(--muted);
    padding:0.55rem 1.3rem; border-radius:0; background:transparent; border:none;
}
.stTabs [aria-selected="true"] {
    color:var(--text) !important; background:transparent !important;
    border-bottom:2px solid var(--accent) !important; font-weight:700 !important;
}

/* SECTION */
.sec-head { font-size:1.1rem; font-weight:700; color:var(--text); margin-bottom:0.2rem; }
.sec-sub  { font-size:0.81rem; color:var(--sub); line-height:1.7; margin-bottom:1.1rem; }
.col-label {
    font-size:0.76rem; font-weight:700; color:var(--text);
    padding-bottom:0.55rem; border-bottom:1.5px solid var(--div);
    margin-bottom:0.85rem;
}

/* ── SELECTBOX ── */
.stSelectbox label { display:none !important; }
.stSelectbox > div > div {
    border-radius:8px !important; border-color:var(--div) !important;
    font-size:0.85rem !important; background:var(--surface) !important;
    color:var(--text) !important; font-weight:500 !important;
}

/* ── RADIO — 핵심 가독성 수정 ── */
.stRadio > label {
    color: var(--text) !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
}
.stRadio > div > label {
    color: var(--text) !important;
    font-weight: 500 !important;
    font-size: 0.83rem !important;
    background: var(--surface) !important;
    border: 1.5px solid var(--div) !important;
    border-radius: 8px !important;
    padding: 0.3rem 0.8rem !important;
    cursor: pointer !important;
}
.stRadio > div > label:hover {
    border-color: var(--accent) !important;
    color: var(--accent) !important;
}
/* 선택된 라디오 버튼 */
.stRadio > div > label[data-checked="true"],
.stRadio [aria-checked="true"] ~ label,
.stRadio input:checked + div {
    background: var(--accent) !important;
    color: #FFF8D8 !important;
    border-color: var(--accent) !important;
}
/* 체크박스 */
.stCheckbox > label, .stCheckbox label {
    color: var(--text) !important;
    font-weight: 500 !important;
    font-size: 0.83rem !important;
}

/* ── 선택 후 미니 정보 ── */
.mini-info {
    display:flex; align-items:center; gap:0.5rem;
    padding:0.5rem 0.85rem;
    background:#FFFFF0; border:1.5px solid var(--accent);
    border-radius:8px; margin-top:0.3rem; font-size:0.76rem; color:var(--sub);
}
.mini-dot { width:13px; height:13px; border-radius:50%; flex-shrink:0; border:1.5px solid rgba(0,0,0,0.12); }

/* ── TAGS ── */
.tag {
    display:inline-block; padding:0.17rem 0.62rem;
    border-radius:100px; font-size:0.69rem; font-weight:600; margin:0.04rem;
}
.t-warm   { background:#4A2800; color:#FFE8C0; }
.t-cool   { background:#162068; color:#C5D8FF; }
.t-spring { background:#4A1C00; color:#FFD8B8; }
.t-summer { background:#141870; color:#CACAFF; }
.t-autumn { background:#3C2000; color:#FFD8A8; }
.t-winter { background:#101C68; color:#BED0FF; }
.t-cat    { background:#302400; color:#FFE898; }
.t-disc   { background:#555;    color:#EEE;   }
.t-new    { background:#0A3A18; color:#A0FFB8; }

/* ── DOT ── */
.dot { display:inline-block; border-radius:50%; border:1.5px solid rgba(0,0,0,0.12); vertical-align:middle; flex-shrink:0; }

/* ── PCARD ── */
.pcard {
    display:flex; align-items:flex-start; gap:0.75rem;
    background:var(--surface); border:1px solid var(--div);
    border-radius:10px; padding:0.8rem 0.95rem; margin-bottom:0.45rem;
}
.pcard-right { flex:1; min-width:0; }
.pcard-top   { display:flex; align-items:center; justify-content:space-between; gap:0.4rem; margin-bottom:0.18rem; }
.pcard-name  { font-weight:600; font-size:0.85rem; color:var(--text); line-height:1.3; }
.pcard-fit   { font-size:0.68rem; color:var(--accent); white-space:nowrap; font-weight:700; flex-shrink:0; }
.pcard-shade { font-size:0.76rem; color:var(--muted); font-weight:500; }
.pcard-note  { font-size:0.71rem; color:var(--sub); margin-top:0.12rem; opacity:0.85; }

/* ── RESULT BOX ── */
.rbox-warm {
    background:linear-gradient(135deg,#FFF8C0,#FFE030);
    border:1.5px solid #A88000; border-radius:16px;
    padding:1.7rem 2rem; margin-bottom:1.2rem;
}
.rbox-cool {
    background:linear-gradient(135deg,#DDE8FF,#AABEFF);
    border:1.5px solid #3860C0; border-radius:16px;
    padding:1.7rem 2rem; margin-bottom:1.2rem;
}
.rbox-warm .rbox-title { font-family:'Cormorant Garamond',serif; font-size:2rem; font-weight:500; color:#1C1000; margin-bottom:0.4rem; }
.rbox-cool .rbox-title { font-family:'Cormorant Garamond',serif; font-size:2rem; font-weight:500; color:#080C30; margin-bottom:0.4rem; }
.rbox-warm .rbox-desc { font-size:0.87rem; line-height:1.75; font-weight:500; color:#2A1E00; }
.rbox-cool .rbox-desc { font-size:0.87rem; line-height:1.75; font-weight:500; color:#0A1240; }

/* 결과 박스 아래 카테고리 선택 라디오 — 배경 대비 맞춤 */
.rbox-radio .stRadio > div > label {
    background: rgba(255,255,255,0.7) !important;
    border-color: rgba(0,0,0,0.2) !important;
    color: var(--text) !important;
}

/* ── INFO BAND ── */
.info-band { border-radius:10px; padding:0.95rem 1.25rem; margin-bottom:1rem; }
.ib-warm { background:linear-gradient(135deg,#FFF8C0,#FFE030); border:1.5px solid #A88000; }
.ib-cool { background:linear-gradient(135deg,#DDE8FF,#AABEFF); border:1.5px solid #3860C0; }

/* ── BUTTON ── */
.stButton > button {
    background:var(--accent) !important; color:#FFF8D8 !important;
    border:none !important; border-radius:8px !important;
    padding:0.62rem 1.8rem !important; font-size:0.87rem !important;
    font-weight:700 !important; width:100% !important;
}
.stButton > button:hover { filter:brightness(1.15) !important; }

/* ── MISC ── */
details summary { font-size:0.84rem !important; color:var(--text) !important; font-weight:600 !important; }
hr { border-color:var(--div) !important; margin:1.3rem 0 !important; }
.stSuccess, .stWarning, .stInfo { border-radius:9px !important; font-size:0.84rem !important; }
p, li, .stMarkdown { color:var(--text) !important; }
.footer { text-align:center; font-size:0.72rem; color:var(--muted); padding:1.5rem 0 2rem; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# DB
# year: 출시년도 (None=클래식, 2024, 2025, 2026)
# new_mar26: True = 2026년 3월 출시 → NEW 태그
# ══════════════════════════════════════════════════════════════
def p(tone, season, chroma, value, cat, hx, avail, note, year=None, new=False):
    return dict(tone=tone, season=season, chroma=chroma, value=value,
                category=cat, hex=hx, avail=avail, note=note, year=year, new=new)

DB = {
    # ═══ LIP ════════════════════════════════════════════════

    # 롬앤 더 쥬시 래스팅 틴트 (스테디셀러)
    "롬앤 더 쥬시 래스팅 틴트": {
        "02 누카다미아":    p("warm",["autumn"],          1,2,"lip","#9A6858",True,"MLBB 누드 레드브라운, 웜톤 데일리"),
        "03 베어 그레이프": p("cool",["summer","winter"], 1,2,"lip","#A87890",True,"차분한 포도빛 핑크베이지"),
        "06 피그피그":      p("cool",["summer","winter"], 2,2,"lip","#C47090",True,"물광 마감, 뮤트 로즈"),
        "07 쥬쥬브":        p("warm",["spring","autumn"], 3,2,"lip","#C45858",True,"생기있는 레드베리"),
        "12 체리밤":        p("cool",["winter"],          4,1,"lip","#9A2840",True,"딥 체리 레드"),
        "13 잇 도토리":     p("warm",["autumn"],          2,2,"lip","#A05038",True,"가을빛 브릭 레드"),
        "17 플럼 콕":       p("cool",["winter"],          3,1,"lip","#8A3860",True,"고혹적인 검붉은 플럼"),
        "19 아몬드 로즈":   p("cool",["summer"],          2,2,"lip","#B87888",True,"차분한 말린 장미빛"),
        "23 피치피치미":    p("warm",["spring"],          3,3,"lip","#E09070",True,"과즙감 복숭아 코랄"),
        "27 핑크 팝시클":   p("cool",["summer"],          3,3,"lip","#E070A8",True,"선명한 핑크에 흰기 한 방울"),
        "28 베어 피그":     p("cool",["summer","winter"], 2,2,"lip","#B07898",True,"무화과에 우유 한 방울, 모브"),
        "29 파파야 잼":     p("warm",["spring","autumn"], 2,3,"lip","#D09878",True,"데일리 파파야 MLBB"),
        "31 탠드 코코":     p("warm",["autumn"],          1,2,"lip","#906050",True,"차분한 코코넛 브라운",2024),
        "32 태니 구아바":   p("warm",["spring"],          2,3,"lip","#D88870",True,"햇빛에 구운 핑크 구아바",2024),
        "33 알로하 쥬시":   p("warm",["spring"],          3,3,"lip","#E07860",True,"하와이안 청량 코랄",2024),
    },

    # 롬앤 블러 퍼지 틴트 (실제 컬러 확인)
    "롬앤 블러 퍼지 틴트": {
        "01 포멜로코":  p("warm",["spring"],          2,3,"lip","#D07860",True,"부드러운 혈색 코랄, 봄웜 베스트"),
        "02 로지엔탈":  p("warm",["spring","autumn"], 1,2,"lip","#C07880",True,"톤다운 MLBB 로즈, 봄·가을웜 가능"),
        "03 머스키":    p("warm",["autumn"],          1,2,"lip","#A07060",True,"머스키 웜 누드브라운"),
        "04 라드우드":  p("warm",["autumn"],          2,2,"lip","#9A5848",True,"레드우드 브릭 웜"),
        "05 비비캔디":  p("cool",["winter"],          3,3,"lip","#E050A0",True,"비비드 퓨어핑크, 겨울쿨 브라이트"),
        "06 모비쉬":    p("cool",["summer"],          1,2,"lip","#9A7888",True,"그레이시 모브, 여름쿨 뮤트 특화"),
        "07 쿨로즈업":  p("cool",["winter","summer"], 2,2,"lip","#A86880",True,"채도 낮은 쿨 플럼로즈"),
        "08 커런트잼":  p("cool",["winter"],          4,2,"lip","#A02840",True,"선명·딥한 베리레드, 쿨브라이트"),
        "09 코랄쥬빌레":p("warm",["spring"],          3,3,"lip","#E07858",True,"코랄 쥬빌레, 밝은 웜코랄",2024),
        "10 퍼지레드":  p("warm",["autumn"],          3,2,"lip","#B83838",True,"퍼지 레드 웜",2024),
        "11 푸시아바이브":p("cool",["winter"],        4,2,"lip","#C02870",True,"비비드 푸시아 쿨",2024),
        "12 웜밍업":    p("warm",["spring","autumn"], 2,3,"lip","#D09078",True,"웜밍업 코랄피치",2025),
        "13 쿨링업":    p("cool",["summer","winter"], 2,2,"lip","#B07888",True,"쿨링업 쿨로즈",2025),
        "14 언로즈":    p("cool",["summer"],          1,3,"lip","#C89AA8",True,"연한 쿨 로즈, 여름쿨 파스텔",2025),
        "15 베리피즈":  p("cool",["winter","summer"], 2,2,"lip","#A86888",True,"옅은 플럼빛 베리핑크",2025),
    },

    # 페리페라 잉크 무드 글로이 틴트
    "페리페라 잉크 무드 글로이 틴트": {
        "01 쿨오프코랄":     p("warm",["spring"],           3,3,"lip","#E07860",True,"밝은 코랄오렌지"),
        "02 맘찍피치":       p("warm",["spring","autumn"],  2,3,"lip","#E09878",True,"과즙 피치 MLBB"),
        "03 맘찍로즈":       p("cool",["summer"],           2,3,"lip","#D088A0",True,"부동의 1위, 뮤트 로즈핑크"),
        "04 베이지핑크":     p("warm",["spring","autumn"],  1,3,"lip","#D0A090",True,"자연스러운 베이지핑크"),
        "05 로즈누드":       p("cool",["summer","winter"],  1,2,"lip","#B07880",True,"차분한 쿨 로즈누드"),
        "06 초코브릭":       p("warm",["autumn"],           2,2,"lip","#8A4838",True,"초콜릿 브릭 레드"),
        "07 딥레드":         p("cool",["winter"],           4,2,"lip","#A02840",True,"강렬한 쿨 레드"),
        "08 베리핑크":       p("cool",["summer"],           3,3,"lip","#D06898",True,"선명한 베리핑크"),
        "09 코랄프레쉬":     p("warm",["spring"],           3,3,"lip","#E06848",True,"생생한 코랄"),
        "10 핑크하구마":     p("cool",["summer","winter"],  2,3,"lip","#D080A8",True,"고구마빛 쿨핑크",2025),
        "11 뮤트모브":       p("cool",["summer"],           1,2,"lip","#A88090",True,"뮤트 모브, 여름쿨 뮤트",2025),
    },

    # 페리페라 오버 블러 틴트 (2024 퍼스널컬러 특화 7종)
    "페리페라 오버 블러 틴트": {
        "01 봄라이트웜":  p("warm",["spring"],          2,3,"lip","#E09878",True,"봄 라이트웜 특화 — 피치코랄",2024),
        "02 봄비비드웜":  p("warm",["spring"],          3,3,"lip","#E07060",True,"봄 비비드웜 특화 — 선명코랄",2024),
        "03 여름라이트쿨":p("cool",["summer"],          1,3,"lip","#D0A0B8",True,"여름 라이트쿨 특화 — 파스텔핑크",2024),
        "04 여름뮤트쿨":  p("cool",["summer"],          1,2,"lip","#B88898",True,"여름 뮤트쿨 특화 — 로즈누드",2024),
        "05 가을딥웜":    p("warm",["autumn"],          2,2,"lip","#9A6050",True,"가을 딥웜 특화 — 브릭누드",2024),
        "06 가을뮤트웜":  p("warm",["autumn"],          1,2,"lip","#A07868",True,"가을 뮤트웜 특화 — 뮤트베이지",2024),
        "07 겨울딥쿨":    p("cool",["winter"],          3,1,"lip","#7A3858",True,"겨울 딥쿨 특화 — 딥플럼",2024),
    },

    # 클리오 듀이 시럽 틴트 (올리브영 인기)
    "클리오 듀이 시럽 틴트": {
        "001 한남동코랄뷰":  p("warm",["spring"],           3,3,"lip","#E07858",True,"오렌지베이스 코랄, 유리알 광택"),
        "002 성수동로즈뷰":  p("cool",["summer"],           2,3,"lip","#D080A0",True,"쿨 로즈뷰 촉촉광"),
        "003 홍대핑크뷰":    p("cool",["summer","winter"],  3,3,"lip","#E060A0",True,"선명한 핑크뷰"),
        "004 청담동누드뷰":  p("warm",["autumn"],           1,2,"lip","#A07868",True,"차분한 웜 누드뷰"),
        "005 압구정버건디뷰":p("cool",["winter"],           3,2,"lip","#8A2850",True,"딥 버건디뷰 쿨",2025),
        "006 이태원테라뷰":  p("warm",["autumn"],           2,2,"lip","#A06048",True,"웜 테라코타뷰",2025),
    },

    # 이더앤 듀이 시럽 틴트 (2026.03 국내단독 출시 — NEW)
    "이더앤 듀이 시럽 틴트": {
        "01 셔벗피치":    p("warm",["spring"],           2,3,"lip","#E0A078",True,"쫀득 셔벗 피치 웜",2026,True),
        "02 코랄봄빛":    p("warm",["spring"],           3,3,"lip","#E07858",True,"봄빛 코랄 웜",2026,True),
        "03 딸기라떼":    p("cool",["summer"],           2,3,"lip","#D08898",True,"딸기라떼 쿨핑크",2026,True),
        "04 로즈무드":    p("cool",["summer","winter"],  2,2,"lip","#C07888",True,"로즈무드 쿨",2026,True),
        "05 베리스무디":  p("cool",["winter"],           3,2,"lip","#A03868",True,"딥베리 스무디 쿨",2026,True),
        "06 복숭아밀크":  p("warm",["spring","autumn"],  1,3,"lip","#E0A888",True,"복숭아밀크 웜누드",2026,True),
        "07 체리블라썸":  p("cool",["spring","summer"],  2,3,"lip","#D888A8",True,"체리블라썸 쿨핑크",2026,True),
        "08 피그허니":    p("warm",["autumn"],           2,2,"lip","#A06858",True,"무화과허니 웜브라운",2026,True),
        "09 딥플럼":      p("cool",["winter"],           3,1,"lip","#7A3060",True,"딥플럼 쿨다크",2026,True),
        "10 테라코타썬":  p("warm",["autumn"],           3,2,"lip","#B06040",True,"테라코타 선셋 웜",2026,True),
        "11 라즈베리소다":p("cool",["summer","winter"],  3,3,"lip","#C04878",True,"라즈베리 소다 쿨",2026,True),
        "12 뉴드코럴":    p("warm",["spring","autumn"],  2,3,"lip","#D09080",True,"뉴드코럴 웜MLBB",2026,True),
        "13 스모키모브":  p("cool",["winter"],           2,1,"lip","#806070",True,"스모키 모브 쿨다크",2026,True),
    },

    # 힌스 로 글로우 젤 틴트 (2026.03 올영픽 — NEW)
    "힌스 로 글로우 젤 틴트": {
        "01 누드코랄":   p("warm",["spring","autumn"],  2,3,"lip","#D09878",True,"로 글로우 누드코랄",2026,True),
        "02 로즈베이지": p("cool",["summer"],           1,3,"lip","#C898A8",True,"로즈베이지 쿨누드",2026,True),
        "03 딸기레드":   p("cool",["winter"],           4,2,"lip","#C02848",True,"딸기레드 쿨브라이트",2026,True),
        "04 코랄피치":   p("warm",["spring"],           3,3,"lip","#E08868",True,"과즙 코랄피치 웜",2026,True),
        "05 피그브라운": p("warm",["autumn"],           2,2,"lip","#9A6050",True,"피그브라운 웜",2026,True),
        "06 베리핑크":   p("cool",["summer","winter"],  3,3,"lip","#D060A0",True,"베리핑크 쿨",2026,True),
    },

    # 맥 리프스틱
    "맥 리프스틱": {
        "Whirl":              p("warm",["autumn"],          1,2,"lip","#906060",True,"국민 누드브라운, 가을 완벽템"),
        "Ruby Woo":           p("cool",["winter"],          4,2,"lip","#C02030",True,"클래식 블루베이스 레드"),
        "Velvet Teddy":       p("warm",["autumn"],          1,2,"lip","#8A5848",True,"따뜻한 뮤트 누드"),
        "Brave":              p("warm",["spring","autumn"], 1,3,"lip","#C09080",True,"피치 누드"),
        "Flat Out Fabulous":  p("cool",["winter"],          3,1,"lip","#803060",True,"다크 플럼"),
    },

    # 에뛰드 픽싱 틴트
    "에뛰드 픽싱 틴트": {
        "01 레드":         p("cool",["winter"],          4,2,"lip","#C02030",True,"클래식 쿨 레드"),
        "03 멜로우피치":   p("warm",["spring"],          2,3,"lip","#E09068",True,"복숭아빛 코랄, 봄 생기"),
        "04 뮤트로즈":     p("cool",["summer"],          2,2,"lip","#C07890",True,"뮤트 쿨로즈"),
        "05 미드나잇모브":p("cool",["winter","summer"],  2,2,"lip","#987090",True,"보랏빛 뮤트 핑크"),
        "06 소프트월넛":   p("warm",["autumn"],          1,2,"lip","#906858",True,"웜 누드, 피부 밀착"),
        "08 베리핑크":     p("cool",["summer"],          3,3,"lip","#C870A0",True,"선명 핑크"),
    },

    # ═══ BLUSH ══════════════════════════════════════════════

    "롬앤 베러 댄 치크": {
        "피치칩":          p("warm",["spring","autumn"],  2,3,"blush","#E8A878",True,"황금 피치, 웜톤 생기"),
        "스트로베리밀크":  p("cool",["summer"],           2,3,"blush","#D898A8",True,"딸기우유빛 쿨 핑크"),
        "코랄리프":        p("warm",["spring"],           3,3,"blush","#E89070",True,"생생한 코랄"),
        "쿨로즈":          p("cool",["winter","summer"],  2,2,"blush","#C880A0",True,"블루베이스 쿨 로즈"),
        "누디피치":        p("warm",["autumn"],           1,2,"blush","#D0988A",True,"웜 누디 피치"),
        "애프리콧밀크":    p("warm",["spring","summer"],  1,3,"blush","#E8C0A0",True,"흰기 돌아 청순한 애프리콧밀크",2025),
        "쿨코튼":          p("cool",["summer"],           1,3,"blush","#E0B8C8",True,"쿨 코튼 파스텔핑크",2025),
    },

    "에뛰드 러블리 쿠키 블러셔": {
        "1호 피치":   p("warm",["spring"],          2,3,"blush","#EDA880",True,"부드러운 피치"),
        "2호 핑크":   p("cool",["summer"],          2,3,"blush","#E0A0B8",True,"밝은 쿨핑크"),
        "3호 오렌지": p("warm",["autumn","spring"], 3,3,"blush","#E89060",True,"선명한 오렌지"),
        "5호 베이지": p("warm",["autumn"],          1,2,"blush","#C8A888",True,"내추럴 베이지 음영"),
    },

    "클리오 킬 커버 더 뉴 치크": {
        "02 다이닝로즈":p("cool",["summer","winter"], 2,3,"blush","#D890A8",True,"뮤트 쿨 로즈"),
        "03 캐시미어":  p("warm",["autumn"],          1,2,"blush","#C8A090",True,"웜 캐시미어 베이지"),
        "05 보나피치":  p("warm",["spring","summer"], 2,3,"blush","#E8A890",True,"따뜻한 코랄피치"),
        "07 쿨모브":    p("cool",["winter"],          2,2,"blush","#B880A8",True,"딥 쿨모브"),
    },

    "NARS 블러쉬": {
        "오가즘":           p("warm",["spring","summer"], 2,3,"blush","#E09888",True,"골드쉬머 피치핑크, 국민템"),
        "딥트로트":         p("warm",["autumn"],          2,2,"blush","#C07860",True,"깊은 테라코타"),
        "카마수트라":       p("cool",["winter"],          3,2,"blush","#B86080",True,"딥 쿨로즈"),
        "부에노스아이레스": p("cool",["summer"],          2,3,"blush","#D898B0",True,"소프트 쿨핑크"),
    },

    "페리페라 블러블러 페이스 블러셔": {
        "01 코코피치":    p("warm",["spring","autumn"], 2,3,"blush","#E0A080",True,"코코넛 피치"),
        "02 쿨로즈퍼지":  p("cool",["summer"],          2,3,"blush","#D8A0B8",True,"퍼지 쿨 로즈핑크"),
        "03 미드나잇플럼":p("cool",["winter"],          3,2,"blush","#A06888",True,"딥 쿨 플럼"),
        "04 어텀테라":    p("warm",["autumn"],          2,2,"blush","#B07058",True,"어스 테라코타",2024),
        "05 스프링코랄":  p("warm",["spring"],          3,3,"blush","#E09070",True,"봄 코랄핑크",2024),
    },

    # VDL 치크스테인 블러셔 (2026.03 올영픽 재출시요청 1위 — NEW)
    "VDL 치크스테인 블러셔": {
        "01 코랄스테인":  p("warm",["spring"],           3,3,"blush","#E09070",True,"스테인 발색 코랄 웜",2026,True),
        "02 로즈스테인":  p("cool",["summer"],           2,3,"blush","#D898B8",True,"스테인 발색 쿨로즈",2026,True),
        "03 베리스테인":  p("cool",["winter"],           3,2,"blush","#A86888",True,"스테인 딥베리 쿨",2026,True),
        "04 피치스테인":  p("warm",["spring","autumn"],  2,3,"blush","#E8A880",True,"스테인 피치 웜",2026,True),
    },

    # 3CE 무드레시피 페이스 블러쉬
    "3CE 무드레시피 페이스 블러쉬": {
        "NUDE PEACH":    p("warm",["spring","summer"], 1,3,"blush","#E8B898",True,"실키 누드피치, 뽀얀 블러",2025),
        "ROSE PINK":     p("cool",["summer"],          2,3,"blush","#E098B8",True,"쿨 로즈핑크",2025),
        "CORAL RED":     p("warm",["spring"],          3,3,"blush","#E88870",True,"코랄레드 웜",2025),
        "DUSTY ROSE":    p("cool",["summer","winter"], 2,2,"blush","#C088A0",True,"더스티 쿨로즈",2025),
    },

    # 헤라 센슈얼 파우더 블러셔
    "헤라 센슈얼 파우더 블러셔": {
        "01 로즈코랄": p("warm",["spring","summer"], 2,3,"blush","#E09888",True,"로즈코랄 쉬머"),
        "02 쿨핑크":   p("cool",["summer"],          2,3,"blush","#D898B8",True,"쿨핑크 쉬머"),
        "03 딥테라":   p("warm",["autumn"],          2,2,"blush","#B07060",True,"딥 테라코타 쉬머"),
    },

    # ═══ SHADOW ═════════════════════════════════════════════

    "클리오 프로 아이 팔레트": {
        "03 앤틱핑크":  p("cool",["summer","winter"], 2,3,"shadow","#D8A8B8",True,"쿨톤 핑크 멀티"),
        "04 브라운브릭":p("warm",["autumn"],          2,2,"shadow","#987060",True,"웜 브라운 전문"),
        "06 어텀테라":  p("warm",["autumn","spring"], 2,2,"shadow","#B07858",True,"테라코타 어텀"),
        "09 스모키쿨":  p("cool",["winter"],          2,1,"shadow","#706880",True,"쿨톤 스모키"),
        "10 웜코퍼":    p("warm",["autumn","spring"], 3,2,"shadow","#C08050",True,"웜 코퍼 쉬머",2024),
        "11 쿨모브":    p("cool",["summer","winter"], 2,2,"shadow","#9878A8",True,"쿨 모브 팔레트",2024),
    },

    "클리오 프로 아이 팔레트 에어": {
        "01 웜누드어스": p("warm",["autumn","spring"], 1,3,"shadow","#C8A880",True,"웜 누드 어스"),
        "02 쿨로즈모브": p("cool",["summer","winter"], 2,3,"shadow","#C090B0",True,"쿨 로즈모브"),
        "03 테라골드":   p("warm",["autumn"],          3,2,"shadow","#B08858",True,"테라골드"),
        "04 쿨스모키":   p("cool",["winter"],          2,1,"shadow","#706888",True,"쿨 스모키"),
    },

    "에뛰드 플레이 컬러 아이즈": {
        "베어누드":       p("warm",["autumn","spring"], 1,3,"shadow","#C8B098",True,"웜 베이지 데일리"),
        "라즈베리초콜릿": p("cool",["winter","summer"], 2,2,"shadow","#907880",True,"쿨 다크베리"),
        "핑크쉐이드":     p("cool",["summer"],          2,3,"shadow","#D8A8B8",True,"소프트 쿨핑크"),
        "브라운토피":     p("warm",["autumn"],          2,2,"shadow","#987060",False,"웜 토피브라운 ★단종"),
    },

    # 데이지크 섀도우 팔레트 (2025 올영어워즈 — 올리브영 실제 노출)
    "데이지크 아이섀도우 팔레트": {
        "01 웜어스":    p("warm",["autumn","spring"], 2,2,"shadow","#B09070",True,"웜 어스톤 데이지크",2025),
        "02 쿨로즈":    p("cool",["summer","winter"], 2,3,"shadow","#C090A8",True,"쿨 로즈 데이지크",2025),
        "03 선셋코퍼":  p("warm",["autumn"],          3,2,"shadow","#B07848",True,"선셋 코퍼 웜",2025),
        "04 쿨스모키":  p("cool",["winter"],          2,1,"shadow","#707088",True,"쿨 스모키",2025),
    },

    "어반디케이 네이키드 팔레트": {
        "NAKED3":         p("cool",["summer","winter"], 2,3,"shadow","#C090A0",True,"쿨 로즈 뉴트럴 — 국내 구매가능"),
        "NAKED RELOADED": p("warm",["autumn","spring"], 2,2,"shadow","#B09070",True,"웜 뉴트럴 — 국내 구매가능"),
    },

    "맥 아이섀도우 단품": {
        "코퍼스파크": p("warm",["autumn"],          3,2,"shadow","#C07840",True,"쉬머 구리빛"),
        "브라운다운": p("warm",["autumn","spring"], 2,2,"shadow","#906050",True,"클래식 웜 브라운"),
        "스노우화이트":p("cool",["winter","summer"], 1,4,"shadow","#E8E0E8",True,"쿨 하이라이트 섀도우"),
    },

    "롬앤 한올한올 아이섀도우": {
        "03 로즈핑크":   p("cool",["summer"],          2,3,"shadow","#D890A8",True,"맑은 쿨 로즈"),
        "06 코퍼브라운": p("warm",["autumn"],          2,2,"shadow","#A07058",True,"구리빛 브라운"),
        "10 테라핑크":   p("warm",["spring"],          2,3,"shadow","#D89080",True,"코랄핑크 섀도우"),
        "13 스모키그레이":p("cool",["winter"],         1,2,"shadow","#888098",True,"쿨 스모키 그레이"),
    },

    # 바닐라코 무드 온 아이 섀도우 팔레트 (2026.03 올영픽 — NEW)
    "바닐라코 무드 온 아이 섀도우 팔레트": {
        "01 웜선셋":    p("warm",["autumn","spring"], 2,2,"shadow","#C09070",True,"웜 선셋 9색 팔레트",2026,True),
        "02 쿨로즈누드":p("cool",["summer","winter"], 2,3,"shadow","#C090A8",True,"쿨 로즈누드 9색 팔레트",2026,True),
        "03 브라운어스":p("warm",["autumn"],          2,2,"shadow","#A07858",True,"브라운 어스 웜 팔레트",2026,True),
        "04 쿨모브스모키":p("cool",["winter"],        2,1,"shadow","#787098",True,"쿨 모브 스모키 팔레트",2026,True),
    },

    # ═══ BASE ═══════════════════════════════════════════════

    "롬앤 그램 글로잉 사틴 파운데이션": {
        "13N 아이보리":    p("warm",["spring","autumn"], 1,3,"base","#E8C8A8",True,"웜 밝은 피부"),
        "21N 라이트베이지":p("warm",["autumn"],          1,3,"base","#DEC0A0",True,"웜 자연 피부"),
        "23C 쿨내추럴":    p("cool",["summer"],          1,3,"base","#D8C0B0",True,"쿨 밝은 피부"),
        "25C 쿨베이지":    p("cool",["winter"],          1,2,"base","#D0B8A8",True,"쿨 중간 피부"),
    },

    "에스쁘아 프로 태일러 파운데이션": {
        "1W 아이보리":p("warm",["spring","autumn"], 1,3,"base","#EAD0B0",True,"웜 피부, 자연 밀착"),
        "2N 내추럴":  p("warm",["autumn"],          1,3,"base","#DEC0A0",True,"웜 중간 피부"),
        "3C 쿨베이지":p("cool",["summer","winter"], 1,3,"base","#D0B8A8",True,"쿨 베이지"),
    },

    "클리오 킬 커버 파운웨어 쿠션": {
        "1W 워너비아이보리":p("warm",["spring","autumn"], 1,3,"base","#EED0A8",True,"웜 아이보리 쿠션"),
        "2N 내추럴베이지":  p("warm",["autumn"],          1,3,"base","#E0C0A0",True,"웜 내추럴 쿠션"),
        "3C 쿨샌드":        p("cool",["summer","winter"], 1,3,"base","#D8C0B0",True,"쿨 샌드 쿠션"),
    },
}

# ══════════════════════════════════════════════════════════════
# PC 8톤
# ══════════════════════════════════════════════════════════════
PC = {
    "봄 라이트 웜":   dict(tone="warm",season="spring",emoji="🌸",
        kw=["맑음","생기","복숭아","산뜻 코랄"],
        desc="피부가 밝고 투명감이 있어요. 밝고 산뜻한 코랄·피치 계열이 잘 어울려요.",
        best=["코랄","피치","살구","밝은 오렌지","라이트 브라운"],avoid=["쿨 로즈","버건디","딥 퍼플","그레이"],
        bg="linear-gradient(135deg,#FFF8C0,#FFE030)",bd="#A88000",tc="#1C1000"),
    "봄 비비드 웜":   dict(tone="warm",season="spring",emoji="🌺",
        kw=["선명함","활기","코랄레드","오렌지"],
        desc="맑고 선명한 컬러가 피부에 생기를 더해요. 비비드 코랄~레드가 특히 잘 어울려요.",
        best=["코랄레드","오렌지레드","밝은 핑크"],avoid=["뮤트 컬러","다크 브라운","그레이"],
        bg="linear-gradient(135deg,#FFF5B0,#FFD820)",bd="#988000",tc="#1C1000"),
    "가을 딥 웜":     dict(tone="warm",season="autumn",emoji="🍂",
        kw=["깊이","테라코타","어스톤","내추럴"],
        desc="황금빛이 도는 깊고 풍부한 웜톤이에요. 테라코타·브릭·카멜이 완벽하게 어울려요.",
        best=["테라코타","브릭레드","머스타드","카멜","올리브"],avoid=["형광","네온","아이시 컬러"],
        bg="linear-gradient(135deg,#FFF3A0,#FFCC00)",bd="#887000",tc="#1A1000"),
    "가을 뮤트 웜":   dict(tone="warm",season="autumn",emoji="🌾",
        kw=["차분함","뮤트","누드","내추럴"],
        desc="채도가 낮고 부드러운 웜톤이에요. 뮤트한 브라운~누드 계열이 자연스러워요.",
        best=["카멜누드","웜베이지","머스타드뮤트","로즈브라운"],avoid=["비비드","형광","쿨 핑크"],
        bg="linear-gradient(135deg,#FFF8C0,#FFE840)",bd="#A08800",tc="#1C1200"),
    "여름 라이트 쿨": dict(tone="cool",season="summer",emoji="🌊",
        kw=["부드러움","로맨틱","파스텔","파우더리"],
        desc="밝고 부드러운 쿨톤이에요. 파스텔 핑크·라벤더·뮤트 로즈가 우아하게 어울려요.",
        best=["파스텔핑크","라벤더","소프트 로즈"],avoid=["오렌지","옐로우","골드 쉬머"],
        bg="linear-gradient(135deg,#DDE8FF,#AABEFF)",bd="#3860C0",tc="#06082A"),
    "여름 뮤트 쿨":   dict(tone="cool",season="summer",emoji="🩵",
        kw=["차분함","뮤트","로즈브라운","그레이시"],
        desc="채도가 낮고 세련된 쿨톤이에요. 뮤트 로즈·그레이핑크 계열이 지적으로 어울려요.",
        best=["뮤트 로즈","그레이핑크","라이트 퍼플"],avoid=["오렌지","테라코타","골드"],
        bg="linear-gradient(135deg,#D5E4FF,#98B8FF)",bd="#2858C0",tc="#040820"),
    "겨울 딥 쿨":     dict(tone="cool",season="winter",emoji="❄️",
        kw=["선명함","대비","딥레드","플럼"],
        desc="선명하고 강한 쿨톤이에요. 딥레드·플럼·버건디가 드라마틱하게 어울려요.",
        best=["딥레드","플럼","버건디","쿨 핑크"],avoid=["오렌지","코랄","웜 브라운","베이지"],
        bg="linear-gradient(135deg,#C8D8FF,#88AAFF)",bd="#1848B8",tc="#02041C"),
    "겨울 비비드 쿨": dict(tone="cool",season="winter",emoji="💙",
        kw=["대담함","비비드","블루베이스","강렬함"],
        desc="강렬하고 비비드한 쿨톤이에요. 블루베이스 레드·선명한 핑크가 빛나요.",
        best=["블루베이스 레드","비비드 핑크","퓨어 블랙","퓨어 화이트"],avoid=["파스텔","피치","코랄","웜 브라운"],
        bg="linear-gradient(135deg,#C0D0FF,#7898FF)",bd="#1038A8",tc="#02041C"),
}

PAIRING = {
    ("spring","blush"):  [("롬앤 베러 댄 치크","코랄리프"),("에뛰드 러블리 쿠키 블러셔","1호 피치"),("NARS 블러쉬","오가즘"),("VDL 치크스테인 블러셔","01 코랄스테인")],
    ("spring","shadow"): [("클리오 프로 아이 팔레트","06 어텀테라"),("에뛰드 플레이 컬러 아이즈","베어누드"),("바닐라코 무드 온 아이 섀도우 팔레트","01 웜선셋"),("롬앤 한올한올 아이섀도우","10 테라핑크")],
    ("autumn","blush"):  [("NARS 블러쉬","딥트로트"),("클리오 킬 커버 더 뉴 치크","03 캐시미어"),("페리페라 블러블러 페이스 블러셔","01 코코피치"),("헤라 센슈얼 파우더 블러셔","03 딥테라")],
    ("autumn","shadow"): [("클리오 프로 아이 팔레트","04 브라운브릭"),("어반디케이 네이키드 팔레트","NAKED RELOADED"),("맥 아이섀도우 단품","코퍼스파크"),("데이지크 아이섀도우 팔레트","01 웜어스")],
    ("summer","blush"):  [("롬앤 베러 댄 치크","스트로베리밀크"),("에뛰드 러블리 쿠키 블러셔","2호 핑크"),("NARS 블러쉬","부에노스아이레스"),("VDL 치크스테인 블러셔","02 로즈스테인")],
    ("summer","shadow"): [("클리오 프로 아이 팔레트","03 앤틱핑크"),("에뛰드 플레이 컬러 아이즈","핑크쉐이드"),("어반디케이 네이키드 팔레트","NAKED3"),("데이지크 아이섀도우 팔레트","02 쿨로즈")],
    ("winter","blush"):  [("NARS 블러쉬","카마수트라"),("롬앤 베러 댄 치크","쿨로즈"),("페리페라 블러블러 페이스 블러셔","03 미드나잇플럼"),("VDL 치크스테인 블러셔","03 베리스테인")],
    ("winter","shadow"): [("클리오 프로 아이 팔레트","09 스모키쿨"),("어반디케이 네이키드 팔레트","NAKED3"),("바닐라코 무드 온 아이 섀도우 팔레트","04 쿨모브스모키"),("데이지크 아이섀도우 팔레트","04 쿨스모키")],
}

CAT_KR = {"lip":"립","blush":"블러셔","shadow":"섀도우","base":"베이스"}
SEA_KR = {"spring":"봄 웜","autumn":"가을 웜","summer":"여름 쿨","winter":"겨울 쿨"}


def dot(hx, sz=16):
    return f'<span class="dot" style="width:{sz}px;height:{sz}px;background:{hx};"></span>'
def tg(text, cls):
    return f'<span class="tag {cls}">{text}</span>'
def tone_tag(t):
    return tg("🌞 웜톤" if t=="warm" else "❄️ 쿨톤", f"t-{t}")
def sea_tag(s):
    return tg(SEA_KR.get(s,""), f"t-{s}")
def new_badge():
    return tg("✦ 2026.03 NEW","t-new")

def pcard(pname, shade, d, fit=""):
    nb  = (" " + new_badge()) if d.get("new") else ""
    fp  = f'<span class="pcard-fit">{fit}</span>' if fit else ""
    return f"""
<div class="pcard">
    <div style="padding-top:2px">{dot(d['hex'],20)}</div>
    <div class="pcard-right">
        <div class="pcard-top">
            <span class="pcard-name">{pname}{nb}</span>{fp}
        </div>
        <div class="pcard-shade">{shade} · {CAT_KR.get(d['category'],'')}</div>
        <div class="pcard-note">{d['note']}</div>
    </div>
</div>"""


def run_analysis(gl, bl, tl):
    ts=cs=vs=wt=0.0
    def acc(items, w):
        nonlocal ts,cs,vs,wt
        for it in items:
            if not it: continue
            pn,sh=it; d=DB[pn][sh]
            ts+=(1 if d["tone"]=="warm" else -1)*w
            cs+=d["chroma"]*w; vs+=d["value"]*w; wt+=abs(w)
    acc(gl,1.0); acc(tl,2.0); acc(bl,-1.5)
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
            if year_filter:
                if year_filter=="new" and not d.get("new"): continue
                elif year_filter==2024 and d.get("year")!=2024: continue
                elif year_filter==2025 and d.get("year")!=2025: continue
                elif year_filter=="classic" and d.get("year") is not None: continue
            if d["tone"]==tone and season in d["season"]: p.append((pn,sh,d))
            elif d["tone"]==tone: g.append((pn,sh,d))
    return (p+g)[:limit]


def product_picker(prefix, include_disc=False):
    cat_labels = ["전체","립","블러셔","섀도우","베이스"]
    cat_map    = {"전체":None,"립":"lip","블러셔":"blush","섀도우":"shadow","베이스":"base"}

    ca, cb = st.columns([1, 2])
    with ca:
        lbl = st.selectbox("c", cat_labels, key=f"{prefix}_cat", label_visibility="collapsed")
    cat = cat_map[lbl]

    pnames = sorted({
        pn for pn, shades in DB.items()
        for sh, d in shades.items()
        if (cat is None or d["category"]==cat) and (include_disc or d["avail"])
    })

    with cb:
        pname = st.selectbox("p", pnames, index=None, placeholder="제품명 선택",
                              key=f"{prefix}_pname", label_visibility="collapsed")
    if not pname:
        return None

    shade_opts = [sh for sh,d in DB[pname].items() if include_disc or d["avail"]]
    shade = st.selectbox("s", shade_opts, index=None, placeholder="호수(컬러) 선택",
                          key=f"{prefix}_shade", label_visibility="collapsed")
    if not shade:
        return None

    d = DB[pname][shade]
    disc = " " + tg("단종","t-disc") if not d["avail"] else ""
    nb   = " " + new_badge() if d.get("new") else ""
    st.markdown(
        f'<div class="mini-info">'
        f'<div class="mini-dot" style="background:{d["hex"]};"></div>'
        f'<div style="display:flex;align-items:center;flex-wrap:wrap;gap:0.28rem;">'
        f'{tone_tag(d["tone"])} {"".join(sea_tag(s) for s in d["season"])}'
        f'{disc}{nb}'
        f'<span style="color:var(--muted);font-size:0.73rem">{d["note"]}</span>'
        f'</div></div>',
        unsafe_allow_html=True,
    )
    return (pname, shade)


# ══════════════════════════════════════════════════════════════
# TAB 1
# ══════════════════════════════════════════════════════════════
def tab_analysis():
    st.markdown('<p class="sec-head">퍼스널 컬러 분석</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sec-sub">사용해봤던 제품들을 입력하면 세부 8톤 퍼스널 컬러를 분석해드려요. '
        '<b>잘 맞았던 제품 1개</b>만 있어도 분석 가능해요.</p>',
        unsafe_allow_html=True,
    )
    with st.expander("💡 입력 팁"):
        st.markdown("""
| 구분 | 기준 | 가중치 |
|---|---|---|
| 👍 잘 맞았던 | 피부가 환해지거나 칭찬을 많이 받은 제품 | × 1 |
| 👎 안 맞았던 | 칙칙해지거나 뜬다는 느낌을 받은 제품 | × −1.5 |
| 🔥 반응 좋았던 | SNS·일상에서 특히 호평받은 제품 | × 2 |

단종 제품도 입력 기록용으로 선택 가능해요.
        """)

    c1,c2,c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown('<div class="col-label">👍 잘 맞았던 제품 · 필수 1–3개</div>', unsafe_allow_html=True)
        g1=product_picker("g1",True); st.divider()
        g2=product_picker("g2",True); st.divider()
        g3=product_picker("g3",True)
    with c2:
        st.markdown('<div class="col-label">👎 안 맞았던 제품 · 선택 1–3개</div>', unsafe_allow_html=True)
        b1=product_picker("b1",True); st.divider()
        b2=product_picker("b2",True); st.divider()
        b3=product_picker("b3",True)
    with c3:
        st.markdown('<div class="col-label">🔥 반응 좋았던 제품 · 선택 1–3개</div>', unsafe_allow_html=True)
        t1=product_picker("t1",True); st.divider()
        t2=product_picker("t2",True); st.divider()
        t3=product_picker("t3",True)

    st.markdown("<br>", unsafe_allow_html=True)
    _,bc,_ = st.columns([2,2,2])
    with bc:
        run = st.button("🌼 퍼스널 컬러 분석하기", use_container_width=True)

    if run:
        goods=[x for x in [g1,g2,g3] if x]
        bads =[x for x in [b1,b2,b3] if x]
        bests=[x for x in [t1,t2,t3] if x]
        if not goods: st.warning("잘 맞았던 제품을 최소 1개 선택해주세요 😊"); return
        st.session_state["result"] = run_analysis(goods, bads, bests)

    if st.session_state.get("result"):
        _render_result(st.session_state["result"])


def _render_result(res):
    pc=res["pc"]; info=PC[pc]; tone=res["tone"]
    st.divider()
    box="rbox-warm" if tone=="warm" else "rbox-cool"
    kw="".join(f'<span class="tag t-{tone}">{k}</span>' for k in info["kw"])
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

    # 라디오 버튼 — 배경색 위에서도 잘 보이도록
    st.markdown("""
<style>
/* 결과 섹션 라디오 강제 오버라이드 */
[data-testid="stRadio"] label,
[data-testid="stRadio"] > div > label {
    color: #1C1400 !important;
    background: rgba(255,255,255,0.85) !important;
    border: 1.5px solid #8B6914 !important;
    border-radius: 8px !important;
    padding: 0.28rem 0.75rem !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

    cc,cy=st.columns([3,2])
    with cc:
        cat_ch=st.radio("",["전체","립","블러셔","섀도우"],horizontal=True,
                         key="res_cat",label_visibility="collapsed")
    with cy:
        yr_ch=st.selectbox("",["전체 연도","2026.03 NEW","2025","2024","클래식"],
                            key="res_yr",label_visibility="collapsed")

    cmap={"전체":None,"립":"lip","블러셔":"blush","섀도우":"shadow"}
    ymap={"전체 연도":None,"2026.03 NEW":"new","2025":2025,"2024":2024,"클래식":"classic"}
    recs=get_recs(res["tone"],res["season"],cat=cmap[cat_ch],limit=8,year_filter=ymap[yr_ch])
    if not recs: st.info("해당 조건의 추천 제품이 없어요."); return
    cols=st.columns(2)
    for i,(pn,sh,d) in enumerate(recs):
        fit="✨ 완벽 매칭" if res["season"] in d["season"] else "👍 어울려요"
        with cols[i%2]: st.markdown(pcard(pn,sh,d,fit), unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TAB 2
# ══════════════════════════════════════════════════════════════
def tab_pairing():
    st.markdown('<p class="sec-head">연계 추천 서비스</p>', unsafe_allow_html=True)
    st.markdown('<p class="sec-sub">퍼스널 컬러를 선택하면 립·블러셔·섀도우를 함께 큐레이션해드려요.</p>', unsafe_allow_html=True)

    pc_list=list(PC.keys())
    auto=st.session_state.get("result",{}).get("pc",pc_list[0])
    idx=pc_list.index(auto) if auto in pc_list else 0
    pc_sel=st.selectbox("퍼스널 컬러",pc_list,index=idx,key="pair_pc")
    if st.session_state.get("result"):
        if st.button("🎯 분석 결과 자동 적용"):
            st.session_state["pair_pc"]=st.session_state["result"]["pc"]; st.rerun()

    info=PC[pc_sel]; tone=info["tone"]; season=info["season"]
    ib="ib-warm" if tone=="warm" else "ib-cool"
    tc=info["tc"]
    st.markdown(f"""
<div class="info-band {ib}">
    <b style="font-size:0.95rem;color:{tc}">{info['emoji']} {pc_sel}</b>
    &nbsp; {tone_tag(tone)} {sea_tag(season)}<br>
    <span style="font-size:0.81rem;color:{tc};opacity:0.88">{info['desc']}</span>
</div>""", unsafe_allow_html=True)

    st.markdown("### 💄 추천 립")
    lr=get_recs(tone,season,cat="lip",limit=6)
    lc=st.columns(3)
    for i,(pn,sh,d) in enumerate(lr):
        nb=(" "+new_badge()) if d.get("new") else ""
        with lc[i%3]:
            st.markdown(f"""
<div class="pcard" style="flex-direction:column;gap:0.25rem;">
    <div style="display:flex;align-items:center;gap:0.55rem">
        {dot(d['hex'],22)}
        <span style="font-weight:600;font-size:0.85rem;color:var(--text)">{pn}{nb}</span>
    </div>
    <div style="padding-left:30px">
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
        with bc[i%2]: st.markdown(pcard(pn,sh,d), unsafe_allow_html=True)

    st.divider()
    st.markdown("### ✨ 어울리는 섀도우")
    sk=(season,"shadow")
    si=[(pn,sh,DB[pn][sh]) for pn,sh in PAIRING.get(sk,[]) if pn in DB and sh in DB[pn] and DB[pn][sh]["avail"]] \
       or [(pn,sh,d) for pn,sh,d in get_recs(tone,season,cat="shadow",limit=4)]
    sc=st.columns(2)
    for i,(pn,sh,d) in enumerate(si[:4]):
        with sc[i%2]: st.markdown(pcard(pn,sh,d), unsafe_allow_html=True)

    st.divider()
    tips={"spring":"봄 웜톤은 **밝고 산뜻한 코랄·피치 조합**이 최고예요. 골드 액세서리와도 찰떡이에요.",
          "autumn":"가을 웜톤은 **어스톤·테라코타 팔레트**로 풍부한 매력을 살려보세요.",
          "summer":"여름 쿨톤은 **뮤트 핑크·라벤더 조합**이 세련돼요. 실버 액세서리가 피부를 빛나게 해줘요.",
          "winter":"겨울 쿨톤은 **강렬한 컨트라스트**가 매력이에요. 선명한 레드 립 하나로 완성!"}
    st.info(tips.get(season,""))


# ══════════════════════════════════════════════════════════════
# TAB 3
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

    def filtered(cat, lmt=3):
        r=[]
        for pn,shades in DB.items():
            for sh,d in shades.items():
                if not d["avail"] or d["category"]!=cat: continue
                if not (cmin<=d["chroma"]<=cmax): continue
                if d["tone"]==tone and season in d["season"]: r.append((pn,sh,d))
                elif d["tone"]==tone: r.append((pn,sh,d))
        if not r: r=[(pn,sh,d) for pn,sh,d in get_recs(tone,season,cat=cat,limit=lmt)]
        return r[:lmt]

    ib="ib-warm" if tone=="warm" else "ib-cool"
    tc=info["tc"]
    st.markdown(f"""
<div class="info-band {ib}">
    <b style="font-size:0.95rem;color:{tc}">{info['emoji']} {pc_sel} · {mood} · {intensity}</b><br>
    <span style="font-size:0.8rem;color:{tc};opacity:0.88">아래 조합으로 오늘 메이크업을 완성해보세요 ✨</span>
</div>""", unsafe_allow_html=True)

    m1,m2,m3=st.columns(3)
    for col,title,cat in [(m1,"💄 립","lip"),(m2,"🌸 블러셔","blush"),(m3,"✨ 섀도우","shadow")]:
        with col:
            st.markdown(f"**{title}**")
            for pn,sh,d in filtered(cat):
                nb=(" "+new_badge()) if d.get("new") else ""
                st.markdown(f"""
<div class="pcard" style="flex-direction:column;gap:0.22rem;margin-bottom:0.4rem;">
    <div style="display:flex;align-items:center;gap:0.5rem">
        {dot(d['hex'],18)}
        <span style="font-weight:600;font-size:0.82rem;color:var(--text)">{pn}{nb}</span>
    </div>
    <div style="padding-left:24px">
        <div class="pcard-shade">{sh}</div>
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
# TAB 4
# ══════════════════════════════════════════════════════════════
def tab_browse():
    st.markdown('<p class="sec-head">제품 탐색</p>', unsafe_allow_html=True)
    st.markdown('<p class="sec-sub">카테고리·톤·계절·출시연도로 필터링해서 전체 제품을 살펴보세요.</p>', unsafe_allow_html=True)

    f1,f2,f3,f4=st.columns(4)
    with f1: fcat =st.selectbox("카테고리",["전체","립","블러셔","섀도우","베이스"],key="br_cat")
    with f2: ftone=st.selectbox("톤",["전체","웜톤","쿨톤"],key="br_tone")
    with f3: fsea =st.selectbox("계절",["전체","봄 웜","가을 웜","여름 쿨","겨울 쿨"],key="br_sea")
    with f4: fyr  =st.selectbox("출시",["전체","✦ 2026.03 NEW","2025","2024","클래식"],key="br_yr")
    show_disc=st.checkbox("단종 제품도 보기",value=False)

    cmap={"전체":None,"립":"lip","블러셔":"blush","섀도우":"shadow","베이스":"base"}
    tmap={"전체":None,"웜톤":"warm","쿨톤":"cool"}
    smap={"전체":None,"봄 웜":"spring","가을 웜":"autumn","여름 쿨":"summer","겨울 쿨":"winter"}
    fc,ft,fs=cmap[fcat],tmap[ftone],smap[fsea]
    yf={"전체":None,"✦ 2026.03 NEW":"new","2025":2025,"2024":2024,"클래식":"classic"}[fyr]

    rows=[]
    for pn,shades in DB.items():
        for sh,d in shades.items():
            if not show_disc and not d["avail"]: continue
            if fc and d["category"]!=fc: continue
            if ft and d["tone"]!=ft: continue
            if fs and fs not in d["season"]: continue
            if yf=="new" and not d.get("new"): continue
            elif yf==2025 and d.get("year")!=2025: continue
            elif yf==2024 and d.get("year")!=2024: continue
            elif yf=="classic" and d.get("year") is not None: continue
            rows.append((pn,sh,d))

    st.markdown(f"<small style='color:var(--muted);font-weight:600'>{len(rows)}개 제품</small>",
                unsafe_allow_html=True)
    if not rows: st.info("조건에 맞는 제품이 없어요."); return

    for i in range(0,len(rows),3):
        cols=st.columns(3)
        for j,(pn,sh,d) in enumerate(rows[i:i+3]):
            with cols[j]:
                disc=" "+tg("단종","t-disc") if not d["avail"] else ""
                nb=" "+new_badge() if d.get("new") else ""
                st.markdown(f"""
<div class="pcard" style="flex-direction:column;gap:0.32rem;padding:0.85rem;">
    <div style="display:flex;align-items:center;gap:0.6rem">
        {dot(d['hex'],22)}
        <div>
            <div class="pcard-name">{pn}{disc}{nb}</div>
            <div class="pcard-shade">{sh}</div>
        </div>
    </div>
    <div class="pcard-note" style="padding-left:30px">{d['note']}</div>
    <div style="padding-left:30px">{tone_tag(d['tone'])} {''.join(sea_tag(s) for s in d['season'])} {tg(CAT_KR.get(d['category'],''),'t-cat')}</div>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TAB 5
# ══════════════════════════════════════════════════════════════
def tab_guide():
    st.markdown('<p class="sec-head">퍼스널 컬러 가이드</p>', unsafe_allow_html=True)
    st.markdown('<p class="sec-sub">세부 8톤의 특징과 뷰티 스타일링 팁을 한눈에 확인하세요.</p>', unsafe_allow_html=True)
    for pc_name,info in PC.items():
        tone=info["tone"]
        with st.expander(f"{info['emoji']}  {pc_name}"):
            a,b=st.columns([3,2])
            with a:
                kw="".join(f'<span class="tag t-{tone}">{k}</span>' for k in info["kw"])
                tc=info["tc"]
                st.markdown(f"""
<div style="background:{info['bg']};border:1.5px solid {info['bd']};border-radius:12px;padding:1.15rem 1.4rem;">
    <b style="font-size:0.98rem;color:{tc}">{info['emoji']} {pc_name}</b><br>
    <div style="font-size:0.84rem;color:{tc};opacity:0.88;margin:0.45rem 0;line-height:1.7">{info['desc']}</div>
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
<div style="text-align:center;padding:0.4rem 0.2rem;">
    <div style="width:30px;height:30px;border-radius:50%;background:{d['hex']};
                margin:0 auto 0.3rem;border:2px solid rgba(0,0,0,0.1);"></div>
    <div style="font-size:0.72rem;font-weight:600;color:var(--text);line-height:1.35">{pn}</div>
    <div style="font-size:0.67rem;color:var(--muted)">{sh}</div>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════
def main():
    st.markdown("""
<div class="hero-title">TONE<em>ME</em></div>
<div class="hero-bar"></div>
<div class="hero-sub">퍼스널 컬러 기반 뷰티 큐레이터 · 세부 8톤 분석 · 국내 구매 가능 제품</div>
""", unsafe_allow_html=True)

    t1,t2,t3,t4,t5 = st.tabs([
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

    st.markdown(
        '<div class="footer">TONEME · 단종 제품은 추천 제외 · 국내 구매 가능 제품만 수록</div>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
