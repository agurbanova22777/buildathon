# MenuMind AI

**MenuMind AI** is a multilingual Streamlit dashboard for Baku restaurant intelligence. It turns raw customer reviews into clear operational insights, margin-risk analysis, and AI-generated customer recovery campaigns.

The app is designed for two audiences:

- **Foodies:** discover what to order, what to avoid, and the real vibe at Baku restaurants.
- **Restaurant managers:** analyze review streams, identify flaws, and generate win-back campaigns.

The current interface is built as a polished Streamlit presentation layer with custom styling, dark/light themes, Azerbaijani/Russian/English localization, per-restaurant manager access, and a safe dual-mode backend.

---

## Core Features

### Multilingual dashboard

MenuMind AI supports:

- **English**
- **Azerbaijani**
- **Russian**

The interface, demo data, analysis prompts, and campaign outputs are language-aware.

### Foodie Explorer

The public-facing explorer helps users understand Baku restaurants through:

- **What to order**
- **What to avoid**
- **Vibe and service tips**

When an API key is provided, the foodie insights can be generated live. Without a key, the app uses curated local Baku demo data.

### Management Portal

The management area is protected with per-restaurant demo keys. Each key opens a restaurant-specific dashboard with relevant KPIs and review feed data.

Demo manager keys:

| Restaurant | Key |
|---|---|
| Paul Azerbaijan | `paul2026` |
| Chinar | `chinar88` |
| Entrée | `entree77` |

The portal includes:

- Restaurant-specific sign-in
- Rating snapshot
- Critical feedback percentage
- Margin risk tier
- Editable review stream
- AI flaw analysis
- AI customer recovery campaign generation

### Dual-mode backend

MenuMind AI works in two modes.

#### 1. Live API mode

If the user enters an API key in the top navigation bar, the app sends the current review feed to a live LLM backend.

The live backend supports OpenRouter keys and routes them through OpenRouter's OpenAI-compatible API endpoint. The OpenRouter path is configured to use a cutting-edge Gemini model:

```text
google/gemini-2.0-flash-001
```

This powers dynamic analysis and campaign generation in the selected language.

#### 2. Local Baku demo fallback

If the API key field is blank, invalid, or the API call fails, the app automatically falls back to pre-written local demo data.

This means the dashboard remains fully usable for presentations, hackathons, offline demos, and judging sessions without requiring a live API connection.

Fallback data currently includes curated Baku restaurant content for restaurants such as:

- Paul Azerbaijan
- Chinar
- Entrée

---

## Project Structure

```text
buildathon/
├── app.py             # Streamlit entrypoint and presentation UI
├── backend.py         # OpenRouter/OpenAI-compatible backend calls and fallback logic
├── data.py            # Translations, restaurant data, demo reviews, KPIs, mock outputs
├── frontend.py        # Theme palettes and custom CSS
├── requirements.txt   # Python dependencies
├── .gitignore         # Python/project ignore rules
└── README.md          # Project documentation
```

### `app.py`

Main Streamlit application file.

Contains:

- Page config
- Session state
- Navbar
- Language/theme controls
- Landing page
- Foodie Explorer UI
- Management Portal UI
- Calls into `backend.py`, `data.py`, and `frontend.py`

### `backend.py`

Backend integration layer.

Contains:

- OpenAI-compatible client setup
- OpenRouter key detection
- Gemini model routing through OpenRouter
- Analysis generation
- Campaign generation
- Foodie insight generation
- Safe fallback to local demo content

### `data.py`

Static product/data layer.

Contains:

- Translation matrix
- Restaurant names
- Demo manager passwords
- Restaurant KPI snapshots
- Baku review feeds
- Mock analysis reports
- Mock recovery campaigns

### `frontend.py`

Presentation styling layer.

Contains:

- Dark/light theme palettes
- Custom CSS
- Typography
- Cards
- Metrics
- Inputs
- Buttons
- Streamlit styling overrides

---

## Installation

### 1. Clone or open the project

```powershell
cd path\to\buildathon
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

The project currently requires:

```text
streamlit>=1.32.0
openai>=1.12.0
```

---

## Running the App

```powershell
streamlit run app.py
```

Then open the local Streamlit URL, usually:

```text
http://localhost:8501
```

---

## Using Live API Mode

1. Get an OpenRouter API key from:

```text
https://openrouter.ai/keys
```

2. Run the app.

3. Paste the key into the **OpenAI Key** field in the top bar.

4. Open **Management Portal**.

5. Sign in with a restaurant key, for example:

```text
paul2026
```

6. Click **Run Flaw & Margin Analysis**.

7. Click **Generate Win-Back Campaign**.

If the key is valid and the OpenRouter account has access to the configured Gemini model, the output will be generated live.

---

## Using Demo Fallback Mode

To use the app without any API key:

1. Leave the API key field blank.
2. Open the Management Portal.
3. Sign in with a demo restaurant key.
4. Run the analysis and campaign buttons.

The app will automatically use the local Baku fallback data.

This is ideal for:

- Live presentations
- Offline demos
- Hackathon judging
- Development without API credits
- Safe product walkthroughs

---

## Language Behavior

When switching languages, the app clears previously generated outputs so stale English analysis does not remain visible after selecting Azerbaijani or Russian.

To generate live content in the new language:

1. Select the desired language.
2. Run the analysis again.
3. Generate the campaign again.

The backend prompt instructs the model to respond entirely in the selected language.

---

## Backend Notes

The backend uses the `openai` Python SDK because OpenRouter exposes an OpenAI-compatible API.

For OpenRouter keys beginning with:

```text
sk-or-
```

`backend.py` routes requests to:

```text
https://openrouter.ai/api/v1
```

For standard OpenAI keys, the client can still use the normal OpenAI endpoint.

If any API call fails, the app does not crash. It displays a warning and falls back to local demo data.

---

## Security Notes

Do not hardcode API keys in the codebase.

Recommended practices:

- Paste keys only into the app during local testing.
- Do not commit `.env` files.
- Do not commit `.streamlit/secrets.toml`.
- Rotate keys if they are accidentally exposed.

The included `.gitignore` excludes common secret, environment, cache, and build files.

---

## Quick Verification

Compile all modules:

```powershell
python -m py_compile app.py backend.py data.py frontend.py
```

Run the app:

```powershell
streamlit run app.py
```

Test both modes:

- **Blank key:** local demo fallback should work.
- **OpenRouter key:** live Gemini-powered analysis should work.

---

## Product Vision

MenuMind AI helps restaurants move from passive review reading to active recovery strategy.

Instead of simply collecting complaints, the dashboard transforms customer feedback into:

- Specific kitchen fixes
- Service quality signals
- Margin risk warnings
- Localized win-back campaigns
- Restaurant-specific intelligence

It is built to be presentation-ready, demo-safe, multilingual, and practical for real restaurant operators in Baku.
