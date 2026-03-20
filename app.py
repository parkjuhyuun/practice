import streamlit as st

st.set_page_config(
    page_title="TONEME · 퍼스널 컬러 뷰티",
    page_icon="🌼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,500;1,400&family=Noto+Sans+KR:wght@300;400;500&display=swap');

:root {
    --bg:       #FEFAE8;
    --surface:  #FFFDF0;
    --border:   #EDE89A;
    --accent:   #D4A800;
    --accent2:  #F5CC00;
    --text:     #2A2400;
    --textsub:  #7A7230;
    --tagwarm:  #FFF3C0;
    --tagcool:  #E8F4FF;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: var(--bg) !important;
    font-family: 'Noto Sans KR', sans-serif;
}
[data-testid="stSidebar"] { display: none; }
.block-container { padding: 2.5rem 3rem 6rem !important; max-width: 1100px !important; }

/* HERO */
.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.2rem; font-weight: 300; letter-spacing: 0.08em;
    color: var(--text); line-height: 1; text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.hero-title em { font-style: italic; color: var(--accent); }
.hero-bar { width: 48px; height: 2.5px; background: var(--accent2); margin: 0.6rem 0 0.7rem; border-radius: 2px; }
.hero-sub { font-size: 0.78rem; color: var(--textsub); letter-spacing: 0.06em; margin-bottom: 2rem; }

/* TABS */
.stTabs [data-baseweb="tab-list"] {
    gap: 0; background: transparent; border-bottom: 2px solid var(--border);
}
.stTabs [data-baseweb="tab"] {
    font-size: 0.86rem; font-weight: 400; color: var(--textsub);
    padding: 0.6rem 1.4rem; border-radius: 0; background: transparent; border: none;
}
.stTabs [aria-selected="true"] {
    color: var(--text) !important; background: transparent !important;
    border-bottom: 2.5px solid var(--accent) !important; font-weight: 600 !important;
}

/* SECTION */
.sec-head { font-size: 1.1rem; font-weight: 600; color: var(--text); margin-bottom: 0.2rem; }
.sec-sub  { font-size: 0.79rem; color: var(--textsub); line-height: 1.65; margin-bottom: 1.2rem; }

/* COL LABEL */
.col-label {
    font-size: 0.75rem; font-weight: 600; letter-spacing: 0.05em;
    color: var(--textsub); padding-bottom: 0.6rem;
    border-bottom: 1px solid var(--border); margin-bottom: 0.8rem;
}

/* SELECTED PRODUCT BADGE — 핵심 개선: 선택 상품 즉시 표시 */
.selected-badge {
    display: flex; align-items: center; gap: 0.6rem;
    background: var(--surface); border: 1.5px solid var(--accent2);
    border-radius: 10px; padding: 0.6rem 0.9rem; margin-top: 0.4rem;
    font-size: 0.83rem; font-weight: 500; color: var(--text);
}
.selected-badge .badge-name  { font-weight: 600; font-size: 0.85rem; }
.selected-badge .badge-shade { font-size: 0.76rem; color: var(--textsub); margin-top: 0.08rem; }
.selected-badge .badge-note  { font-size: 0.7rem; color: #A09830; margin-top: 0.05rem; }

/* TAGS */
.tag { display:inline-block; padding:0.15rem 0.6rem; border-radius:100px; font-size:0.68rem; font-weight:500; margin:0.08rem; }
.t-warm   { background:#FFF3C0; color:#7A5A00; }
.t-cool   { background:#E8F4FF; color:#304080; }
.t-spring { background:#FFEECC; color:#9A5800; }
.t-summer { background:#EAE8FF; color:#4040A0; }
.t-autumn { background:#FFE8C8; color:#8A3800; }
.t-winter { background:#E0E8FF; color:#2828A0; }
.t-cat    { background:#F5F0D0; color:#6A5E20; }
.t-disc   { background:#F5F5F0; color:#AAA; }
.t-new    { background:#FFF0A0; color:#8A6000; }

/* SWATCH DOT */
.dot { display:inline-block; border-radius:50%; border:1.5px solid rgba(0,0,0,0.1); vertical-align:middle; flex-shrink:0; }

/* PRODUCT CARD */
.pcard {
    display:flex; align-items:center; gap:0.7rem;
    background:var(--surface); border:1px solid var(--border);
    border-radius:11px; padding:0.75rem 0.9rem; margin-bottom:0.45rem;
}
.pcard-info { flex:1; min-width:0; }
.pcard-name  { font-weight:500; font-size:0.84rem; line-height:1.3; }
.pcard-shade { font-size:0.76rem; color:var(--textsub); }
.pcard-note  { font-size:0.71rem; color:#B0A860; margin-top:0.1rem; }
.pcard-fit   { font-size:0.69rem; color:var(--accent); white-space:nowrap; }

/* RESULT BOX */
.rbox-warm {
    background: linear-gradient(135deg,#FFFBE0,#FFF3A0);
    border:1.5px solid #E8D040; border-radius:18px; padding:1.8rem 2rem; margin-bottom:1.2rem;
}
.rbox-cool {
    background: linear-gradient(135deg,#F0F4FF,#E0EAFF);
    border:1.5px solid #B0C0E8; border-radius:18px; padding:1.8rem 2rem; margin-bottom:1.2rem;
}
.rbox-title { font-family:'Cormorant Garamond',serif; font-size:2rem; font-weight:300; color:var(--text); margin-bottom:0.4rem; }
.rbox-desc  { font-size:0.86rem; color:#555; line-height:1.75; }

/* INFO BAND */
.info-band { border-radius:11px; padding:1rem 1.3rem; margin-bottom:1rem; }
.ib-warm   { background:linear-gradient(135deg,#FFFBE0,#FFF3B8); border:1px solid #E0C830; }
.ib-cool   { background:linear-gradient(135deg,#F0F4FF,#E0E8FF); border:1px solid #A8B8E0; }

/* SKIN TONE CHIP — 새 기능: 피부톤 체크 */
.skin-chip {
    display:inline-block; padding:0.4rem 1rem; border-radius:100px;
    font-size:0.78rem; font-weight:500; cursor:pointer; margin:0.2rem;
    border:1.5px solid var(--border); background:var(--surface); color:var(--text);
}

/* BUTTON */
.stButton > button {
    background:var(--accent) !important; color:#fff !important;
    border:none !important; border-radius:9px !important;
    padding:0.6rem 1.8rem !important; font-size:0.86rem !important;
    font-weight:500 !important; width:100% !important; transition:opacity 0.15s !important;
}
.stButton > button:hover { opacity:0.8 !important; }

/* SELECTBOX */
.stSelectbox label { font-size:0.78rem !important; color:var(--textsub) !important; }
.stSelectbox > div > div {
    border-radius:9px !important; border-color:var(--border) !important;
    font-size:0.85rem !important; background:var(--surface) !important;
}

/* SLIDER */
.stSlider > div > div > div { background: var(--accent2) !important; }

/* EXPANDER */
details summary { font-size:0.8rem !important; color:var(--textsub) !important; }
hr { border-color:var(--border) !important; margin:1.4rem 0 !important; }
.stSuccess, .stWarning, .stInfo { border-radius:10px !important; font-size:0.84rem !important; }
.footer { text-align:center; font-size:0.72rem; color:#A09830; padding:1.5rem 0 2rem; letter-spacing:0.06em; }

/* 즐겨찾기 버튼 */
.fav-btn { font-size:1.1rem; cursor:pointer; padding:0.2rem; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 제품 DB  (2024년 이후 출시작 포함, avail=True만 추천에 사용)
# tone     : "warm" | "cool"
# season   : list["spring"|"autumn"|"summer"|"winter"]
# chroma   : 1~4   value : 1~4
# category : "lip"|"blush"|"shadow"|"base"
# hex      : 대표컬러   avail : True=판매중 False=단종
# note     : 한줄설명   new : True=2024년 이후 출시
# ══════════════════════════════════════════════════════════════
DB = {
    # ── LIP ─────────────────────────────────────────────────
    "롬앤 쥬시 래스팅 틴트": {
        "06 피그피그":           dict(tone="cool",season=["summer","winter"],  chroma=2,value=2,category="lip",hex="#C47090",avail=True, note="물광 마감, 뮤트 로즈",                new=False),
        "07 쥬쥬브":             dict(tone="warm",season=["spring","autumn"],  chroma=3,value=2,category="lip",hex="#C45858",avail=True, note="생기있는 레드베리",                  new=False),
        "08 애플브라운":         dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="lip",hex="#A85040",avail=True, note="깊은 테라코타 브라운",               new=False),
        "17 딸기우유":           dict(tone="cool",season=["spring","summer"],  chroma=2,value=3,category="lip",hex="#D88090",avail=True, note="투명감 딸기밀크 핑크",               new=False),
        "20 레드벨벳":           dict(tone="cool",season=["winter"],           chroma=4,value=2,category="lip",hex="#B83040",avail=True, note="딥레드, 강렬한 존재감",              new=False),
        "23 피칸브라운":         dict(tone="warm",season=["autumn"],           chroma=1,value=2,category="lip",hex="#885040",avail=True, note="일상 내추럴 누드브라운",             new=False),
        "28 핑크핑크":           dict(tone="cool",season=["summer"],           chroma=3,value=3,category="lip",hex="#E070A8",avail=True, note="발랄한 쿨핑크 — 2024 신규",         new=True),
        "29 브릭베이지":         dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="lip",hex="#A06850",avail=True, note="웜 브릭베이지 — 2024 신규",         new=True),
    },
    "에뛰드 픽싱 틴트": {
        "03 멜로우피치":         dict(tone="warm",season=["spring"],           chroma=2,value=3,category="lip",hex="#E09068",avail=True, note="복숭아빛 코랄, 봄 생기",            new=False),
        "05 미드나잇모브":       dict(tone="cool",season=["winter","summer"],  chroma=2,value=2,category="lip",hex="#987090",avail=True, note="보랏빛 뮤트 핑크",                  new=False),
        "06 소프트월넛":         dict(tone="warm",season=["autumn"],           chroma=1,value=2,category="lip",hex="#906858",avail=True, note="웜 누드, 피부 밀착",                new=False),
        "08 베리핑크":           dict(tone="cool",season=["summer"],           chroma=3,value=3,category="lip",hex="#C870A0",avail=True, note="선명 핑크, 여름 포인트",            new=False),
        "11 진저브라운":         dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="lip",hex="#8A5040",avail=False,note="깊은 진저브라운 ★단종",             new=False),
        "12 스트로베리소다":     dict(tone="cool",season=["spring","summer"],  chroma=3,value=3,category="lip",hex="#E06898",avail=True, note="청량 딸기소다 — 2024 출시",         new=True),
    },
    "페리페라 잉크 무드 글로이 틴트": {
        "01 쿨오프코랄":         dict(tone="warm",season=["spring"],           chroma=3,value=3,category="lip",hex="#E07860",avail=True, note="밝은 코랄오렌지",                   new=False),
        "03 맘찍로즈":           dict(tone="cool",season=["summer"],           chroma=2,value=3,category="lip",hex="#D088A0",avail=True, note="뮤트 로즈핑크",                     new=False),
        "06 초코브릭":           dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="lip",hex="#8A4838",avail=True, note="초콜릿 브릭 레드",                  new=False),
        "09 코랄프레쉬":         dict(tone="warm",season=["spring"],           chroma=3,value=3,category="lip",hex="#E06848",avail=True, note="생생한 코랄",                       new=False),
        "14 누드로즈우드":       dict(tone="cool",season=["summer","winter"],  chroma=1,value=2,category="lip",hex="#A87888",avail=True, note="쿨 누드로즈우드 — 2024 신규",       new=True),
        "15 라벤더쇼크":         dict(tone="cool",season=["summer"],           chroma=2,value=3,category="lip",hex="#B890C8",avail=True, note="라벤더빛 쿨핑크 — 2024 신규",       new=True),
    },
    "클리오 쉬폰 블러 틴트": {
        "03 피치퍼즐":           dict(tone="warm",season=["spring","autumn"],  chroma=2,value=3,category="lip",hex="#D89080",avail=True, note="스모키 피치",                       new=False),
        "05 코랄":               dict(tone="warm",season=["spring"],           chroma=2,value=3,category="lip",hex="#DC7060",avail=True, note="클래식 코랄",                       new=False),
        "07 로즈":               dict(tone="cool",season=["summer","winter"],  chroma=3,value=3,category="lip",hex="#C86890",avail=True, note="청량한 로즈",                       new=False),
        "09 레드브릭":           dict(tone="warm",season=["autumn"],           chroma=3,value=2,category="lip",hex="#A03830",avail=True, note="벽돌빛 레드",                       new=False),
        "13 쿨핑크클라우드":     dict(tone="cool",season=["summer"],           chroma=2,value=3,category="lip",hex="#D880B0",avail=True, note="구름 같은 쿨핑크 — 2024 출시",      new=True),
        "14 웜테라누드":         dict(tone="warm",season=["autumn"],           chroma=1,value=2,category="lip",hex="#9A6050",avail=True, note="웜 테라코타 누드 — 2024 출시",      new=True),
    },
    "3CE 벨벳 립 틴트": {
        "파우더핑크":            dict(tone="cool",season=["summer"],           chroma=1,value=3,category="lip",hex="#D8A8B8",avail=True, note="파우더리 쿨핑크 누드",              new=False),
        "두메":                  dict(tone="cool",season=["winter"],           chroma=2,value=2,category="lip",hex="#B06888",avail=True, note="뮤트 로즈브라운, 겨울 정석",        new=False),
        "러스티로즈":            dict(tone="cool",season=["summer","winter"],  chroma=2,value=2,category="lip",hex="#A87080",avail=True, note="빈티지 로즈",                       new=False),
        "퍼스트데이트":          dict(tone="warm",season=["spring"],           chroma=2,value=3,category="lip",hex="#E09898",avail=True, note="밝은 베이비핑크",                   new=False),
        "누드플럼":              dict(tone="cool",season=["winter"],           chroma=2,value=1,category="lip",hex="#7A5068",avail=True, note="딥 누드 플럼",                      new=False),
        "코코아무드":            dict(tone="warm",season=["autumn"],           chroma=1,value=2,category="lip",hex="#8A5848",avail=True, note="코코아 웜 브라운 — 2024 신규",      new=True),
        "쿨라일락":              dict(tone="cool",season=["summer"],           chroma=2,value=3,category="lip",hex="#C0A0D0",avail=True, note="연한 쿨 라일락 — 2024 신규",        new=True),
    },
    "맥 리프스틱": {
        "Whirl":                 dict(tone="warm",season=["autumn"],           chroma=1,value=2,category="lip",hex="#906060",avail=True, note="국민 누드브라운, 가을 완벽템",      new=False),
        "Ruby Woo":              dict(tone="cool",season=["winter"],           chroma=4,value=2,category="lip",hex="#C02030",avail=True, note="클래식 블루베이스 레드",            new=False),
        "Velvet Teddy":          dict(tone="warm",season=["autumn"],           chroma=1,value=2,category="lip",hex="#8A5848",avail=True, note="따뜻한 뮤트 누드",                  new=False),
        "Brave":                 dict(tone="warm",season=["spring","autumn"],  chroma=1,value=3,category="lip",hex="#C09080",avail=True, note="피치 누드",                         new=False),
        "Flat Out Fabulous":     dict(tone="cool",season=["winter"],           chroma=3,value=1,category="lip",hex="#803060",avail=True, note="다크 플럼",                         new=False),
    },
    "롬앤 한올한올 뉴립스틱": {
        "04 베어릭":             dict(tone="warm",season=["autumn"],           chroma=1,value=2,category="lip",hex="#9A6858",avail=True, note="워터리 피부색 누드",                new=False),
        "07 코럴하이":           dict(tone="warm",season=["spring"],           chroma=3,value=3,category="lip",hex="#E07060",avail=True, note="코랄 레드",                         new=False),
        "11 스트로베리파우더":   dict(tone="cool",season=["summer"],           chroma=2,value=3,category="lip",hex="#D08898",avail=True, note="파우더리 딸기 핑크",                new=False),
        "14 라즈베리무드":       dict(tone="cool",season=["winter"],           chroma=3,value=2,category="lip",hex="#B04870",avail=True, note="선명한 라즈베리",                   new=False),
        "17 코코넛누드":         dict(tone="warm",season=["spring","autumn"],  chroma=1,value=3,category="lip",hex="#C8A080",avail=True, note="밀크누드, 일상 쓰기 좋은",          new=False),
    },
    # 2024년 신규 브랜드/라인
    "투쿨포스쿨 아트클래스 바이 로댕 틴트": {
        "01 로제":               dict(tone="cool",season=["summer"],           chroma=2,value=3,category="lip",hex="#D890A8",avail=True, note="그라데이션 쿨로즈 — 2024 출시",     new=True),
        "02 베이지테라":         dict(tone="warm",season=["autumn"],           chroma=1,value=2,category="lip",hex="#A07860",avail=True, note="그라데이션 웜베이지 — 2024 출시",   new=True),
        "03 버건디":             dict(tone="cool",season=["winter"],           chroma=3,value=2,category="lip",hex="#903060",avail=True, note="그라데이션 버건디 — 2024 출시",     new=True),
    },
    "어퓨 쥬시 팝 틴트 2024": {
        "01 코튼캔디핑크":       dict(tone="cool",season=["spring","summer"],  chroma=2,value=3,category="lip",hex="#E890B8",avail=True, note="솜사탕 쿨핑크 — 2024 출시",         new=True),
        "02 망고코랄":           dict(tone="warm",season=["spring"],           chroma=3,value=3,category="lip",hex="#E8804A",avail=True, note="망고빛 코랄오렌지 — 2024 출시",    new=True),
        "03 피그플럼":           dict(tone="cool",season=["winter"],           chroma=3,value=2,category="lip",hex="#903868",avail=True, note="무화과 플럼 — 2024 출시",           new=True),
    },
    "미샤 아이돌 립 글로우": {
        "01 누드코랄":           dict(tone="warm",season=["spring","autumn"],  chroma=2,value=3,category="lip",hex="#D89070",avail=True, note="촉촉 누드코랄 — 2024 출시",         new=True),
        "02 쿨로즈베리":         dict(tone="cool",season=["summer","winter"],  chroma=2,value=2,category="lip",hex="#C06888",avail=True, note="쿨 로즈베리 글로우 — 2024 출시",    new=True),
        "03 웜브릭":             dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="lip",hex="#A04838",avail=True, note="웜 브릭 레드 — 2024 출시",          new=True),
    },

    # ── BLUSH ────────────────────────────────────────────────
    "롬앤 베러 댄 치크": {
        "피치칩":                dict(tone="warm",season=["spring","autumn"],  chroma=2,value=3,category="blush",hex="#E8A878",avail=True, note="황금 피치, 웜 피부 생기",          new=False),
        "스트로베리밀크":        dict(tone="cool",season=["summer"],           chroma=2,value=3,category="blush",hex="#D898A8",avail=True, note="딸기우유빛 쿨 핑크",               new=False),
        "코랄리프":              dict(tone="warm",season=["spring"],           chroma=3,value=3,category="blush",hex="#E89070",avail=True, note="생생한 코랄",                       new=False),
        "쿨로즈":                dict(tone="cool",season=["winter","summer"],  chroma=2,value=2,category="blush",hex="#C880A0",avail=True, note="블루베이스 쿨 로즈",               new=False),
        "누디피치":              dict(tone="warm",season=["autumn"],           chroma=1,value=2,category="blush",hex="#D0988A",avail=True, note="웜 누디 피치",                      new=False),
        "선셋코랄":              dict(tone="warm",season=["spring","autumn"],  chroma=3,value=2,category="blush",hex="#E07858",avail=True, note="선셋빛 코랄 — 2024 신규",           new=True),
        "라벤더드림":            dict(tone="cool",season=["summer"],           chroma=2,value=3,category="blush",hex="#C0B0D8",avail=True, note="라벤더빛 쿨 — 2024 신규",           new=True),
    },
    "에뛰드 러블리 쿠키 블러셔": {
        "1호 피치":              dict(tone="warm",season=["spring"],           chroma=2,value=3,category="blush",hex="#EDA880",avail=True, note="부드러운 피치",                      new=False),
        "2호 핑크":              dict(tone="cool",season=["summer"],           chroma=2,value=3,category="blush",hex="#E0A0B8",avail=True, note="밝은 쿨핑크",                        new=False),
        "3호 오렌지":            dict(tone="warm",season=["autumn","spring"],  chroma=3,value=3,category="blush",hex="#E89060",avail=True, note="선명한 오렌지",                      new=False),
        "5호 베이지":            dict(tone="warm",season=["autumn"],           chroma=1,value=2,category="blush",hex="#C8A888",avail=True, note="내추럴 베이지 음영",                 new=False),
    },
    "클리오 킬 커버 더 뉴 치크": {
        "02 다이닝로즈":         dict(tone="cool",season=["summer","winter"],  chroma=2,value=3,category="blush",hex="#D890A8",avail=True, note="뮤트 쿨 로즈",                       new=False),
        "03 캐시미어":           dict(tone="warm",season=["autumn"],           chroma=1,value=2,category="blush",hex="#C8A090",avail=True, note="웜 캐시미어 베이지",                 new=False),
        "05 보나피치":           dict(tone="warm",season=["spring","summer"],  chroma=2,value=3,category="blush",hex="#E8A890",avail=True, note="따뜻한 코랄피치",                    new=False),
        "07 쿨모브":             dict(tone="cool",season=["winter"],           chroma=2,value=2,category="blush",hex="#B880A8",avail=True, note="딥 쿨모브",                           new=False),
    },
    "NARS 블러쉬": {
        "오가즘":                dict(tone="warm",season=["spring","summer"],  chroma=2,value=3,category="blush",hex="#E09888",avail=True, note="골드쉬머 피치핑크, 국민템",          new=False),
        "딥트로트":              dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="blush",hex="#C07860",avail=True, note="깊은 테라코타",                       new=False),
        "카마수트라":            dict(tone="cool",season=["winter"],           chroma=3,value=2,category="blush",hex="#B86080",avail=True, note="딥 쿨로즈",                           new=False),
        "부에노스아이레스":      dict(tone="cool",season=["summer"],           chroma=2,value=3,category="blush",hex="#D898B0",avail=True, note="소프트 쿨핑크",                       new=False),
    },
    "페리페라 블러블러 페이스 블러셔": {
        "01 코코피치":           dict(tone="warm",season=["spring","autumn"],  chroma=2,value=3,category="blush",hex="#E0A080",avail=True, note="코코넛 피치",                         new=False),
        "02 쿨로즈퍼지":         dict(tone="cool",season=["summer"],           chroma=2,value=3,category="blush",hex="#D8A0B8",avail=True, note="퍼지 쿨 로즈핑크",                    new=False),
        "03 미드나잇플럼":       dict(tone="cool",season=["winter"],           chroma=3,value=2,category="blush",hex="#A06888",avail=True, note="딥 쿨 플럼",                          new=False),
        "04 어텀테라":           dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="blush",hex="#B07058",avail=True, note="어스 테라코타 — 2024 신규",            new=True),
        "05 스프링코랄":         dict(tone="warm",season=["spring"],           chroma=3,value=3,category="blush",hex="#E09070",avail=True, note="봄 코랄핑크 — 2024 신규",             new=True),
    },
    # 2024 신규 블러셔
    "헤라 센슈얼 파우더 블러셔 2024": {
        "01 로즈코랄":           dict(tone="warm",season=["spring","summer"],  chroma=2,value=3,category="blush",hex="#E09888",avail=True, note="로즈코랄 쉬머 — 2024 출시",          new=True),
        "02 쿨핑크":             dict(tone="cool",season=["summer"],           chroma=2,value=3,category="blush",hex="#D898B8",avail=True, note="쿨핑크 쉬머 — 2024 출시",             new=True),
        "03 딥테라":             dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="blush",hex="#B07060",avail=True, note="딥 테라코타 쉬머 — 2024 출시",        new=True),
    },
    "투쿨포스쿨 체크 체크 블러셔": {
        "01 코튼피치":           dict(tone="warm",season=["spring"],           chroma=2,value=3,category="blush",hex="#EDB090",avail=True, note="코튼 피치 — 2024 출시",               new=True),
        "02 플럼체크":           dict(tone="cool",season=["winter"],           chroma=2,value=2,category="blush",hex="#B07890",avail=True, note="플럼 쿨 — 2024 출시",                 new=True),
    },

    # ── SHADOW ──────────────────────────────────────────────
    "클리오 프로 아이 팔레트": {
        "03 앤틱핑크":           dict(tone="cool",season=["summer","winter"],  chroma=2,value=3,category="shadow",hex="#D8A8B8",avail=True, note="쿨톤 핑크 멀티",                   new=False),
        "04 브라운브릭":         dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="shadow",hex="#987060",avail=True, note="웜 브라운 전문",                   new=False),
        "06 어텀테라":           dict(tone="warm",season=["autumn","spring"],  chroma=2,value=2,category="shadow",hex="#B07858",avail=True, note="테라코타 어텀",                     new=False),
        "09 스모키쿨":           dict(tone="cool",season=["winter"],           chroma=2,value=1,category="shadow",hex="#706880",avail=True, note="쿨톤 스모키 전문",                 new=False),
        "11 로즈골드":           dict(tone="warm",season=["spring","autumn"],  chroma=2,value=3,category="shadow",hex="#C09070",avail=True, note="로즈골드 웜 — 2024 신규",          new=True),
        "12 쿨그레이": dict(tone="cool",season=["winter","summer"],chroma=1,value=2,category="shadow",hex="#9090A8",avail=True, note="쿨 그레이 스모키 — 2024 신규",new=True),
    },
    "에뛰드 플레이 컬러 아이즈": {
        "베어누드":              dict(tone="warm",season=["autumn","spring"],  chroma=1,value=3,category="shadow",hex="#C8B098",avail=True, note="웜 베이지 데일리",                 new=False),
        "라즈베리초콜릿":        dict(tone="cool",season=["winter","summer"],  chroma=2,value=2,category="shadow",hex="#907880",avail=True, note="쿨 다크베리",                      new=False),
        "핑크쉐이드":            dict(tone="cool",season=["summer"],           chroma=2,value=3,category="shadow",hex="#D8A8B8",avail=True, note="소프트 쿨핑크",                    new=False),
        "브라운토피":            dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="shadow",hex="#987060",avail=False,note="웜 토피브라운 ★단종",              new=False),
        "올리브그린":            dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="shadow",hex="#788050",avail=True, note="올리브 어스톤 — 2024 신규",        new=True),
        "코랄선셋":              dict(tone="warm",season=["spring"],           chroma=3,value=3,category="shadow",hex="#E09870",avail=True, note="코랄 선셋 팔레트 — 2024 신규",     new=True),
    },
    "어반디케이 네이키드 팔레트": {
        "NAKED3":                dict(tone="cool",season=["summer","winter"],  chroma=2,value=3,category="shadow",hex="#C090A0",avail=True, note="쿨 로즈 뉴트럴 — 국내 구매가능",  new=False),
        "NAKED RELOADED":        dict(tone="warm",season=["autumn","spring"],  chroma=2,value=2,category="shadow",hex="#B09070",avail=True, note="웜 뉴트럴 — 국내 구매가능",        new=False),
    },
    "맥 아이섀도우 단품": {
        "코퍼스파크":            dict(tone="warm",season=["autumn"],           chroma=3,value=2,category="shadow",hex="#C07840",avail=True, note="쉬머 구리빛",                      new=False),
        "브라운다운":            dict(tone="warm",season=["autumn","spring"],  chroma=2,value=2,category="shadow",hex="#906050",avail=True, note="클래식 웜 브라운",                 new=False),
        "스노우화이트":          dict(tone="cool",season=["winter","summer"],  chroma=1,value=4,category="shadow",hex="#E8E0E8",avail=True, note="쿨 하이라이트 섀도우",             new=False),
    },
    "롬앤 한올한올 아이섀도우": {
        "03 로즈핑크":           dict(tone="cool",season=["summer"],           chroma=2,value=3,category="shadow",hex="#D890A8",avail=True, note="맑은 쿨 로즈",                     new=False),
        "06 코퍼브라운":         dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="shadow",hex="#A07058",avail=True, note="구리빛 브라운",                    new=False),
        "10 테라핑크":           dict(tone="warm",season=["spring"],           chroma=2,value=3,category="shadow",hex="#D89080",avail=True, note="코랄핑크 섀도우",                  new=False),
        "13 스모키그레이":       dict(tone="cool",season=["winter"],           chroma=1,value=2,category="shadow",hex="#888098",avail=True, note="쿨 스모키 그레이",                 new=False),
    },
    # 2024 신규 섀도우
    "페리페라 인크 더 아이섀도우 팔레트 2024": {
        "01 웜어스":             dict(tone="warm",season=["autumn"],           chroma=2,value=2,category="shadow",hex="#A07858",avail=True, note="어스톤 웜 팔레트 — 2024 출시",     new=True),
        "02 쿨로즈":             dict(tone="cool",season=["summer","winter"],  chroma=2,value=3,category="shadow",hex="#C090A8",avail=True, note="쿨 로즈 팔레트 — 2024 출시",       new=True),
        "03 코랄핑크":           dict(tone="warm",season=["spring"],           chroma=3,value=3,category="shadow",hex="#E09078",avail=True, note="코랄핑크 팔레트 — 2024 출시",      new=True),
    },
    "투쿨포스쿨 아트클래스 팔레트 2024": {
        "웜누드":                dict(tone="warm",season=["spring","autumn"],  chroma=1,value=3,category="shadow",hex="#C8A888",avail=True, note="웜 누드 아트 팔레트 — 2024",        new=True),
        "쿨모브":                dict(tone="cool",season=["summer","winter"],  chroma=2,value=2,category="shadow",hex="#9888A8",avail=True, note="쿨 모브 아트 팔레트 — 2024",        new=True),
    },

    # ── BASE ────────────────────────────────────────────────
    "롬앤 그램 글로잉 사틴 파운데이션": {
        "13N 아이보리":          dict(tone="warm",season=["spring","autumn"],  chroma=1,value=3,category="base",hex="#E8C8A8",avail=True, note="웜 밝은 피부",                       new=False),
        "21N 라이트베이지":      dict(tone="warm",season=["autumn"],           chroma=1,value=3,category="base",hex="#DEC0A0",avail=True, note="웜 자연 피부",                       new=False),
        "23C 쿨내추럴":          dict(tone="cool",season=["summer"],           chroma=1,value=3,category="base",hex="#D8C0B0",avail=True, note="쿨 밝은 피부",                       new=False),
        "25C 쿨베이지":          dict(tone="cool",season=["winter"],           chroma=1,value=2,category="base",hex="#D0B8A8",avail=True, note="쿨 중간 피부",                       new=False),
    },
    "에스쁘아 프로 태일러 파운데이션": {
        "1W 아이보리":           dict(tone="warm",season=["spring","autumn"],  chroma=1,value=3,category="base",hex="#EAD0B0",avail=True, note="웜 피부, 자연 밀착",                 new=False),
        "2N 내추럴":             dict(tone="warm",season=["autumn"],           chroma=1,value=3,category="base",hex="#DEC0A0",avail=True, note="웜 중간 피부",                       new=False),
        "3C 쿨베이지":           dict(tone="cool",season=["summer","winter"],  chroma=1,value=3,category="base",hex="#D0B8A8",avail=True, note="쿨 베이지",                          new=False),
    },
    "클리오 킬 커버 파운웨어 쿠션 2024": {
        "1W 워너비아이보리":     dict(tone="warm",season=["spring","autumn"],  chroma=1,value=3,category="base",hex="#EED0A8",avail=True, note="웜 아이보리 쿠션 — 2024 신규",        new=True),
        "2N 내추럴베이지":       dict(tone="warm",season=["autumn"],           chroma=1,value=3,category="base",hex="#E0C0A0",avail=True, note="웜 내추럴 쿠션 — 2024 신규",          new=True),
        "3C 쿨샌드":             dict(tone="cool",season=["summer","winter"],  chroma=1,value=3,category="base",hex="#D8C0B0",avail=True, note="쿨 샌드 쿠션 — 2024 신규",            new=True),
    },
}

# ══════════════════════════════════════════════════════════════
# 퍼스널 컬러 세부 8톤
# ══════════════════════════════════════════════════════════════
PC = {
    "봄 라이트 웜":   dict(tone="warm",season="spring",emoji="🌸",kw=["맑음","생기","복숭아","산뜻 코랄"],       desc="피부가 밝고 투명감이 있어요. 밝고 산뜻한 코랄·피치 계열이 잘 어울려요.",               best=["코랄","피치","살구","밝은 오렌지","라이트 브라운"],       avoid=["쿨 로즈","버건디","딥 퍼플","그레이"],  bg="linear-gradient(135deg,#FFFBE0,#FFF3C8)",bd="#E8D868"),
    "봄 비비드 웜":   dict(tone="warm",season="spring",emoji="🌺",kw=["선명함","활기","코랄레드","오렌지"],       desc="맑고 선명한 컬러가 피부에 생기를 더해요. 비비드 코랄~레드가 특히 잘 어울려요.",            best=["코랄레드","오렌지레드","밝은 핑크"],                       avoid=["뮤트 컬러","다크 브라운","그레이"],     bg="linear-gradient(135deg,#FFF8D0,#FFE890)",bd="#E0C840"),
    "가을 딥 웜":     dict(tone="warm",season="autumn",emoji="🍂",kw=["깊이","테라코타","어스톤","내추럴"],       desc="황금빛이 도는 깊고 풍부한 웜톤이에요. 테라코타·브릭·카멜이 완벽하게 어울려요.",             best=["테라코타","브릭레드","머스타드","카멜","올리브"],           avoid=["형광","네온","아이시 컬러"],             bg="linear-gradient(135deg,#FFF5D0,#FFEBA0)",bd="#DCCC50"),
    "가을 뮤트 웜":   dict(tone="warm",season="autumn",emoji="🌾",kw=["차분함","뮤트","누드","내추럴"],          desc="채도가 낮고 부드러운 웜톤이에요. 뮤트한 브라운~누드 계열이 자연스러워요.",                   best=["카멜누드","웜베이지","머스타드뮤트","로즈브라운"],         avoid=["비비드","형광","쿨 핑크"],              bg="linear-gradient(135deg,#FFFAE0,#FFF3B8)",bd="#E0D060"),
    "여름 라이트 쿨": dict(tone="cool",season="summer",emoji="🌊",kw=["부드러움","로맨틱","파스텔","파우더리"],  desc="밝고 부드러운 쿨톤이에요. 파스텔 핑크·라벤더·뮤트 로즈가 우아하게 어울려요.",                best=["파스텔핑크","라벤더","소프트 로즈"],                       avoid=["오렌지","옐로우","골드 쉬머"],          bg="linear-gradient(135deg,#F0F4FF,#E0EAFF)",bd="#A8C0E8"),
    "여름 뮤트 쿨":   dict(tone="cool",season="summer",emoji="🩵",kw=["차분함","뮤트","로즈브라운","그레이시"],  desc="채도가 낮고 세련된 쿨톤이에요. 뮤트 로즈·그레이핑크 계열이 지적으로 어울려요.",               best=["뮤트 로즈","그레이핑크","라이트 퍼플"],                   avoid=["오렌지","테라코타","골드"],             bg="linear-gradient(135deg,#EEF2FF,#E0E8FF)",bd="#A0B8E8"),
    "겨울 딥 쿨":     dict(tone="cool",season="winter",emoji="❄️",kw=["선명함","대비","딥레드","플럼"],          desc="선명하고 강한 쿨톤이에요. 딥레드·플럼·버건디가 드라마틱하게 어울려요.",                      best=["딥레드","플럼","버건디","쿨 핑크"],                        avoid=["오렌지","코랄","웜 브라운","베이지"],   bg="linear-gradient(135deg,#EAF0FF,#D8E4FF)",bd="#98B0E0"),
    "겨울 비비드 쿨": dict(tone="cool",season="winter",emoji="💙",kw=["대담함","비비드","블루베이스","강렬함"],  desc="강렬하고 비비드한 쿨톤이에요. 블루베이스 레드·선명한 핑크가 빛나요.",                          best=["블루베이스 레드","비비드 핑크","퓨어 블랙","퓨어 화이트"], avoid=["파스텔","피치","코랄","웜 브라운"],     bg="linear-gradient(135deg,#E8EEFF,#D8E0FF)",bd="#90A8E0"),
}

PAIRING = {
    ("spring","blush"):  [("롬앤 베러 댄 치크","코랄리프"),("에뛰드 러블리 쿠키 블러셔","1호 피치"),("NARS 블러쉬","오가즘"),("헤라 센슈얼 파우더 블러셔 2024","01 로즈코랄")],
    ("spring","shadow"): [("클리오 프로 아이 팔레트","06 어텀테라"),("에뛰드 플레이 컬러 아이즈","베어누드"),("페리페라 인크 더 아이섀도우 팔레트 2024","03 코랄핑크"),("롬앤 한올한올 아이섀도우","10 테라핑크")],
    ("autumn","blush"):  [("NARS 블러쉬","딥트로트"),("클리오 킬 커버 더 뉴 치크","03 캐시미어"),("페리페라 블러블러 페이스 블러셔","04 어텀테라"),("헤라 센슈얼 파우더 블러셔 2024","03 딥테라")],
    ("autumn","shadow"): [("클리오 프로 아이 팔레트","04 브라운브릭"),("어반디케이 네이키드 팔레트","NAKED RELOADED"),("맥 아이섀도우 단품","코퍼스파크"),("페리페라 인크 더 아이섀도우 팔레트 2024","01 웜어스")],
    ("summer","blush"):  [("롬앤 베러 댄 치크","스트로베리밀크"),("에뛰드 러블리 쿠키 블러셔","2호 핑크"),("NARS 블러쉬","부에노스아이레스"),("투쿨포스쿨 체크 체크 블러셔","02 플럼체크")],
    ("summer","shadow"): [("클리오 프로 아이 팔레트","03 앤틱핑크"),("에뛰드 플레이 컬러 아이즈","핑크쉐이드"),("어반디케이 네이키드 팔레트","NAKED3"),("페리페라 인크 더 아이섀도우 팔레트 2024","02 쿨로즈")],
    ("winter","blush"):  [("NARS 블러쉬","카마수트라"),("롬앤 베러 댄 치크","쿨로즈"),("페리페라 블러블러 페이스 블러셔","03 미드나잇플럼"),("클리오 킬 커버 더 뉴 치크","07 쿨모브")],
    ("winter","shadow"): [("클리오 프로 아이 팔레트","09 스모키쿨"),("어반디케이 네이키드 팔레트","NAKED3"),("투쿨포스쿨 아트클래스 팔레트 2024","쿨모브"),("클리오 프로 아이 팔레트","12 쿨그레이")],
}

CAT_KR = {"lip":"💄 립","blush":"🌸 블러셔","shadow":"✨ 섀도우","base":"🫧 베이스"}
SEA_KR = {"spring":"봄 웜","autumn":"가을 웜","summer":"여름 쿨","winter":"겨울 쿨"}

def dot_html(hex_col, size=18):
    return f'<span class="dot" style="width:{size}px;height:{size}px;background:{hex_col};"></span>'

def tag_html(text, cls):
    return f'<span class="tag {cls}">{text}</span>'

def tone_tag(t):
    return tag_html("🌞 웜톤" if t=="warm" else "❄️ 쿨톤", f"t-{t}")

def sea_tag(s):
    return tag_html(SEA_KR.get(s,""), f"t-{s}")

def new_tag():
    return tag_html("✨ NEW", "t-new")

def pcard_html(pname, shade, d, fit=""):
    fit_part = f'<div class="pcard-fit">{fit}</div>' if fit else ""
    new_part = new_tag() if d.get("new") else ""
    return f"""
<div class="pcard">
    {dot_html(d['hex'],20)}
    <div class="pcard-info">
        <div class="pcard-name">{pname} {new_part}</div>
        <div class="pcard-shade">{shade} · {CAT_KR.get(d['category'],'')}</div>
        <div class="pcard-note">{d['note']}</div>
    </div>
    {fit_part}
</div>"""


# ── 분석 엔진 ──────────────────────────────────────────────────
def run_analysis(good_list, bad_list, best_list):
    ts = cs = vs = wt = 0.0
    def acc(items, w):
        nonlocal ts, cs, vs, wt
        for item in items:
            if not item: continue
            pn, sh = item
            d = DB[pn][sh]
            ts += (1 if d["tone"]=="warm" else -1)*w
            cs += d["chroma"]*w; vs += d["value"]*w; wt += abs(w)
    acc(good_list,1.0); acc(best_list,2.0); acc(bad_list,-1.5)
    if wt == 0: return None
    ac, av = cs/wt, vs/wt
    if ts > 0:
        pc = ("봄 비비드 웜" if ac>=2.5 else "봄 라이트 웜") if av>=2.8 \
        else ("가을 딥 웜"   if ac>=2.0 else "가을 뮤트 웜")
    else:
        pc = ("여름 라이트 쿨" if ac>=2.3 else "여름 뮤트 쿨") if av>=2.8 \
        else ("겨울 비비드 쿨" if ac>=2.5 else "겨울 딥 쿨")
    return {"pc":pc,"tone":"warm" if ts>0 else "cool","season":PC[pc]["season"]}


def get_recs(tone, season, cat=None, limit=8, new_only=False):
    perfect, good = [], []
    for pn, shades in DB.items():
        for sh, d in shades.items():
            if not d["avail"]: continue
            if cat and d["category"]!=cat: continue
            if new_only and not d.get("new"): continue
            if d["tone"]==tone and season in d["season"]: perfect.append((pn,sh,d))
            elif d["tone"]==tone: good.append((pn,sh,d))
    return (perfect+good)[:limit]


# ── 핵심 개선: 선택 즉시 뱃지 표시 위젯 ─────────────────────────
def product_picker(prefix, include_disc=False):
    cat_labels = ["전체","💄 립","🌸 블러셔","✨ 섀도우","🫧 베이스"]
    cat_map    = {"전체":None,"💄 립":"lip","🌸 블러셔":"blush","✨ 섀도우":"shadow","🫧 베이스":"base"}

    chosen_lbl = st.selectbox("카", cat_labels, key=f"{prefix}_cat", label_visibility="collapsed")
    chosen_cat = cat_map[chosen_lbl]

    pnames = sorted({
        pn for pn, shades in DB.items()
        for sh, d in shades.items()
        if (chosen_cat is None or d["category"]==chosen_cat)
        and (include_disc or d["avail"])
    })

    pname = st.selectbox(
        "제품명", pnames, index=None, placeholder="제품명을 선택하세요",
        key=f"{prefix}_pname", label_visibility="collapsed"
    )
    if not pname:
        return None

    shade_opts = [sh for sh, d in DB[pname].items() if include_disc or d["avail"]]
    shade = st.selectbox(
        "호수", shade_opts, index=None, placeholder="컬러·호수를 선택하세요",
        key=f"{prefix}_shade", label_visibility="collapsed"
    )
    if not shade:
        return None

    # ★ 핵심 개선: 선택 즉시 이름+컬러 뱃지로 표시
    d = DB[pname][shade]
    disc_txt = " <span class='tag t-disc'>단종</span>" if not d["avail"] else ""
    new_txt  = new_tag() if d.get("new") else ""
    st.markdown(f"""
<div class="selected-badge">
    {dot_html(d['hex'],22)}
    <div>
        <div class="badge-name">{pname} {new_txt}{disc_txt}</div>
        <div class="badge-shade">{shade} &nbsp;·&nbsp; {CAT_KR.get(d['category'],'')}</div>
        <div class="badge-note">{tone_tag(d['tone'])} {''.join(sea_tag(s) for s in d['season'])} &nbsp; {d['note']}</div>
    </div>
</div>""", unsafe_allow_html=True)
    return (pname, shade)


# ══════════════════════════════════════════════════════════════
# TAB 1  퍼스널 컬러 분석
# ══════════════════════════════════════════════════════════════
def tab_analysis():
    st.markdown('<p class="sec-head">퍼스널 컬러 분석</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sec-sub">사용해봤던 제품들을 입력하면 세부 8톤 퍼스널 컬러를 분석해드려요.<br>'
        '<b>잘 맞았던 제품 1개</b>만 있어도 분석 가능 &nbsp;·&nbsp; 안 맞았던·반응 좋았던 제품은 각 1~3개 자유 입력</p>',
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
        st.markdown('<div class="col-label">👍 잘 맞았던 제품 &nbsp;·&nbsp; 필수 1–3개</div>', unsafe_allow_html=True)
        g1 = product_picker("g1", include_disc=True)
        st.divider()
        g2 = product_picker("g2", include_disc=True)
        st.divider()
        g3 = product_picker("g3", include_disc=True)

    with c2:
        st.markdown('<div class="col-label">👎 안 맞았던 제품 &nbsp;·&nbsp; 선택 1–3개</div>', unsafe_allow_html=True)
        b1 = product_picker("b1", include_disc=True)
        st.divider()
        b2 = product_picker("b2", include_disc=True)
        st.divider()
        b3 = product_picker("b3", include_disc=True)

    with c3:
        st.markdown('<div class="col-label">🔥 반응 좋았던 제품 &nbsp;·&nbsp; 선택 1–3개</div>', unsafe_allow_html=True)
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
    pc   = res["pc"]
    info = PC[pc]
    tone = res["tone"]
    st.divider()
    box_cls = "rbox-warm" if tone=="warm" else "rbox-cool"
    kw_html = "".join(f"<span class='tag t-{tone}'>{k}</span>" for k in info["kw"])
    st.markdown(f"""
<div class="{box_cls}">
    <div class="rbox-title">{info['emoji']} {pc}</div>
    <div class="rbox-desc">{info['desc']}</div>
    <div style="margin-top:0.8rem">{kw_html}</div>
</div>""", unsafe_allow_html=True)

    r1, r2 = st.columns(2)
    with r1:
        st.markdown("**✅ 잘 어울리는 컬러**")
        for c in info["best"]:  st.markdown(f"· {c}")
    with r2:
        st.markdown("**⛔ 피하면 좋은 컬러**")
        for c in info["avoid"]: st.markdown(f"· {c}")

    st.markdown("#### 🎁 맞춤 추천 제품")

    # ★ 추가 기능: 신제품 필터
    col_cat, col_new = st.columns([3,1])
    with col_cat:
        cat_choice = st.radio("", ["전체","💄 립","🌸 블러셔","✨ 섀도우"],
                              horizontal=True, key="res_cat", label_visibility="collapsed")
    with col_new:
        new_only = st.checkbox("✨ 2024+ 신제품만", key="res_new")

    cmap = {"전체":None,"💄 립":"lip","🌸 블러셔":"blush","✨ 섀도우":"shadow"}
    recs = get_recs(res["tone"], res["season"], cat=cmap[cat_choice], limit=8, new_only=new_only)

    if not recs:
        st.info("해당 조건의 추천 제품이 없어요.")
        return
    cols = st.columns(2)
    for i, (pn, sh, d) in enumerate(recs):
        fit = "✨ 완벽 매칭" if res["season"] in d["season"] else "👍 어울려요"
        with cols[i%2]:
            st.markdown(pcard_html(pn,sh,d,fit), unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TAB 2  연계 추천
# ══════════════════════════════════════════════════════════════
def tab_pairing():
    st.markdown('<p class="sec-head">연계 추천 서비스</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sec-sub">퍼스널 컬러를 선택하면 립·블러셔·섀도우를 함께 큐레이션해드려요.<br>'
        '분석 탭 결과가 있다면 아래 버튼으로 자동 적용 가능해요.</p>',
        unsafe_allow_html=True,
    )

    pc_list = list(PC.keys())
    auto_pc = st.session_state.get("result",{}).get("pc",pc_list[0])
    default_idx = pc_list.index(auto_pc) if auto_pc in pc_list else 0
    pc_sel = st.selectbox("퍼스널 컬러 선택", pc_list, index=default_idx, key="pair_pc")

    if st.session_state.get("result"):
        if st.button("🎯 분석 결과 자동 적용"):
            st.session_state["pair_pc"] = st.session_state["result"]["pc"]
            st.rerun()

    info   = PC[pc_sel]
    tone   = info["tone"]
    season = info["season"]

    st.markdown(f"""
<div class="info-band {'ib-warm' if tone=='warm' else 'ib-cool'}">
    <b>{info['emoji']} {pc_sel}</b> &nbsp; {tone_tag(tone)} {sea_tag(season)}<br>
    <small style="color:#555">{info['desc']}</small>
</div>""", unsafe_allow_html=True)

    st.markdown("### 💄 추천 립")
    lip_recs = get_recs(tone, season, cat="lip", limit=6)
    lc = st.columns(3)
    for i, (pn, sh, d) in enumerate(lip_recs):
        with lc[i%3]:
            st.markdown(f"""
<div class="pcard" style="flex-direction:column;align-items:flex-start;gap:0.28rem;">
    <div style="display:flex;align-items:center;gap:0.55rem">
        {dot_html(d['hex'],24)} <b style="font-size:0.83rem">{pn}</b>
        {'&nbsp;'+new_tag() if d.get('new') else ''}
    </div>
    <div style="padding-left:30px">
        <div class="pcard-shade">{sh}</div>
        <div class="pcard-note">{d['note']}</div>
    </div>
</div>""", unsafe_allow_html=True)

    st.divider()

    st.markdown("### 🌸 어울리는 블러셔")
    bkey = (season,"blush")
    blush_items = [(pn,sh,DB[pn][sh]) for pn,sh in PAIRING.get(bkey,[])
                   if pn in DB and sh in DB[pn] and DB[pn][sh]["avail"]] \
                  or [(pn,sh,d) for pn,sh,d in get_recs(tone,season,cat="blush",limit=4)]
    bc = st.columns(2)
    for i,(pn,sh,d) in enumerate(blush_items[:4]):
        with bc[i%2]:
            st.markdown(pcard_html(pn,sh,d), unsafe_allow_html=True)

    st.divider()

    st.markdown("### ✨ 어울리는 섀도우")
    skey = (season,"shadow")
    shadow_items = [(pn,sh,DB[pn][sh]) for pn,sh in PAIRING.get(skey,[])
                    if pn in DB and sh in DB[pn] and DB[pn][sh]["avail"]] \
                   or [(pn,sh,d) for pn,sh,d in get_recs(tone,season,cat="shadow",limit=4)]
    sc = st.columns(2)
    for i,(pn,sh,d) in enumerate(shadow_items[:4]):
        with sc[i%2]:
            st.markdown(pcard_html(pn,sh,d), unsafe_allow_html=True)

    st.divider()
    tips = {
        "spring": "봄 웜톤은 **밝고 산뜻한 코랄·피치 조합**이 최고예요. 골드 액세서리와도 찰떡이에요.",
        "autumn": "가을 웜톤은 **어스톤·테라코타 팔레트**로 풍부한 매력을 살려보세요. 로즈골드 쥬얼리와 잘 어울려요.",
        "summer": "여름 쿨톤은 **뮤트 핑크·라벤더 조합**이 세련돼요. 실버 액세서리가 피부를 더 빛나게 해줘요.",
        "winter": "겨울 쿨톤은 **강렬한 컨트라스트**가 매력이에요. 선명한 레드 립 하나로 전체 룩을 완성해보세요.",
    }
    st.info(tips.get(season,""))


# ══════════════════════════════════════════════════════════════
# TAB 3  제품 탐색
# ══════════════════════════════════════════════════════════════
def tab_browse():
    st.markdown('<p class="sec-head">제품 탐색</p>', unsafe_allow_html=True)
    st.markdown('<p class="sec-sub">카테고리·톤·계절로 필터링해서 전체 제품을 살펴보세요.</p>', unsafe_allow_html=True)

    f1,f2,f3,f4 = st.columns(4)
    with f1: fcat  = st.selectbox("카테고리",["전체","💄 립","🌸 블러셔","✨ 섀도우","🫧 베이스"],key="br_cat")
    with f2: ftone = st.selectbox("톤",["전체","🌞 웜톤","❄️ 쿨톤"],key="br_tone")
    with f3: fsea  = st.selectbox("계절",["전체","봄 웜","가을 웜","여름 쿨","겨울 쿨"],key="br_sea")
    with f4: fnew  = st.selectbox("출시연도",["전체","✨ 2024+ 신제품"],key="br_new")

    show_disc = st.checkbox("단종 제품도 보기", value=False)

    cmap={"전체":None,"💄 립":"lip","🌸 블러셔":"blush","✨ 섀도우":"shadow","🫧 베이스":"base"}
    tmap={"전체":None,"🌞 웜톤":"warm","❄️ 쿨톤":"cool"}
    smap={"전체":None,"봄 웜":"spring","가을 웜":"autumn","여름 쿨":"summer","겨울 쿨":"winter"}
    fc,ft,fs = cmap[fcat],tmap[ftone],smap[fsea]
    only_new = (fnew=="✨ 2024+ 신제품")

    rows=[]
    for pn,shades in DB.items():
        for sh,d in shades.items():
            if not show_disc and not d["avail"]: continue
            if fc and d["category"]!=fc: continue
            if ft and d["tone"]!=ft: continue
            if fs and fs not in d["season"]: continue
            if only_new and not d.get("new"): continue
            rows.append((pn,sh,d))

    st.markdown(f"<small style='color:#8A7830'>{len(rows)}개 제품</small>", unsafe_allow_html=True)
    if not rows:
        st.info("조건에 맞는 제품이 없어요.")
        return

    for i in range(0,len(rows),3):
        cols = st.columns(3)
        for j,(pn,sh,d) in enumerate(rows[i:i+3]):
            with cols[j]:
                disc = " <span class='tag t-disc'>단종</span>" if not d["avail"] else ""
                new_part = new_tag() if d.get("new") else ""
                st.markdown(f"""
<div class="pcard" style="flex-direction:column;align-items:flex-start;border-radius:12px;padding:0.9rem;gap:0.35rem;">
    <div style="display:flex;align-items:center;gap:0.6rem">
        {dot_html(d['hex'],22)}
        <div>
            <div class="pcard-name">{pn}{disc} {new_part}</div>
            <div class="pcard-shade">{sh}</div>
        </div>
    </div>
    <div class="pcard-note">{d['note']}</div>
    <div>{tone_tag(d['tone'])} {''.join(sea_tag(s) for s in d['season'])} {tag_html(CAT_KR.get(d['category'],''),'t-cat')}</div>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TAB 4  컬러 가이드
# ══════════════════════════════════════════════════════════════
def tab_guide():
    st.markdown('<p class="sec-head">퍼스널 컬러 가이드</p>', unsafe_allow_html=True)
    st.markdown('<p class="sec-sub">세부 8톤의 특징과 뷰티 스타일링 팁을 한눈에 확인하세요.</p>', unsafe_allow_html=True)

    for pc_name,info in PC.items():
        tone = info["tone"]
        with st.expander(f"{info['emoji']}  {pc_name}"):
            a,b = st.columns([3,2])
            with a:
                kw_html = "".join(f"<span class='tag t-{tone}'>{k}</span>" for k in info["kw"])
                st.markdown(f"""
<div style="background:{info['bg']};border:1px solid {info['bd']};border-radius:13px;padding:1.2rem 1.5rem;">
    <b style="font-size:1rem">{info['emoji']} {pc_name}</b><br>
    <div style="font-size:0.84rem;color:#444;margin:0.45rem 0;line-height:1.7">{info['desc']}</div>
    <div>{kw_html}</div>
</div>""", unsafe_allow_html=True)
            with b:
                st.markdown("**✅ 어울리는 컬러**")
                for c in info["best"]:  st.markdown(f"· {c}")
                st.markdown("**⛔ 피할 컬러**")
                for c in info["avoid"]: st.markdown(f"· {c}")

            st.markdown("**🛍️ 대표 추천 제품**")
            recs = get_recs(tone, info["season"], limit=4)
            gc = st.columns(4)
            for i,(pn,sh,d) in enumerate(recs):
                with gc[i]:
                    st.markdown(f"""
<div style="text-align:center;padding:0.45rem 0.2rem;">
    <div style="width:32px;height:32px;border-radius:50%;background:{d['hex']};margin:0 auto 0.3rem;border:2px solid rgba(0,0,0,0.07);"></div>
    <div style="font-size:0.73rem;font-weight:500;line-height:1.3">{pn}</div>
    <div style="font-size:0.68rem;color:#A09830">{sh}</div>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TAB 5  ★ 추가 기능: 오늘의 뷰티 조합 추천
# ══════════════════════════════════════════════════════════════
def tab_today():
    st.markdown('<p class="sec-head">오늘의 뷰티 조합</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sec-sub">상황·분위기를 선택하면 퍼스널 컬러에 맞는 오늘의 완성 메이크업 조합을 추천해드려요.</p>',
        unsafe_allow_html=True,
    )

    pc_list = list(PC.keys())
    auto_pc = st.session_state.get("result",{}).get("pc",pc_list[0])
    default_idx = pc_list.index(auto_pc) if auto_pc in pc_list else 0

    co1, co2, co3 = st.columns(3)
    with co1:
        pc_sel = st.selectbox("내 퍼스널 컬러", pc_list, index=default_idx, key="today_pc")
    with co2:
        mood = st.selectbox("오늘의 무드", ["데일리 내추럴", "오피스 룩", "데이트 메이크업", "파티·이벤트", "페스티벌"], key="today_mood")
    with co3:
        intensity = st.selectbox("강도", ["라이트", "미디엄", "스트롱"], key="today_int")

    if st.session_state.get("result"):
        if st.button("🎯 내 분석 결과 자동 적용", key="today_auto"):
            st.rerun()

    info   = PC[pc_sel]
    tone   = info["tone"]
    season = info["season"]

    # 무드별 조합 가이드
    mood_guide = {
        "데일리 내추럴":  {"lip_cat":1,"blush_cat":1,"shadow_cat":1,"lip_kw":"누드·코랄 계열","blush_kw":"가벼운 피치","shadow_kw":"베이지 단색"},
        "오피스 룩":      {"lip_cat":1,"blush_cat":1,"shadow_cat":1,"lip_kw":"뮤트 누드","blush_kw":"자연스러운 베이지","shadow_kw":"브라운 그라데이션"},
        "데이트 메이크업":{"lip_cat":2,"blush_cat":2,"shadow_cat":2,"lip_kw":"로즈·코랄 포인트","blush_kw":"화사한 핑크·피치","shadow_kw":"글리터 포인트"},
        "파티·이벤트":   {"lip_cat":3,"blush_cat":2,"shadow_cat":3,"lip_kw":"비비드·딥 컬러","blush_kw":"선명한 컬러","shadow_kw":"스모키·글리터"},
        "페스티벌":       {"lip_cat":3,"blush_cat":3,"shadow_cat":3,"lip_kw":"선명한 컬러","blush_kw":"대담한 컬러","shadow_kw":"대담한 컬러"},
    }
    g = mood_guide[mood]

    int_map = {"라이트":1,"미디엄":2,"스트롱":3}
    chroma_min = max(1, int_map[intensity]-1)
    chroma_max = min(4, int_map[intensity]+1)

    def filtered_recs(cat, limit=3):
        results = []
        for pn, shades in DB.items():
            for sh, d in shades.items():
                if not d["avail"]: continue
                if d["category"]!=cat: continue
                if not (chroma_min <= d["chroma"] <= chroma_max): continue
                if d["tone"]==tone and season in d["season"]:
                    results.append((pn,sh,d,"perfect"))
                elif d["tone"]==tone:
                    results.append((pn,sh,d,"good"))
        results.sort(key=lambda x: 0 if x[3]=="perfect" else 1)
        return results[:limit]

    st.markdown(f"""
<div class="info-band {'ib-warm' if tone=='warm' else 'ib-cool'}">
    <b>{info['emoji']} {pc_sel}</b> &nbsp;·&nbsp; <b>{mood}</b> &nbsp;·&nbsp; <b>{intensity}</b><br>
    <small style="color:#555">아래 조합으로 오늘 메이크업을 완성해보세요 ✨</small>
</div>""", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)
    sections = [
        (m1, "💄 립 추천", "lip", g["lip_kw"]),
        (m2, "🌸 블러셔 추천", "blush", g["blush_kw"]),
        (m3, "✨ 섀도우 추천", "shadow", g["shadow_kw"]),
    ]
    for col, title, cat, kw in sections:
        with col:
            st.markdown(f"**{title}**")
            st.markdown(f"<small style='color:#8A7830'>{kw}</small>", unsafe_allow_html=True)
            recs = filtered_recs(cat, limit=3)
            if not recs:
                recs_fallback = get_recs(tone, season, cat=cat, limit=2)
                recs = [(pn,sh,d,"good") for pn,sh,d in recs_fallback]
            for pn, sh, d, fit in recs:
                new_p = new_tag() if d.get("new") else ""
                st.markdown(f"""
<div class="pcard" style="flex-direction:column;align-items:flex-start;gap:0.25rem;margin-bottom:0.4rem;">
    <div style="display:flex;align-items:center;gap:0.5rem">
        {dot_html(d['hex'],20)} <b style="font-size:0.8rem;line-height:1.3">{pn} {new_p}</b>
    </div>
    <div style="padding-left:26px;font-size:0.75rem;color:#6A6030">{sh}</div>
    <div style="padding-left:26px;font-size:0.7rem;color:#A09830">{d['note']}</div>
</div>""", unsafe_allow_html=True)

    st.divider()
    # 메이크업 팁
    tips_by_mood = {
        "데일리 내추럴": "💡 **데일리 팁**: 베이스를 가볍게 하고 립 하나로 생기를 더해보세요. 피부 표현에 집중하면 훨씬 자연스러워요.",
        "오피스 룩":     "💡 **오피스 팁**: 눈썹을 단정히 정리하고 뮤트 컬러로 통일감을 주세요. 번들거림 없는 매트 마감이 프로페셔널해 보여요.",
        "데이트 메이크업":"💡 **데이트 팁**: 립과 블러셔를 같은 계열로 맞추면 얼굴이 화사해 보여요. 속눈썹 컬링으로 눈을 더 크게!",
        "파티·이벤트":  "💡 **파티 팁**: 포인트를 한 곳(립 또는 눈)에만 주면 과하지 않고 세련돼 보여요. 하이라이터로 광채를 더해보세요.",
        "페스티벌":      "💡 **페스티벌 팁**: 방수 제품을 우선적으로 선택하세요. 글리터 섀도우를 눈꼬리에만 살짝 올리면 화려함 UP!",
    }
    st.info(tips_by_mood.get(mood,""))


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════
def main():
    st.markdown("""
<div class="hero-title">TONE<em>ME</em></div>
<div class="hero-bar"></div>
<div class="hero-sub">퍼스널 컬러 기반 뷰티 큐레이터 &nbsp;·&nbsp; 세부 8톤 분석 &nbsp;·&nbsp; 국내 구매 가능 제품 &nbsp;·&nbsp; 2024 신제품 포함</div>
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
        '<div class="footer">TONEME &nbsp;·&nbsp; 단종 제품은 추천 제외 &nbsp;·&nbsp; 국내 구매 가능 &nbsp;·&nbsp; 2024 신제품 포함</div>',
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
