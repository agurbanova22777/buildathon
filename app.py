"""
MenuMind AI - Next-Generation Restaurant Intelligence Platform
Bespoke UI | No Sidebar | Full EN/AZ/RU | Theme Engine | Password-gated B2B
"""
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="MenuMind AI", page_icon="🍽️", layout="wide")

for k, v in {"page": "landing", "lang": "EN", "theme": "dark", "auth": False,
             "auth_restaurant": None,
             "analysis": None, "campaign": None, "foodie_res": None, "foodie_data": None}.items():
    if k not in st.session_state:
        st.session_state[k] = v

EXEC_PW = "baku2026"  # legacy/demo master password (maps to Paul Azerbaijan)

# Per-restaurant manager passwords (each restaurant has its own credential)
RESTAURANT_PWS = {
    "paul2026":  "Paul Azerbaijan",
    "chinar88":  "Chinar",
    "entree77":  "Entrée",
    "baku2026":  "Paul Azerbaijan",  # demo fallback
}

# Per-restaurant KPI snapshot (rating / critical-feedback % / margin risk tier)
RESTAURANT_STATS = {
    "Paul Azerbaijan": {"rating": "3.1", "reviews": 8,  "critical": "42", "risk": "HIGH",   "risk_color": "danger"},
    "Chinar":          {"rating": "4.4", "reviews": 12, "critical": "16", "risk": "LOW",    "risk_color": "good"},
    "Entrée":          {"rating": "3.8", "reviews": 11, "critical": "27", "risk": "MEDIUM", "risk_color": "accent"},
}

