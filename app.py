"""MenuMind AI Streamlit presentation interface."""

import streamlit as st

from backend import run_analysis, run_campaign, run_foodie
from data import BAKU, BAKU_NAMES, RESTAURANT_PWS, RESTAURANT_STATS, T
from frontend import PALETTES, get_css

st.set_page_config(page_title="MenuMind AI", page_icon="🍽️", layout="wide")

for k, v in {"page": "landing", "lang": "EN", "theme": "dark", "auth": False,
             "auth_restaurant": None,
             "analysis": None, "campaign": None, "foodie_res": None, "foodie_data": None}.items():
    if k not in st.session_state:
        st.session_state[k] = v

def t(k):
    e = T.get(k, {})
    return e.get(st.session_state.lang, e.get("EN", k))

def clear_generated_outputs():
    st.session_state.analysis = None
    st.session_state.campaign = None
    st.session_state.foodie_res = None
    st.session_state.foodie_data = None

# Inject CSS FIRST so navbar inputs are styled correctly
st.markdown(get_css(st.session_state.theme), unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════
# NAVBAR
# ═══════════════════════════════════════════════════════════════════════
nb_l, nb_m, nb_r1, nb_r2 = st.columns([3, 4, 1.5, 1.5])
with nb_l:
    st.markdown('<div class="mm-brand"><span class="dot"></span>MenuMind <em style="font-style:italic;font-weight:400;">AI</em></div>', unsafe_allow_html=True)
with nb_m:
    api_key = st.text_input("api", type="password", placeholder=t("api_label"),
                            label_visibility="collapsed", key="nb_api")
with nb_r1:
    lang_map = {"English": "EN", "Azərbaycanca": "AZ", "Русский": "RU"}
    code_to_label = {v: k for k, v in lang_map.items()}
    current_label = code_to_label.get(st.session_state.lang, "English")
    sel = st.selectbox("lang", list(lang_map.keys()),
                       index=list(lang_map.keys()).index(current_label),
                       label_visibility="collapsed", key="nb_lang")
    if lang_map[sel] != st.session_state.lang:
        st.session_state.lang = lang_map[sel]
        clear_generated_outputs()
        st.rerun()
with nb_r2:
    th_labels = [t("td"), t("tl")]
    current_th_idx = 0 if st.session_state.theme == "dark" else 1
    sel_th = st.selectbox("theme", th_labels, index=current_th_idx,
                          label_visibility="collapsed", key="nb_theme")
    new_th = "dark" if sel_th == t("td") else "light"
    if new_th != st.session_state.theme:
        st.session_state.theme = new_th
        st.rerun()

# ═══════════════════════════════════════════════════════════════════════
# PAGE ROUTER
# ═══════════════════════════════════════════════════════════════════════

# ─── LANDING ───────────────────────────────────────────────────────────
if st.session_state.page == "landing":
    title = t('hero_title')
    # italicize the last word of the title in serif accent
    words = title.split()
    if len(words) > 2:
        title_html = ' '.join(words[:-1]) + f' <em>{words[-1]}</em>'
    else:
        title_html = f'<em>{title}</em>'
    st.markdown(f"""
    <div class="mm-hero">
        <div class="mm-eyebrow">— Baku · Restaurant Intelligence —</div>
        <h1>{title_html}</h1>
        <div class="sub">{t('hero_sub')}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown(f"""
        <div class="mm-card">
            <div class="num">01 / EXPLORER</div>
            <h3>{t('card_foodie_t')}</h3>
            <p>{t('card_foodie_d')}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
        if st.button(t("card_foodie_t"), use_container_width=True, type="primary", key="go_f"):
            st.session_state.page = "foodie"
            st.rerun()
    with c2:
        st.markdown(f"""
        <div class="mm-card">
            <div class="num">02 / OPERATOR</div>
            <h3>{t('card_exec_t')}</h3>
            <p>{t('card_exec_d')}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
        if st.button(t("card_exec_t"), use_container_width=True, type="primary", key="go_e"):
            st.session_state.page = "exec"
            st.rerun()

# ─── FOODIE MODULE ─────────────────────────────────────────────────────
elif st.session_state.page == "foodie":
    back_col, _ = st.columns([2, 8])
    with back_col:
        if st.button(t("back"), key="back_f"):
            st.session_state.page = "landing"
            st.session_state.foodie_res = None
            st.session_state.foodie_data = None
            st.rerun()

    st.markdown(f'<div class="mm-section-sub">— 01 / Explorer Mode —</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="mm-section-h">{t("foodie_title")}</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:var(--muted);margin-top:0;">{t("foodie_sub")}</p>', unsafe_allow_html=True)
    st.markdown('<hr class="mm-divider">', unsafe_allow_html=True)

    selected = st.selectbox(t("foodie_select"), BAKU_NAMES, index=0)

    if st.button(t("foodie_btn"), type="primary", use_container_width=True, key="f_go"):
        with st.spinner(t("spin1")):
            st.session_state.foodie_data = run_foodie(selected, api_key)
            st.session_state.foodie_res = selected

    if st.session_state.foodie_res:
        rest = st.session_state.foodie_res
        lang = st.session_state.lang
        st.markdown('<hr class="mm-divider">', unsafe_allow_html=True)
        st.markdown(f'<div class="mm-badge"><span class="dot"></span>NOW VIEWING · <b>{rest}</b></div>', unsafe_allow_html=True)
        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

        if st.session_state.foodie_data:
            st.markdown(st.session_state.foodie_data)
        elif rest in BAKU:
            d = BAKU[rest]
            good_items = "".join(f"<li>{x}</li>" for x in d["good"][lang])
            bad_items = "".join(f"<li>{x}</li>" for x in d["bad"][lang])
            vibe_items = "".join(f"<li>{x}</li>" for x in d["vibe"][lang])
            st.markdown(f'<div class="mm-fcard good r1"><h4>{t("foodie_good")}</h4><ul>{good_items}</ul></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="mm-fcard bad r2"><h4>{t("foodie_bad")}</h4><ul>{bad_items}</ul></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="mm-fcard vibe r3"><h4>{t("foodie_vibe")}</h4><ul>{vibe_items}</ul></div>', unsafe_allow_html=True)

# ─── EXECUTIVE MODULE ──────────────────────────────────────────────────
elif st.session_state.page == "exec":
    back_col, _ = st.columns([2, 8])
    with back_col:
        if st.button(t("back"), key="back_e"):
            st.session_state.page = "landing"
            st.session_state.analysis = None
            st.session_state.campaign = None
            st.rerun()

    if not st.session_state.auth:
        st.markdown(f"""
        <div class="mm-lock">
            <h2>{t('lock_title')}</h2>
            <p>{t('lock_sub')}</p>
            <div class="hint">{t('lock_hint')}</div>
        </div>
        """, unsafe_allow_html=True)
        _, mid, _ = st.columns([1, 2, 1])
        with mid:
            pw = st.text_input(t("pw_label"), type="password", key="pw_in")
            if st.button(t("pw_btn"), type="primary", use_container_width=True, key="pw_go"):
                key = pw.strip().lower()
                if key in RESTAURANT_PWS:
                    st.session_state.auth = True
                    st.session_state.auth_restaurant = RESTAURANT_PWS[key]
                    st.rerun()
                else:
                    st.error(t("pw_err"))
    else:
        rest_name = st.session_state.auth_restaurant or "Paul Azerbaijan"
        head_l, head_r = st.columns([6, 2])
        with head_l:
            st.markdown(f'<div class="mm-section-sub">— 02 / Operator Console —</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="mm-section-h">{t("exec_title")}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="mm-badge"><span class="dot"></span>{t("signed_as")} · <b>{rest_name}</b></div>', unsafe_allow_html=True)
        with head_r:
            st.markdown("<div style='height:36px'></div>", unsafe_allow_html=True)
            if st.button(t("signout"), key="sign_out", type="secondary"):
                st.session_state.auth = False
                st.session_state.auth_restaurant = None
                st.session_state.analysis = None
                st.session_state.campaign = None
                st.rerun()
        st.markdown('<hr class="mm-divider">', unsafe_allow_html=True)

        p = PALETTES[st.session_state.theme]
        stats = RESTAURANT_STATS.get(rest_name, RESTAURANT_STATS["Paul Azerbaijan"])
        # risk color mapping
        risk_palette = {"danger": p["danger"], "accent": p["accent"], "good": "#6FA84B"}
        risk_clr = risk_palette.get(stats["risk_color"], p["accent"])
        # critical % bar tone (low=green, mid=amber, high=red)
        crit_int = int(stats["critical"])
        crit_clr = p["danger"] if crit_int >= 35 else (p["accent"] if crit_int >= 22 else "#6FA84B")
        # localized review count subtext
        rev_word = {"EN": f"{stats['reviews']} recent reviews",
                    "AZ": f"{stats['reviews']} son rəy",
                    "RU": f"{stats['reviews']} отзывов"}[st.session_state.lang]

        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f'<div class="mm-metric r1"><div class="lbl">{t("m1_label")}</div><div class="val">{stats["rating"]}<span style="color:var(--muted);font-size:1.2rem;"> / 5.0</span></div><div class="sub">{rev_word}</div></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="mm-metric r2" style="border-left-color:{crit_clr};"><div class="lbl">{t("m2_label")}</div><div class="val" style="color:{crit_clr};">{stats["critical"]}<span style="font-size:1.4rem;">%</span></div><div class="sub">{t("m2_sub")}</div></div>', unsafe_allow_html=True)
        with m3:
            st.markdown(f'<div class="mm-metric r3" style="border-left-color:{risk_clr};"><div class="lbl">{t("m3_label")}</div><div class="val" style="color:{risk_clr};">{stats["risk"]}</div><div class="sub">{t("m3_sub")}</div></div>', unsafe_allow_html=True)

        st.markdown('<hr class="mm-divider">', unsafe_allow_html=True)
        st.markdown(f"### {t('rev_title')}")
        st.caption(t("rev_cap"))

        default_reviews = BAKU[rest_name]["reviews"][st.session_state.lang]
        reviews_input = st.text_area("rev", value=default_reviews, height=240, label_visibility="collapsed", key=f"rev_{rest_name}")

        st.markdown('<hr class="mm-divider">', unsafe_allow_html=True)
        if st.button(t("btn_analyze"), type="primary", use_container_width=True, key="ex_an"):
            with st.spinner(t("spin1")):
                st.session_state.analysis = run_analysis(reviews_input, api_key, rest_name)
                st.session_state.campaign = None

        if st.session_state.analysis:
            st.markdown('<hr class="mm-divider">', unsafe_allow_html=True)
            st.markdown(f"### {t('analysis_t')}")
            st.markdown(st.session_state.analysis)

            st.markdown('<hr class="mm-divider">', unsafe_allow_html=True)
            if st.button(t("btn_campaign"), type="secondary", use_container_width=True, key="ex_cp"):
                with st.spinner(t("spin2")):
                    st.session_state.campaign = run_campaign(st.session_state.analysis, api_key, rest_name)

            if st.session_state.campaign:
                st.markdown(st.session_state.campaign)

