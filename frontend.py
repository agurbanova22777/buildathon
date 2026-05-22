"""Frontend theme palettes and CSS for the Streamlit presentation layer."""

# ═══════════════════════════════════════════════════════════════════════
# THEME PALETTES & CSS
# ═══════════════════════════════════════════════════════════════════════
PALETTES = {
    "dark":  {"bg": "#0B1416", "bg2": "#13202A", "card": "#13202A",
              "text": "#F2EBDD", "muted": "#8AA0A6",
              "accent": "#E8B14B", "accent2": "#C73E3A", "ink": "#0B1416",
              "border": "rgba(232,177,75,0.18)", "danger": "#C73E3A",
              "input_bg": "#0F1A20", "popover_bg": "#13202A"},
    "light": {"bg": "#F4EFE6", "bg2": "#FBF7EF", "card": "#FFFFFF",
              "text": "#0F1B1F", "muted": "#6B7574",
              "accent": "#A0651A", "accent2": "#9B2C2C", "ink": "#0F1B1F",
              "border": "rgba(15,27,31,0.12)", "danger": "#9B2C2C",
              "input_bg": "#FFFFFF", "popover_bg": "#FFFFFF"},
}

def get_css(th):
    p = PALETTES[th]
    grain_op = "0.04" if th == "dark" else "0.06"
    good_tint = "rgba(139,178,108,0.10)" if th == "dark" else "rgba(94,124,67,0.08)"
    bad_tint  = "rgba(199,62,58,0.12)"  if th == "dark" else "rgba(155,44,44,0.06)"
    vibe_tint = "rgba(232,177,75,0.10)" if th == "dark" else "rgba(160,101,26,0.08)"
    good_bar = "#8BB26C"; bad_bar = p['accent2']; vibe_bar = p['accent']
    return f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,800;0,9..144,900;1,9..144,400;1,9..144,700&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');
:root {{
  --bg: {p['bg']}; --bg2: {p['bg2']}; --card: {p['card']};
  --text: {p['text']}; --muted: {p['muted']};
  --accent: {p['accent']}; --accent2: {p['accent2']};
  --border: {p['border']}; --danger: {p['danger']};
  --input-bg: {p['input_bg']}; --popover-bg: {p['popover_bg']};
  --serif: 'Fraunces', 'Times New Roman', serif;
  --sans: 'Manrope', system-ui, sans-serif;
  --mono: 'JetBrains Mono', 'Courier New', monospace;
}}

/* Hide Streamlit chrome */
[data-testid="stSidebar"], #MainMenu, header, footer,
[data-testid="stToolbar"], .stDeployButton, [data-testid="stHeader"] {{ display: none !important; }}

/* Layered atmospheric background */
.stApp {{
  background:
    radial-gradient(ellipse 80% 60% at 15% 0%, {p['accent']}18 0%, transparent 50%),
    radial-gradient(ellipse 70% 50% at 85% 100%, {p['accent2']}15 0%, transparent 55%),
    linear-gradient(180deg, var(--bg) 0%, var(--bg2) 100%) !important;
  background-attachment: fixed !important;
  color: var(--text) !important;
  font-family: var(--sans) !important;
}}
.stApp::before {{
  content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 0;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='80' height='80'><path d='M40 0L80 40L40 80L0 40Z' fill='none' stroke='%23{p['accent'].lstrip('#')}' stroke-width='0.4' opacity='0.18'/></svg>");
  opacity: {grain_op};
}}
.block-container {{ padding-top: 1.2rem !important; max-width: 1180px; position: relative; z-index: 1; }}

/* Typography */
body, p, li, span, label, div {{ font-family: var(--sans); color: var(--text); }}
h1, h2, h3, h4 {{ font-family: var(--serif); color: var(--text); letter-spacing: -0.01em; font-weight: 600; }}
h1 {{ font-weight: 800; }}
code, pre, .mono {{ font-family: var(--mono) !important; }}