# ═══════════════════════════════════════════════════════════════════════
# FULL TRANSLATION MATRIX — every user-visible string
# ═══════════════════════════════════════════════════════════════════════
T = {
"brand":       {"EN": "🍽️ MenuMind AI", "AZ": "🍽️ MenuMind AI", "RU": "🍽️ MenuMind AI"},
"back":        {"EN": "← Back to Home", "AZ": "← Ana Səhifəyə Qayıt", "RU": "← На Главную"},
"api_label":   {"EN": "OpenAI Key (optional)", "AZ": "OpenAI Açarı (istəyə bağlı)", "RU": "Ключ OpenAI (опционально)"},
"hero_title":  {"EN": "Next-Generation Restaurant Intelligence",
                "AZ": "Yeni Nəsil Restoran Kəşfiyyatı",
                "RU": "Ресторанная Аналитика Нового Поколения"},
"hero_sub":    {"EN": "Transform raw reviews into actionable kitchen fixes, margin protection, and loyalty-winning campaigns — powered by AI.",
                "AZ": "Müştəri rəylərini mətbəx təkmilləşdirmələrinə, marja qorunmasına və loyallıq kampaniyalarına çevirin — süni intellekt ilə.",
                "RU": "Превращайте отзывы в улучшения кухни, защиту маржи и кампании лояльности — с помощью ИИ."},
"card_foodie_t": {"EN": "🔍  Explorer Mode", "AZ": "🔍  Kəşfiyyatçı Rejimi", "RU": "🔍  Режим Исследователя"},
"card_foodie_d": {"EN": "Discover what to order, what to skip, and the real vibe at Baku's top restaurants.",
                  "AZ": "Bakının ən yaxşı restoranlarında nə sifariş etməli, nədən qaçınmalı və atmosferi kəşf edin.",
                  "RU": "Узнайте, что заказать, чего избегать и какая атмосфера в лучших ресторанах Баку."},
"card_exec_t": {"EN": "📊  Management Portal", "AZ": "📊  Rəhbərlik Portalı", "RU": "📊  Портал Руководителя"},
"card_exec_d": {"EN": "Analyze feedback, map margin risks, and generate AI-powered recovery campaigns.",
                "AZ": "Rəyləri analiz edin, marja risklərini müəyyən edin və AI ilə bərpa kampaniyaları yaradın.",
                "RU": "Анализируйте отзывы, выявляйте риски маржи и создавайте AI-кампании по возврату."},
"foodie_title":  {"EN": "Smart Restaurant Explorer", "AZ": "Ağıllı Restoran Kəşfiyyatçısı", "RU": "Умный Ресторанный Навигатор"},
"foodie_sub":    {"EN": "Get the real truth behind the reviews — instantly.",
                  "AZ": "Rəylərin arxasındakı həqiqəti dərhal öyrənin.",
                  "RU": "Узнайте правду за отзывами — мгновенно."},
"foodie_select": {"EN": "Choose a restaurant", "AZ": "Restoran seçin", "RU": "Выберите ресторан"},
"foodie_btn":    {"EN": "✨ Analyze Reviews", "AZ": "✨ Rəyləri Analiz Et", "RU": "✨ Анализировать"},
"foodie_good":   {"EN": "👍 What to Order", "AZ": "👍 Nə Sifariş Etməli", "RU": "👍 Что заказать"},
"foodie_bad":    {"EN": "👎 What to Avoid", "AZ": "👎 Nədən Qaçınmalı", "RU": "👎 Чего избегать"},
"foodie_vibe":   {"EN": "💡 Vibe & Service", "AZ": "💡 Atmosfer və Xidmət", "RU": "💡 Атмосфера и Сервис"},
"lock_title":  {"EN": "Manager Sign-In", "AZ": "Menecer Girişi", "RU": "Вход Менеджера"},
"lock_sub":    {"EN": "Each restaurant has its own access credential. Sign in with your venue's manager key.",
                "AZ": "Hər restoranın öz giriş açarı var. Məkanınızın menecer açarı ilə daxil olun.",
                "RU": "У каждого ресторана свой ключ доступа. Войдите с ключом менеджера вашего заведения."},
"lock_hint":   {"EN": "Demo keys: paul2026 · chinar88 · entree77",
                "AZ": "Demo açarlar: paul2026 · chinar88 · entree77",
                "RU": "Демо-ключи: paul2026 · chinar88 · entree77"},
"pw_label":    {"EN": "Manager key", "AZ": "Menecer açarı", "RU": "Ключ менеджера"},
"pw_btn":      {"EN": "Sign In", "AZ": "Daxil Ol", "RU": "Войти"},
"pw_err":      {"EN": "Unrecognized key. Each restaurant has a unique credential.",
                "AZ": "Açar tanınmadı. Hər restoranın unikal açarı var.",
                "RU": "Ключ не распознан. У каждого ресторана уникальный ключ."},
"signed_as":   {"EN": "Signed in as", "AZ": "Daxil olduğunuz hesab", "RU": "Вход выполнен как"},
"signout":     {"EN": "Sign out", "AZ": "Çıxış", "RU": "Выйти"},
"exec_title":  {"EN": "Business Performance & Margin Optimization",
                "AZ": "Biznes Performans və Marja Optimallaşdırması",
                "RU": "Бизнес-Аналитика и Оптимизация Маржи"},
"m1_label":    {"EN": "Overall Rating", "AZ": "Ümumi Reytinq", "RU": "Общий Рейтинг"},
"m1_sub":      {"EN": "8 recent reviews", "AZ": "8 son rəy", "RU": "8 отзывов"},
"m2_label":    {"EN": "Critical Feedback", "AZ": "Kritik Rəylər", "RU": "Критические Отзывы"},
"m2_sub":      {"EN": "Threshold exceeded", "AZ": "Hədd aşılıb", "RU": "Порог превышен"},
"m3_label":    {"EN": "Margin Risk", "AZ": "Marja Riski", "RU": "Риск Маржи"},
"m3_sub":      {"EN": "Premium items under-performing", "AZ": "Premium məhsullar zəif çıxış edir", "RU": "Премиальные позиции не оправдывают"},
"rev_title":   {"EN": "📝 Customer Reviews", "AZ": "📝 Müştəri Rəyləri", "RU": "📝 Отзывы Клиентов"},
"rev_cap":     {"EN": "Paste reviews or use pre-loaded Baku data.", "AZ": "Rəyləri yapışdırın və ya hazır Bakı datasetindən istifadə edin.", "RU": "Вставьте отзывы или используйте датасет Баку."},
"btn_analyze": {"EN": "🔍 Run Flaw & Margin Analysis", "AZ": "🔍 Qüsur və Marja Analizi", "RU": "🔍 Анализ Дефектов и Маржи"},
"btn_campaign":{"EN": "🚀 Generate Win-Back Campaign", "AZ": "🚀 Geri Qazanma Kampaniyası", "RU": "🚀 Генерация Кампании Возврата"},
"analysis_t":  {"EN": "📋 Analysis Results", "AZ": "📋 Analiz Nəticələri", "RU": "📋 Результаты Анализа"},
"spin1":       {"EN": "Analyzing...", "AZ": "Analiz edilir...", "RU": "Анализируем..."},
"spin2":       {"EN": "Generating...", "AZ": "Hazırlanır...", "RU": "Генерируем..."},
"td":          {"EN": "Dark", "AZ": "Qaranlıq", "RU": "Тёмная"},
"tl":          {"EN": "Light", "AZ": "İşıqlı", "RU": "Светлая"},
"footer":      {"EN": "Built in Baku · Powered by GPT-4o-mini", "AZ": "Bakıda hazırlanıb · GPT-4o-mini", "RU": "Сделано в Баку · GPT-4o-mini"},
}

def t(k):
    e = T.get(k, {})
    return e.get(st.session_state.lang, e.get("EN", k))

# ═══════════════════════════════════════════════════════════════════════
# BAKU RESTAURANT DATA — fully translated
# ═══════════════════════════════════════════════════════════════════════
BAKU_NAMES = ["Paul Azerbaijan", "Chinar", "Entrée"]

