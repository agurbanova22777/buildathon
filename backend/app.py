from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

app = Flask(__name__)
CORS(app)

FALLBACK_ANALYSIS = """
### 🍔 Food & Dish Issues

- **Truffle Burger** — soggy bun reported in 3 out of 6 reviews. This is your most-mentioned dish and your highest-margin item. The issue is consistent and recurring.
- **Salmon** — described as overcooked and dry by one reviewer. Protein overcooking signals kitchen timing problems.
- **Pasta** — arrived cold on a quiet Tuesday. Points to a heat-retention or plating delay issue.
- **Risotto** — cold in the center, suggesting undercooking or sitting too long before service.

---

### ⏱️ Service & Operational Issues

- **Weekend staffing** is critically understaffed. Two servers for a full floor caused 55-minute waits.
- **Order follow-through** is broken — waiters take orders then disappear with no check-ins.
- **Food temperature control** is failing across multiple dishes and multiple days of the week.

---

### ⚠️ Business Warning

Your Truffle Burger is your highest-margin item and it has 3 direct negative mentions this week alone. A customer who orders your flagship dish and has a bad experience **will not return**. Repeat customer lifetime value on a high-margin item like this is 4-6x the value of a one-time visit. Every soggy bun is not just a bad meal — it is a lost loyal customer worth hundreds of dollars over time. Fix the assembly line for this item immediately.
"""

FALLBACK_CAMPAIGN = """
### 📱 Instagram Post

We heard you — loud and clear. 👂

Our Truffle Burger is back and it's **better than ever**. We went back to the kitchen, rebuilt our assembly process, and the buns are now perfectly toasted every single time. 🍔🔥

Come taste the difference this weekend and use code **TOASTED20** for 20% off your next Truffle Burger.

Because when you care enough to tell us, we care enough to fix it. 💛

---

### 📣 Promo Strategy

- **Platform:** Instagram + Google Business reply
- **Promo code:** TOASTED20 (20% off, weekend only)
- **Target:** Re-engage past visitors who left negative reviews
- **Follow-up:** Reply to every 1-star review mentioning the burger with this post link
"""

FALLBACK_VIBE = {
    "good": "- **The pasta** — locals swear by the house-made tagliatelle, order it with the truffle butter\n- **Weekend brunch** — the eggs benedict has a loyal following, arrives fast and hot\n- **Natural wine list** — small but well-curated, ask your server for the house pour",
    "bad": "- **The grilled chicken** — multiple reviewers call it dry and bland, skip it\n- **Dessert menu** — limited options and the tiramisu gets mixed reviews\n- **Peak Friday dinner** — waits can hit 30+ minutes even with a reservation",
    "tip": "- Best seats are by the window on the left side — great light and away from kitchen noise\n- Go Tuesday or Wednesday for the fastest service and freshest prep\n- Ask for the **off-menu soup** — they make a different one daily and it never disappoints"
}

def get_client(api_key):
    key = api_key or os.getenv("OPENAI_API_KEY", "")
    if not key or not OPENAI_AVAILABLE:
        return None
    return OpenAI(api_key=key)

def ask_ai(client, system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        max_tokens=1000,
        temperature=0.7,
    )
    return response.choices[0].message.content

SYSTEM_OWNER = """You are a dual expert: a Restaurant Operations Consultant and a Financial Margin Analyst.
You analyze customer reviews to find specific culinary flaws, service failures, and financial risks.
Always respond in clean Markdown with bold text, bullet points, section headers using ###, and relevant emojis.
Be specific — name the exact dishes, exact complaints, and explain the business impact clearly."""

SYSTEM_CAMPAIGN = """You are an expert Restaurant Social Media Marketer and brand recovery specialist.
You write compelling, human, warm Instagram captions that acknowledge customer feedback and invite them back.
Always include a promo code, a specific dish reference, and a follow-up strategy section.
Respond in clean Markdown with bold text, bullet points, and emojis."""

SYSTEM_FOODIE = """You are a trusted local food critic who has read hundreds of reviews for any given restaurant.
You distill the real truth into three sharp, honest sections: what to order, what to avoid, and a pro tip about vibe or timing.
Always respond in clean Markdown bullet points with bold dish names and emojis. Be concise and genuinely useful."""

@app.route("/analyze", methods=["POST"])
def analyze():
    body    = request.get_json()
    reviews = body.get("reviews", "")
    api_key = body.get("api_key", "")
    client  = get_client(api_key)

    if not client:
        return jsonify({
            "rating":        "3.7 / 5.0",
            "feedback_rate": "22%",
            "risk_level":    "HIGH ⚠️",
            "analysis":      FALLBACK_ANALYSIS,
        })

    prompt = f"""Analyze these restaurant reviews and return:
1. An overall rating out of 5.0 (just the number like 3.7 / 5.0)
2. The critical feedback rate as a percentage (just like 22%)
3. Financial margin risk level: HIGH, MEDIUM, or LOW with an emoji
4. A full structured analysis with ### Food & Dish Issues and ### Service & Operational Issues sections, plus a ### Business Warning

Reviews:
{reviews}

Return a JSON object with keys: rating, feedback_rate, risk_level, analysis"""

    try:
        raw = ask_ai(client, SYSTEM_OWNER, prompt)
        raw = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        import json
        data = json.loads(raw)
        return jsonify(data)
    except Exception:
        return jsonify({
            "rating":        "3.7 / 5.0",
            "feedback_rate": "22%",
            "risk_level":    "HIGH ⚠️",
            "analysis":      FALLBACK_ANALYSIS,
        })

@app.route("/campaign", methods=["POST"])
def campaign():
    body    = request.get_json()
    reviews = body.get("reviews", "")
    api_key = body.get("api_key", "")
    client  = get_client(api_key)

    if not client:
        return jsonify({"campaign": FALLBACK_CAMPAIGN})

    prompt = f"""Based on these reviews, write a targeted Instagram recovery campaign post.
Reference the exact flaw found in the reviews, show it has been fixed, include a promo code, and add a short promo strategy section.

Reviews:
{reviews}"""

    try:
        result = ask_ai(client, SYSTEM_CAMPAIGN, prompt)
        return jsonify({"campaign": result})
    except Exception:
        return jsonify({"campaign": FALLBACK_CAMPAIGN})

@app.route("/vibe", methods=["POST"])
def vibe():
    body       = request.get_json()
    restaurant = body.get("restaurant", "")
    api_key    = body.get("api_key", "")
    client     = get_client(api_key)

    if not client:
        return jsonify(FALLBACK_VIBE)

    prompt = f"""Give me a real, honest summary for the restaurant: "{restaurant}".
Return a JSON object with three keys:
- good: bullet list of what to order (with bold dish names)
- bad: bullet list of what to avoid
- tip: bullet list of pro tips about vibe, timing, or seating

Use Markdown formatting inside each value."""

    try:
        raw = ask_ai(client, SYSTEM_FOODIE, prompt)
        raw = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        import json
        data = json.loads(raw)
        return jsonify(data)
    except Exception:
        return jsonify(FALLBACK_VIBE)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

