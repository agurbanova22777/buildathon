"""Static demo data, translations, credentials, and KPI snapshots for MenuMind AI."""

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

