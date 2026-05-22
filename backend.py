"""OpenAI backend integration and safe demo-mode fallbacks for MenuMind AI."""

import streamlit as st
from openai import OpenAI

from data import MOCK_ANALYSIS, MOCK_CAMPAIGN

OPENAI_MODEL = "gpt-4o-mini"
OPENROUTER_MODEL = "google/gemini-2.0-flash-001"

def _client_and_model(api_key):
    key = api_key.strip()
    if key.startswith("sk-or-"):
        return OpenAI(
            api_key=key,
            base_url="https://openrouter.ai/api/v1",
            default_headers={
                "HTTP-Referer": "http://localhost:8501",
                "X-Title": "MenuMind AI",
            },
        ), OPENROUTER_MODEL
    return OpenAI(api_key=key), OPENAI_MODEL

def call_llm(sys_prompt, user_prompt, api_key):
    if not api_key or not api_key.strip():
        return None
    try:
        client, model = _client_and_model(api_key)
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": sys_prompt},
                      {"role": "user", "content": user_prompt}],
            temperature=0.7, max_tokens=2000,
        )
        return resp.choices[0].message.content
    except Exception as e:
        st.warning(f"⚠️ API error ({type(e).__name__}). Using demo data.")
        return None

LANG_NAMES = {"EN": "English", "AZ": "Azerbaijani", "RU": "Russian"}

def _lang_instruction():
    lang = st.session_state.lang
    if lang == "EN":
        return ""
    return f" IMPORTANT: Respond ENTIRELY in {LANG_NAMES[lang]}."

def run_analysis(reviews, api_key, restaurant_name=""):
    ctx = f" for restaurant '{restaurant_name}' in Baku" if restaurant_name else ""
    r = call_llm(
        "You are a Restaurant Operations Consultant and Financial Analyst. "
        f"Analyze customer reviews{ctx}. "
        "Return a Markdown report with: "
        "1) A table of specific food/dish issues (columns: Dish, Problem, Mentions, Severity) "
        "2) Bullet list of service & operational issues "
        "3) Financial margin risk assessment with a quoted risk level. "
        "Use bold text, emojis, and Markdown tables for structure."
        + _lang_instruction(),
        f"Analyze these customer reviews:\n\n{reviews}", api_key)
    return r if r else MOCK_ANALYSIS[st.session_state.lang]

def run_campaign(analysis, api_key, restaurant_name=""):
    ctx = f" for '{restaurant_name}'" if restaurant_name else ""
    r = call_llm(
        f"You are a premium restaurant Social Media Marketer in Baku, Azerbaijan{ctx}. "
        "Based on the analysis provided, generate: "
        "1) A ready-to-copy Instagram caption with a promo code and call-to-action "
        "2) A strategy table (columns: Element, Detail) covering promo code, duration, target, spend, in-store action "
        "3) Expected impact section with bullet points. "
        "Use Markdown formatting, bold text, emojis, and Baku-specific cultural context."
        + _lang_instruction(),
        f"Generate a win-back campaign based on this analysis:\n\n{analysis}", api_key)
    return r if r else MOCK_CAMPAIGN[st.session_state.lang]

def run_foodie(name, api_key):
    r = call_llm(
        "You are a brutally honest Baku food critic who has eaten at every restaurant in town. "
        "Provide 3 clearly separated sections in Markdown: "
        "## 👍 What to Order (best dishes with specific details), "
        "## 👎 What to Avoid (dishes/items that disappoint and why), "
        "## 💡 Vibe & Tips (atmosphere, best time to visit, insider advice). "
        "Bold dish names, use emojis, be specific with prices in AZN where relevant."
        + _lang_instruction(),
        f"Give your honest, detailed truth about '{name}' restaurant in Baku.", api_key)
    return r