/* Navbar */
.mm-brand {{
  font-family: var(--serif); font-size: 1.55rem; font-weight: 800;
  letter-spacing: -0.02em; color: var(--text);
  padding-top: 4px; display: flex; align-items: center; gap: 6px;
}}
.mm-brand .dot {{ width: 7px; height: 7px; border-radius: 50%;
  background: var(--accent); box-shadow: 0 0 12px var(--accent); animation: pulse 2.4s ease-in-out infinite; }}
@keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0.45; }} }}

/* Hero */
.mm-hero {{ text-align: center; padding: 72px 20px 28px; animation: rise 0.7s ease-out; }}
.mm-eyebrow {{
  font-family: var(--mono); font-size: 0.72rem; letter-spacing: 0.25em;
  text-transform: uppercase; color: var(--accent) !important;
  margin-bottom: 18px; opacity: 0; animation: rise 0.6s ease-out 0.05s forwards;
}}
.mm-hero h1 {{
  font-family: var(--serif); font-size: 4.2rem; font-weight: 900;
  line-height: 1.02; letter-spacing: -0.035em; margin: 0 auto 22px;
  max-width: 900px; opacity: 0; animation: rise 0.7s ease-out 0.15s forwards;
}}
.mm-hero h1 em {{
  font-style: italic; font-weight: 400; color: var(--accent) !important;
  font-feature-settings: "ss01";
}}
.mm-hero .sub {{
  font-size: 1.15rem; line-height: 1.55; color: var(--muted) !important;
  max-width: 620px; margin: 0 auto; opacity: 0;
  animation: rise 0.7s ease-out 0.3s forwards;
}}
@keyframes rise {{ from {{ opacity: 0; transform: translateY(16px); }} to {{ opacity: 1; transform: translateY(0); }} }}

/* Landing cards */
.mm-card {{
  background: var(--card); border: 1px solid var(--border);
  border-radius: 4px; padding: 38px 32px;
  position: relative; overflow: hidden;
  transition: transform 0.35s cubic-bezier(.2,.7,.3,1), border-color 0.3s;
  opacity: 0; animation: rise 0.7s ease-out 0.45s forwards;
}}
.mm-card::before {{
  content: ""; position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
  transform: scaleX(0); transform-origin: left; transition: transform 0.4s ease;
}}
.mm-card:hover {{ transform: translateY(-6px); border-color: var(--accent); }}
.mm-card:hover::before {{ transform: scaleX(1); }}
.mm-card .num {{
  font-family: var(--mono); font-size: 0.7rem; color: var(--muted);
  letter-spacing: 0.2em; margin-bottom: 16px;
}}
.mm-card h3 {{ font-family: var(--serif); font-size: 1.7rem; font-weight: 700; margin-bottom: 12px; letter-spacing: -0.015em; }}
.mm-card p {{ color: var(--muted) !important; font-size: 0.96rem; line-height: 1.6; margin-bottom: 0; }}

/* Metric cards */
.mm-metric {{
  background: var(--card); border: 1px solid var(--border);
  border-radius: 4px; padding: 24px 22px; position: relative;
  border-left: 3px solid var(--accent);
}}
.mm-metric .lbl {{
  font-family: var(--mono); font-size: 0.66rem; font-weight: 500;
  text-transform: uppercase; letter-spacing: 0.18em;
  color: var(--muted) !important; margin-bottom: 10px;
}}
.mm-metric .val {{ font-family: var(--serif); font-size: 2.4rem; font-weight: 700; line-height: 1; letter-spacing: -0.02em; }}
.mm-metric .sub {{ font-size: 0.78rem; color: var(--muted) !important; margin-top: 8px; font-family: var(--sans); }}