BAKU = {
"Paul Azerbaijan": {
  "good": {
    "EN": ["Croissants & pastries — consistently flaky, buttery, best in Baku",
            "Eggs Benedict with smoked salmon — perfectly poached, rich hollandaise",
            "Tarte Tatin — caramelized apple perfection, a must-try dessert",
            "Coffee quality — strong French press, great for slow mornings"],
    "AZ": ["Kruassanlar və şirniyyatlar — həmişə təzə, kərəyağlı, Bakının ən yaxşısı",
            "Yumurta Benedikt hisə verilmiş qızılbalıqla — mükəmməl bişirilmiş",
            "Tarte Tatin — karamelli alma mükəmməlliyi, mütləq sınayın",
            "Kofe keyfiyyəti — güclü French press, sakit səhərlər üçün ideal"],
    "RU": ["Круассаны и выпечка — неизменно слоистые, маслянистые, лучшие в Баку",
            "Яйца Бенедикт с копчёным лососем — идеальная пашот, насыщенный голландез",
            "Тарт Татен — карамелизированное яблочное совершенство",
            "Качество кофе — крепкий френч-пресс, отлично для неспешного утра"],
  },
  "bad": {
    "EN": ["Macarons — often stale from display case, 8 AZN each feels like a scam",
            "Croque-monsieur — tiny portion, cheese barely melted, not worth the price",
            "Onion soup — arrives lukewarm, lacks depth and body",
            "Omelettes — overcooked and rubbery, kitchen inconsistency"],
    "AZ": ["Makaronlar — vitrin şkafında bayatlamış, 8 AZN-ə dəyməz",
            "Krok-mesyö — kiçik porsiya, pendir əriməyib, qiymətinə dəyməz",
            "Soğan şorbası — ilıq gəlir, dadı və doyumluluğu yoxdur",
            "Omletlər — artıq bişirilib, rezin kimi, mətbəx qeyri-sabitdir"],
    "RU": ["Макароны — часто чёрствые из витрины, 8 AZN за штуку — грабёж",
            "Крок-месье — крошечная порция, сыр еле расплавлен, не стоит цены",
            "Луковый суп — приходит тёплым, нет глубины вкуса",
            "Омлеты — пережарены, резиновые, нестабильность кухни"],
  },
  "vibe": {
    "EN": ["Beautiful French interior, Instagram-worthy terrace on the boulevard",
            "Best for weekend brunch or morning pastry + coffee",
            "Avoid weekday lunch rush (12–2 PM) — kitchen gets overwhelmed",
            "Tip: Stick to pastries and egg dishes, skip the hot French classics"],
    "AZ": ["Gözəl fransız interyer, bulvar üzərində Instagram-a layiq terras",
            "Həftəsonu brançı və ya səhər kruassan + kofe üçün ideal",
            "İş günü nahar saatından (12–14) qaçının — mətbəx çaşır",
            "Məsləhət: Şirniyyatlara və yumurta yeməklərinə sadiq qalın"],
    "RU": ["Красивый французский интерьер, терраса на бульваре для Instagram",
            "Лучше всего для бранча на выходных или утренней выпечки с кофе",
            "Избегайте обеденного часа пик (12–14) — кухня не справляется",
            "Совет: Берите выпечку и яичные блюда, пропускайте горячую классику"],
  },
  "reviews": {
    "EN": '⭐⭐⭐⭐ "Croissants are divine — flaky, buttery, fresh every morning."\n⭐⭐⭐ "Waited 30 min for a Caesar salad. Croutons stale, dressing too heavy."\n⭐⭐ "Croque-monsieur was tiny, cheese barely melted. Staff forgot coffee twice."\n⭐⭐⭐⭐⭐ "Eggs Benedict with smoked salmon is perfection. Beautiful interior."\n⭐⭐⭐ "Hot dishes inconsistent. Onion soup lukewarm. Steak frites was great."\n⭐⭐ "Macarons looked gorgeous but tasted stale — 8 AZN each, unacceptable."\n⭐⭐⭐⭐ "Terrace overlooking the boulevard is lovely. Tarte Tatin was heavenly."\n⭐⭐⭐ "Pancakes fluffy and great, but the omelette was rubbery. Coffee excellent."',
    "AZ": '⭐⭐⭐⭐ "Kruassanlar əladır — təzə, kərəyağlı, hər səhər mükəmməl."\n⭐⭐⭐ "Sezar salatı üçün 30 dəq gözlədik. Krutonlar bayat, sous ağır idi."\n⭐⭐ "Krok-mesyö kiçik idi, pendir əriməmişdi. Kofe sifarişimizi iki dəfə unutdular."\n⭐⭐⭐⭐⭐ "Qızılbalıqlı Benedikt yumurtası mükəmməldir. Gözəl interyer."\n⭐⭐⭐ "İsti yeməklər qeyri-sabitdir. Soğan şorbası ilıq idi. Steyk frit əla."\n⭐⭐ "Makaronlar gözəl görünürdü amma bayat idi — hərəsi 8 AZN, qəbuledilməz."\n⭐⭐⭐⭐ "Bulvar mənzərəli terras əladır. Tarte Tatin möhtəşəm idi."\n⭐⭐⭐ "Pancake yumşaq idi, amma omlet rezin idi. Kofe əla."',
    "RU": '⭐⭐⭐⭐ "Круассаны божественны — слоистые, маслянистые, свежие каждое утро."\n⭐⭐⭐ "Ждали салат Цезарь 30 мин. Сухарики чёрствые, заправка тяжёлая."\n⭐⭐ "Крок-месье крошечный, сыр еле расплавлен. Забыли кофе дважды."\n⭐⭐⭐⭐⭐ "Яйца Бенедикт с лососем — совершенство. Красивый интерьер."\n⭐⭐⭐ "Горячие блюда нестабильны. Луковый суп тёплый. Стейк фрит отличный."\n⭐⭐ "Макароны красивые, но чёрствые — 8 AZN, недопустимо."\n⭐⭐⭐⭐ "Терраса с видом на бульвар прекрасна. Тарт Татен божественный."\n⭐⭐⭐ "Панкейки пышные, но омлет резиновый. Кофе отличный."',
  },
},
"Chinar": {
  "good": {
    "EN": ["8-hour slow-cooked lamb shoulder — signature dish, melts in your mouth",
            "Duck confit from tasting menu — masterfully prepared, crispy skin",
            "Beef tartare starter — perfectly seasoned, quail egg on top",
            "Sommelier wine pairings — knowledgeable, Georgian wines are a highlight"],
    "AZ": ["8 saatlıq yavaş bişirilmiş quzu çiyin — vizit kartı, ağızda əriyir",
            "Dadma menyusundan ördək konfit — usta işi, xırtıldayan qabıq",
            "Mal əti tartar — mükəmməl ədviyyatlı, üstündə bildirçin yumurtası",
            "Sommelye şərab seçimləri — peşəkar, Gürcü şərabları xüsusi tövsiyə"],
    "RU": ["Томлёное баранье плечо 8 часов — фирменное блюдо, тает во рту",
            "Утиный конфи из дегустационного меню — мастерски, хрустящая корочка",
            "Тартар из говядины — идеально приправлен, перепелиное яйцо сверху",
            "Винные пары от сомелье — профессионал, грузинские вина — хит"],
  },
  "bad": {
    "EN": ["Wine markup — 3x retail prices, astronomical even for house wines",
            "Chocolate fondant — inconsistently over-baked, loses the molten center",
            "Prix fixe pacing — courses arrive too fast, cannot enjoy each one",
            "Special occasions ignored — anniversary notes lost, no acknowledgment"],
    "AZ": ["Şərab qiymətləri — pərakəndədən 3 dəfə baha, hətta ev şərabları belə",
            "Şokolad fondan — bəzən artıq bişirilir, ərimiş mərkəzini itirir",
            "Pris fiks tempi — yeməklər çox tez gəlir, hər birindən zövq almaq olmur",
            "Xüsusi günlər nəzərə alınmır — ildönümü qeydləri itirilir"],
    "RU": ["Наценка на вино — в 3 раза выше розницы, даже домашние вина",
            "Шоколадный фондан — иногда перепечён, теряет жидкий центр",
            "Темп при-фикс — блюда приносят слишком быстро",
            "Особые случаи игнорируются — заметки о годовщине теряются"],
  },
  "vibe": {
    "EN": ["Stunning Old City rooftop with panoramic views — dress code enforced",
            "Best for business dinners and anniversaries (confirm celebration in advance)",
            "Avoid large group bookings — acoustics are poor for conversation",
            "Tip: Go for tasting menu + wine pairing, skip à la carte"],
    "AZ": ["Köhnə Şəhər üzərində möhtəşəm dam terras — geyim qaydası var",
            "İşgüzar naharlar və ildönümləri üçün ideal (bayramı əvvəlcədən təsdiqləyin)",
            "Böyük qrup sifarişlərindən qaçının — akustika söhbət üçün zəifdir",
            "Məsləhət: Dadma menyusu + şərab seçimi götürün, a la kart buraxın"],
    "RU": ["Потрясающая терраса на крыше Старого Города — дресс-код",
            "Лучше для деловых ужинов и годовщин (подтвердите праздник заранее)",
            "Избегайте больших групп — акустика плохая для разговора",
            "Совет: Берите дегустационное меню + винную пару, пропускайте а ля карт"],
  },
  "reviews": {
    "EN": '⭐⭐⭐⭐⭐ "Lamb shoulder melted in my mouth. World-class fine dining."\n⭐⭐⭐⭐ "Stunning rooftop, Old City views. Seafood risotto perfect. Wine markup 3x."\n⭐⭐⭐ "Beautiful setting but prix fixe felt rushed. Courses came too fast."\n⭐⭐⭐⭐⭐ "Tasting menu with wine pairing worth every manat. Duck confit masterpiece."\n⭐⭐ "Anniversary ignored despite reservation notes. Service felt impersonal."\n⭐⭐⭐⭐ "Beef tartare phenomenal. Chocolate fondant slightly over-baked."\n⭐⭐⭐ "Business dinner ruined by noise from adjacent table. Poor acoustics."\n⭐⭐⭐⭐ "Sommelier guided us perfectly. Pomegranate sorbet delightful surprise."',
    "AZ": '⭐⭐⭐⭐⭐ "Quzu çiyin ağızda əriyirdi. Dünya səviyyəli restoran."\n⭐⭐⭐⭐ "Möhtəşəm dam terrası, Köhnə Şəhər mənzərəsi. Risotto əla. Şərab 3x baha."\n⭐⭐⭐ "Gözəl mühit amma pris fiks tələsik idi. Yeməklər çox tez gəlirdi."\n⭐⭐⭐⭐⭐ "Şərab cütlüyü ilə dadma menyusu hər manatına dəyərdi."\n⭐⭐ "Rezervasiya qeydlərinə baxmayaraq ildönümü nəzərə alınmadı."\n⭐⭐⭐⭐ "Mal əti tartar fenomenal idi. Şokolad fondan bir az artıq bişirilmişdi."\n⭐⭐⭐ "İşgüzar nahar qonşu masanın səs-küyü ilə pozuldu."\n⭐⭐⭐⭐ "Sommelye bizi mükəmməl istiqamətləndirdi. Nar sorbeti xoş sürpriz idi."',
    "RU": '⭐⭐⭐⭐⭐ "Баранье плечо таяло во рту. Мировой уровень."\n⭐⭐⭐⭐ "Потрясающая крыша, вид на Старый Город. Ризотто идеально. Вино 3x."\n⭐⭐⭐ "Красиво, но при-фикс поспешный. Блюда приносили слишком быстро."\n⭐⭐⭐⭐⭐ "Дегустационное меню с вином стоило каждого маната."\n⭐⭐ "Годовщину проигнорировали несмотря на заметки."\n⭐⭐⭐⭐ "Тартар из говядины феноменален. Фондан чуть перепечён."\n⭐⭐⭐ "Деловой ужин испорчен шумом от соседнего стола."\n⭐⭐⭐⭐ "Сомелье идеально нас направил. Гранатовый сорбет — сюрприз."',
  },
},
"Entrée": {
  "good": {
    "EN": ["Signature burger with truffle fries — juicy patty, perfect brioche bun",
            "Brunch avocado toast + poached eggs — Instagram-perfect AND delicious",
            "Cheese board & sharing plates — generous, well-curated for groups",
            "Cocktail menu — Aperol Spritz perfectly balanced, fair prices"],
    "AZ": ["İmza burger truffle kartofu ilə — şirəli, mükəmməl brioş çörəyi",
            "Brunch avokado tostu + poçe yumurta — Instagram-a layiq VƏ dadlı",
            "Pendir lövhəsi və paylaşma boşqabları — səxavətli, qruplar üçün ideal",
            "Kokteyl menyusu — Aperol Spritz mükəmməl balansda, ədalətli qiymətlər"],
    "RU": ["Фирменный бургер с трюфельным фри — сочная котлета, идеальная бриошь",
            "Тост с авокадо + пашот — красиво для Instagram И вкусно",
            "Сырная доска и блюда для компании — щедро, отлично подобрано",
            "Коктейльное меню — Апероль Шприц идеально сбалансирован"],
  },
  "bad": {
    "EN": ["Pasta carbonara — made with cream instead of eggs, not authentic",
            "Tiramisu — pre-made days ago, soggy, zero coffee flavor",
            "Peak-hour wait times — up to 40 min for food on busy nights",
            "Music volume — too loud for dinner conversation, have to shout"],
    "AZ": ["Pasta karbonara — yumurta əvəzinə qaymaqla hazırlanıb, orijinal deyil",
            "Tiramisu — günlər öncə hazırlanıb, islanmış, kofe dadı yoxdur",
            "Pik saatlarda gözləmə — məşğul axşamlarda yeməyə 40 dəq gözləmə",
            "Musiqi səsi — nahar söhbəti üçün çox yüksək, qışqırmaq lazımdır"],
    "RU": ["Паста карбонара — на сливках вместо яиц, не аутентична",
            "Тирамису — приготовлено за дни до подачи, размокшее, без кофе",
            "Ожидание в час пик — до 40 мин за еду в загруженные вечера",
            "Громкость музыки — слишком громко, приходится кричать"],
  },
  "vibe": {
    "EN": ["Trendy modern interior, great for groups and after-work drinks",
            "Best for weekend brunch or casual evening with friends",
            "Avoid Friday/Saturday dinner 8–10 PM — painfully slow service",
            "Tip: Sit on the terrace for quieter conversation, order the burger"],
    "AZ": ["Trendy müasir interyer, qruplar və iş sonrası içkilər üçün əla",
            "Həftəsonu brançı və ya dostlarla rahat axşam üçün ideal",
            "Cümə/Şənbə naharı 20:00–22:00 arası qaçının — çox yavaş xidmət",
            "Məsləhət: Sakit söhbət üçün terrasa oturun, burger götürün"],
    "RU": ["Модный современный интерьер, отлично для компаний и после работы",
            "Лучше для бранча на выходных или вечера с друзьями",
            "Избегайте пятницы/субботы 20–22 — болезненно медленный сервис",
            "Совет: Садитесь на террасу, берите бургер"],
  },
  "reviews": {
    "EN": '⭐⭐⭐⭐ "Burger is one of the best in Baku. Truffle fries are addictive."\n⭐⭐⭐ "Nice interior but music way too loud. Salmon poke bowl was fresh."\n⭐⭐ "Pasta carbonara swimming in cream. That is not carbonara."\n⭐⭐⭐⭐⭐ "Brunch is phenomenal! Avocado toast with poached eggs was perfect."\n⭐⭐⭐ "Service slow at peak hours. Waited 40 min. Grilled chicken juicy."\n⭐⭐⭐⭐ "After-work drinks are great. Cheese board is generous."\n⭐⭐ "Tiramisu was soggy mush. No coffee flavor. Made days ago."\n⭐⭐⭐⭐ "Great for groups! Calamari crispy, bruschetta trio creative."',
    "AZ": '⭐⭐⭐⭐ "Burger Bakının ən yaxşılarından biridir. Truffle kartof asılılıq yaradır."\n⭐⭐⭐ "Gözəl interyer amma musiqi çox yüksəkdir. Qızılbalıq poke kasası təzə idi."\n⭐⭐ "Pasta karbonara qaymağa batmışdı. Bu karbonara deyil."\n⭐⭐⭐⭐⭐ "Brunch fenomenaldır! Poçe yumurtalı avokado tostu mükəmməl idi."\n⭐⭐⭐ "Pik saatlarda xidmət yavaşdır. 40 dəq gözlədik. Toyuq şirəli idi."\n⭐⭐⭐⭐ "İş sonrası içkilər əladır. Pendir lövhəsi səxavətlidir."\n⭐⭐ "Tiramisu islanmış idi. Kofe dadı yox. Günlər öncə hazırlanıb."\n⭐⭐⭐⭐ "Qruplar üçün əla! Kalamar xırtıldayan, brusketta yaradıcı idi."',
    "RU": '⭐⭐⭐⭐ "Бургер один из лучших в Баку. Трюфельный фри вызывает зависимость."\n⭐⭐⭐ "Красивый интерьер, но музыка слишком громкая. Поке с лососем свежий."\n⭐⭐ "Карбонара плавала в сливках. Это не карбонара."\n⭐⭐⭐⭐⭐ "Бранч феноменален! Тост с авокадо и пашот идеальны."\n⭐⭐⭐ "Обслуживание медленное в час пик. Ждали 40 мин. Курица сочная."\n⭐⭐⭐⭐ "После работы здесь отлично. Сырная доска щедрая."\n⭐⭐ "Тирамису — размокшая каша. Без кофе. Сделано дни назад."\n⭐⭐⭐⭐ "Отлично для компаний! Кальмары хрустящие, брускетты креативные."',
  },
},
}

# ═══════════════════════════════════════════════════════════════════════
# MOCK ANALYSIS — fully translated
# ═══════════════════════════════════════════════════════════════════════
MOCK_ANALYSIS = {
"EN": """## 🍔 Food & Dish Issues

| Dish | Problem | Mentions | Severity |
|------|---------|----------|----------|
| **Macarons** | Stale from display, no freshness | 2x | 🔴 Critical |
| **Pasta Carbonara** | Made with cream, incorrect technique | 2x | 🔴 Critical |
| **Tiramisu** | Pre-made days ago, soggy | 1x | 🔴 Critical |
| **Croque-Monsieur** | Tiny portion, cheese not melted | 1x | 🟡 Medium |
| **Onion Soup** | Served lukewarm, lacks depth | 1x | 🟡 Medium |

---

## ⚙️ Service & Operational Issues

- **⏱️ Excessive Wait Times** — 30+ min for simple dishes. Kitchen bottleneck.
- **👻 Forgotten Orders** — Coffee lost twice in one visit. Staff tracking failure.
- **🎂 Special Occasions Ignored** — Anniversary noted, zero acknowledgment.
- **🔊 Noise Levels** — Music too loud for dinner conversation.
- **😐 Poor Complaint Handling** — Manager shrugged at valid complaint.

---

## 💰 Financial Margin Risk

> **⚠️ HIGH — Premium Brand Erosion**

1. **High-margin desserts failing.** Macarons (8 AZN) carry 70-80% margins yet draw harshest complaints.
2. **Special occasion failures = lost lifetime value.** Celebration customers spend 3-5x more annually.
3. **Technique errors damage credibility.** Cream-based "carbonara" erodes trust.
4. **Bright spots** 🌟 — Croissants, Eggs Benedict, terrace experience are anchor assets.
""",
"AZ": """## 🍔 Yemək Problemləri

| Yemək | Problem | Qeydlər | Ciddilik |
|-------|---------|---------|----------|
| **Makaronlar** | Vitrində bayatlamış | 2x | 🔴 Kritik |
| **Pasta Karbonara** | Qaymaqla hazırlanıb, yanlış texnika | 2x | 🔴 Kritik |
| **Tiramisu** | Günlər öncə hazırlanıb, islanmış | 1x | 🔴 Kritik |
| **Krok-Mesyö** | Kiçik porsiya, pendir əriməyib | 1x | 🟡 Orta |
| **Soğan Şorbası** | İlıq gəlib, dadı zəifdir | 1x | 🟡 Orta |

---

## ⚙️ Xidmət Problemləri

- **⏱️ Həddindən Artıq Gözləmə** — Sadə yeməklər üçün 30+ dəq. Mətbəx darboğazı.
- **👻 Unudulmuş Sifarişlər** — Kofe bir ziyarətdə iki dəfə itirildi.
- **🎂 Xüsusi Günlər Nəzərə Alınmır** — İldönümü qeyd edilmiş, sıfır reaksiya.
- **🔊 Səs Səviyyəsi** — Musiqi nahar söhbəti üçün çox yüksəkdir.
- **😐 Zəif Şikayət İdarəetməsi** — Menecer şikayətə çiyin çəkdi.

---

## 💰 Maliyyə Marja Riski

> **⚠️ YÜKSƏK — Premium Brend Eroziyası**

1. **Yüksək marjalı desertlər uğursuz olur.** Makaronlar (8 AZN) 70-80% marja daşıyır, lakin ən sərt şikayətləri alır.
2. **Xüsusi gün uğursuzluqları = itirilmiş ömürlük dəyər.** Bayram müştəriləri illik 3-5x daha çox xərcləyir.
3. **Texnika səhvləri etibarlılığa zərər verir.** Qaymaqla "karbonara" etibarı sarsıdır.
4. **İşıqlı nöqtələr** 🌟 — Kruassanlar, Benedikt Yumurtası, terras təcrübəsi dayaq nöqtələridir.
""",
"RU": """## 🍔 Проблемы Блюд

| Блюдо | Проблема | Упоминания | Серьёзность |
|-------|----------|------------|-------------|
| **Макароны** | Чёрствые из витрины | 2x | 🔴 Критично |
| **Карбонара** | На сливках, неправильная техника | 2x | 🔴 Критично |
| **Тирамису** | Приготовлено дни назад, размокшее | 1x | 🔴 Критично |
| **Крок-Месье** | Маленькая порция, сыр не расплавлен | 1x | 🟡 Среднее |
| **Луковый Суп** | Тёплый, нет глубины | 1x | 🟡 Среднее |

---

## ⚙️ Проблемы Сервиса

- **⏱️ Ожидание** — 30+ мин за простые блюда. Узкое место кухни.
- **👻 Забытые Заказы** — Кофе забыли дважды за визит.
- **🎂 Особые Случаи** — Годовщина отмечена, ноль реакции.
- **🔊 Шум** — Музыка слишком громкая для разговора.
- **😐 Жалобы** — Менеджер пожал плечами на жалобу.

---

## 💰 Риск Маржи

> **⚠️ ВЫСОКИЙ — Эрозия Премиального Бренда**

1. **Высокомаржинальные десерты провалены.** Макароны (8 AZN) с маржой 70-80% собирают самые жёсткие отзывы.
2. **Провал особых случаев = потеря LTV.** Клиенты на праздниках тратят в 3-5x больше.
3. **Ошибки техники подрывают доверие.** "Карбонара" на сливках в премиум-заведении.
4. **Светлые пятна** 🌟 — Круассаны, Яйца Бенедикт, терраса — якорные активы.
""",
}