/* Foodie insight cards */
.mm-fcard {{
  border-radius: 4px; padding: 24px 28px; margin-bottom: 14px;
  background: var(--card); border: 1px solid var(--border); position: relative;
  border-left: 3px solid var(--accent);
}}
.mm-fcard.good {{ background: linear-gradient(95deg, {good_tint}, transparent 60%), var(--card); border-left-color: {good_bar}; }}
.mm-fcard.bad  {{ background: linear-gradient(95deg, {bad_tint},  transparent 60%), var(--card); border-left-color: {bad_bar}; }}
.mm-fcard.vibe {{ background: linear-gradient(95deg, {vibe_tint}, transparent 60%), var(--card); border-left-color: {vibe_bar}; }}
.mm-fcard h4 {{ font-family: var(--serif); font-size: 1.15rem; margin: 0 0 14px; font-weight: 700; }}
.mm-fcard ul {{ margin: 0; padding-left: 18px; }}
.mm-fcard li {{ margin-bottom: 8px; line-height: 1.55; color: var(--text); }}

/* Restaurant badge (on exec page) */
.mm-badge {{
  display: inline-flex; align-items: center; gap: 10px;
  background: var(--card); border: 1px solid var(--border);
  padding: 8px 16px; border-radius: 999px; font-family: var(--mono);
  font-size: 0.78rem; letter-spacing: 0.05em;
}}
.mm-badge .dot {{ width: 6px; height: 6px; border-radius: 50%; background: var(--accent); }}
.mm-badge b {{ font-family: var(--serif); font-weight: 700; font-style: italic; color: var(--accent) !important; font-size: 1rem; }}

/* Lock screen */
.mm-lock {{
  max-width: 480px; margin: 40px auto 12px; text-align: center;
  background: var(--card); border: 1px solid var(--border);
  border-radius: 4px; padding: 48px 40px 36px;
  position: relative; overflow: hidden;
}}
.mm-lock::before {{
  content: ""; position: absolute; top: 0; left: 50%; transform: translateX(-50%);
  width: 60px; height: 3px; background: var(--accent);
}}
.mm-lock h2 {{ font-family: var(--serif); font-size: 1.9rem; font-weight: 700; margin: 10px 0 12px; }}
.mm-lock p {{ color: var(--muted) !important; font-size: 0.92rem; line-height: 1.55; }}
.mm-lock .hint {{ font-family: var(--mono); font-size: 0.75rem; color: var(--accent) !important; margin-top: 14px; letter-spacing: 0.04em; }}

.mm-divider {{ border: none; border-top: 1px solid var(--border); margin: 28px 0; }}

/* Form controls */
.stTextInput input, .stTextArea textarea {{
  background-color: var(--input-bg) !important; color: var(--text) !important;
  border: 1px solid var(--border) !important; border-radius: 4px !important;
  font-family: var(--sans) !important; font-size: 0.95rem !important;
}}
.stTextInput input::placeholder, .stTextArea textarea::placeholder {{
  color: var(--muted) !important; opacity: 0.7 !important;
}}
.stTextInput input:focus, .stTextArea textarea:focus {{
  border-color: var(--accent) !important; box-shadow: 0 0 0 2px {p['accent']}33 !important;
}}

/* Selectbox (closed state) */
.stSelectbox div[data-baseweb="select"],
.stSelectbox div[data-baseweb="select"] > div,
.stSelectbox div[data-baseweb="select"] * {{
  cursor: pointer !important;
}}
.stSelectbox div[data-baseweb="select"] > div {{
  background-color: var(--input-bg) !important; color: var(--text) !important;
  border: 1px solid var(--border) !important; border-radius: 4px !important;
  font-family: var(--sans) !important;
}}
.stSelectbox div[data-baseweb="select"] svg {{ color: var(--text) !important; fill: var(--text) !important; }}
li[role="option"], ul[role="listbox"] li {{ cursor: pointer !important; }}