MOCK_CAMPAIGN = {
"EN": """## 🚀 Win-Back Campaign: "Every Detail, Perfected."

### 📱 Instagram Caption *(Ready to Copy)*:

> 🥐 **We obsess over the details — so you don't have to.**
>
> Our pastry chef perfected a new macaron process: baked fresh every 4 hours, never from a display case.
>
> 💥 **Code FRESHBAKU — complimentary macaron box** with any brunch order this weekend.
>
> 📍 Reserve your terrace table ➡️ link in bio
>
> #BakuBrunch #FreshBaked #WeListened

---

### 📋 Strategy:

| Element | Detail |
|---------|--------|
| **Promo Code** | `FRESHBAKU` — Free macaron box (4pc) with brunch |
| **Duration** | Saturday + Sunday only |
| **Target** | Baku Instagram foodies 22–40 |
| **Spend** | 80 AZN boosted post |
| **In-Store** | Sign: "Baked fresh every 4 hours" |

### 🎯 Expected Impact:
- +20-30% weekend brunch traffic from lapsed customers
- Positive UGC from "macaron unboxing" moments
- New reviews counter stale complaints
- Each returning customer ≈ 35 AZN average ticket
""",
"AZ": """## 🚀 Geri Qazanma Kampaniyası: "Hər Detal Mükəmməldir."

### 📱 Instagram Başlıq *(Kopyalamağa Hazır)*:

> 🥐 **Biz detallara həsr olunuruq — siz rahatlayın.**
>
> Şirniyyat ustamız yeni makaron prosesini mükəmməlləşdirdi: hər 4 saatda təzə, heç vaxt vitrindən deyil.
>
> 💥 **Kod FRESHBAKU — brunch sifarişinə pulsuz makaron qutusu** bu həftəsonu.
>
> 📍 Terras masanızı rezerv edin ➡️ bio-dakı link
>
> #BakıBrunch #TəzəBişmiş #BizDinlədik

---

### 📋 Strategiya:

| Element | Detal |
|---------|-------|
| **Promo Kodu** | `FRESHBAKU` — Brunch ilə pulsuz makaron qutusu (4 ədəd) |
| **Müddət** | Yalnız Şənbə + Bazar |
| **Hədəf** | Bakı Instagram qurmanları 22–40 yaş |
| **Xərc** | 80 AZN gücləndirilmiş post |
| **Mağazada** | Yazı: "Hər 4 saatda təzə bişirilir" |

### 🎯 Gözlənilən Təsir:
- Əvvəlki müştərilərdən +20-30% həftəsonu brunch trafiki
- "Makaron açılışı" anlarından müsbət istifadəçi kontenti
- Yeni rəylər bayat şikayətləri əvəz edir
- Hər qayıdan müştəri ≈ 35 AZN orta çek
""",
"RU": """## 🚀 Кампания Возврата: "Каждая Деталь Совершенна."

### 📱 Instagram *(Готово к Копированию)*:

> 🥐 **Мы одержимы деталями — чтобы вам не пришлось.**
>
> Наш кондитер усовершенствовал макароны: свежая выпечка каждые 4 часа, никогда из витрины.
>
> 💥 **Код FRESHBAKU — бесплатные макароны** к любому бранчу в эти выходные.
>
> 📍 Забронируйте столик ➡️ ссылка в био
>
> #БакуБранч #СвежаяВыпечка #МыУслышали

---

### 📋 Стратегия:

| Элемент | Детали |
|---------|--------|
| **Промокод** | `FRESHBAKU` — Макароны (4шт) к бранчу |
| **Срок** | Суббота + воскресенье |
| **Аудитория** | Бакинские фуди 22–40 лет |
| **Бюджет** | 80 AZN продвигаемый пост |
| **В заведении** | Табличка: "Выпечка каждые 4 часа" |

### 🎯 Ожидаемый Эффект:
- +20-30% трафика бранча от ушедших клиентов
- Позитивный UGC от "распаковки макарон"
- Новые отзывы перекрывают жалобы
- Каждый вернувшийся клиент ≈ 35 AZN средний чек
""",
}