/* Selectbox dropdown POPOVER (the open menu) — critical fix for light mode */
div[data-baseweb="popover"] {{ background: transparent !important; }}
ul[role="listbox"], div[data-baseweb="menu"], div[data-baseweb="popover"] ul {{
  background-color: var(--popover-bg) !important;
  border: 1px solid var(--border) !important;
  border-radius: 4px !important;
  box-shadow: 0 12px 32px rgba(0,0,0,0.25) !important;
}}
li[role="option"], ul[role="listbox"] li, div[data-baseweb="menu"] li {{
  background-color: var(--popover-bg) !important;
  color: var(--text) !important;
  font-family: var(--sans) !important;
}}
li[role="option"]:hover, ul[role="listbox"] li:hover, li[aria-selected="true"] {{
  background-color: {p['accent']}22 !important;
  color: var(--text) !important;
}}

/* Buttons */
.stButton > button {{
  border-radius: 4px !important; font-family: var(--sans) !important;
  font-weight: 600 !important; letter-spacing: 0.02em !important;
  padding: 10px 22px !important; transition: all 0.25s ease !important;
}}
.stButton > button[kind="primary"],
.stButton > button[kind="primary"] p,
.stButton > button[kind="primary"] div,
.stButton > button[kind="primary"] span {{
  background: var(--accent) !important; color: {p['ink']} !important;
  border-color: var(--accent) !important;
}}
.stButton > button[kind="primary"] {{
  border: 1px solid var(--accent) !important;
  box-shadow: 0 4px 14px {p['accent']}33 !important;
}}
.stButton > button[kind="primary"]:hover,
.stButton > button[kind="primary"]:hover p,
.stButton > button[kind="primary"]:hover div,
.stButton > button[kind="primary"]:hover span {{
  background: {p['ink']} !important; color: var(--accent) !important;
  border-color: var(--accent) !important;
}}
.stButton > button[kind="primary"]:hover {{ transform: translateY(-1px); }}
.stButton > button[kind="secondary"],
.stButton > button[kind="secondary"] p,
.stButton > button[kind="secondary"] div,
.stButton > button[kind="secondary"] span {{
  background: transparent !important; color: var(--text) !important;
}}
.stButton > button[kind="secondary"] {{ border: 1px solid var(--border) !important; }}
.stButton > button[kind="secondary"]:hover,
.stButton > button[kind="secondary"]:hover p,
.stButton > button[kind="secondary"]:hover div,
.stButton > button[kind="secondary"]:hover span {{
  border-color: var(--accent) !important; color: var(--accent) !important;
}}

/* Hide "Press Enter to apply" instructions that overlap the password eye icon */
[data-testid="InputInstructions"],
.stTextInput div[data-baseweb="input"] + div,
div[class*="InputInstructions"] {{
  display: none !important;
}}

/* Markdown tables */
.stMarkdown table {{ border-collapse: collapse; font-family: var(--sans); margin: 14px 0; }}
.stMarkdown th {{
  background: {p['accent']}18; color: var(--text) !important;
  font-family: var(--mono); font-size: 0.78rem; text-transform: uppercase;
  letter-spacing: 0.08em; padding: 10px 14px; text-align: left;
  border-bottom: 2px solid var(--accent);
}}
.stMarkdown td {{ padding: 10px 14px; border-bottom: 1px solid var(--border); color: var(--text) !important; }}
.stMarkdown blockquote {{
  border-left: 3px solid var(--accent); padding: 6px 0 6px 18px;
  margin: 14px 0; color: var(--muted) !important; font-style: italic;
  font-family: var(--serif); font-size: 1.05rem;
}}

/* Section heading on subpages */
.mm-section-h {{
  font-family: var(--serif); font-size: 2.2rem; font-weight: 700;
  letter-spacing: -0.02em; margin: 8px 0 4px;
}}
.mm-section-sub {{
  font-family: var(--mono); font-size: 0.78rem; letter-spacing: 0.18em;
  text-transform: uppercase; color: var(--accent) !important; margin-bottom: 18px;
}}

/* Stagger reveal helper */
.r1 {{ animation: rise 0.6s ease-out 0.1s both; }}
.r2 {{ animation: rise 0.6s ease-out 0.25s both; }}
.r3 {{ animation: rise 0.6s ease-out 0.4s both; }}
</style>
"""