# ═══════════════════════════════════════════════════════════════════════
# LLM INTEGRATION
# ═══════════════════════════════════════════════════════════════════════
def call_llm(sys_prompt, user_prompt, api_key):
    if not api_key or not api_key.strip():
        return None
    try:
        client = OpenAI(api_key=api_key.strip())
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": sys_prompt},
                      {"role": "user", "content": user_prompt}],
            temperature=0.7, max_tokens=2000,
        )
        return resp.choices[0].message.content
    except Exception as e:
        st.warning(f"⚠️ API error ({type(e).__name__}). Using demo data.")
        return None

def run_analysis(reviews, api_key):
    r = call_llm(
        "You are a Restaurant Operations Consultant and Financial Analyst. "
        "Return a Markdown report with: 1) Table of food issues 2) Service issues bullets "
        "3) Financial margin risk assessment. Use bold, emojis, tables.",
        f"Analyze:\n\n{reviews}", api_key)
    return r if r else MOCK_ANALYSIS[st.session_state.lang]

def run_campaign(analysis, api_key):
    r = call_llm(
        "You are a premium restaurant Social Media Marketer. Generate Instagram caption with "
        "promo code, strategy table, expected outcomes. Markdown, bold, emojis. Baku context.",
        f"Campaign for:\n\n{analysis}", api_key)
    return r if r else MOCK_CAMPAIGN[st.session_state.lang]

def run_foodie(name, api_key):
    return call_llm(
        "You are a brutally honest Baku food critic. Provide 3 sections in Markdown: "
        "What to Order, What to Avoid, Vibe & Tips. Bold dish names, emojis.",
        f"Honest truth about '{name}' in Baku.", api_key)

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
                st.session_state.analysis = run_analysis(reviews_input, api_key)

        if st.session_state.analysis:
            st.markdown('<hr class="mm-divider">', unsafe_allow_html=True)
            st.markdown(f"### {t('analysis_t')}")
            st.markdown(st.session_state.analysis)

            st.markdown('<hr class="mm-divider">', unsafe_allow_html=True)
            if st.button(t("btn_campaign"), type="secondary", use_container_width=True, key="ex_cp"):
                with st.spinner(t("spin2")):
                    st.session_state.campaign = run_campaign(st.session_state.analysis, api_key)

            if st.session_state.campaign:
                st.markdown(st.session_state.campaign)

