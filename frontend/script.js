const BACKEND = "http://127.0.0.1:5000";

const els = {
  navBtns:        document.querySelectorAll(".nav-btn"),
  viewOwner:      document.getElementById("view-owner"),
  viewFoodie:     document.getElementById("view-foodie"),
  apiKey:         document.getElementById("api-key"),
  reviewsInput:   document.getElementById("reviews-input"),
  btnAnalyze:     document.getElementById("btn-analyze"),
  btnCampaign:    document.getElementById("btn-campaign"),
  analysisResult: document.getElementById("analysis-result"),
  analysisContent:document.getElementById("analysis-content"),
  campaignResult: document.getElementById("campaign-result"),
  campaignContent:document.getElementById("campaign-content"),
  copyCampaign:   document.getElementById("copy-campaign"),
  metricRating:   document.getElementById("metric-rating"),
  metricFeedback: document.getElementById("metric-feedback"),
  metricRisk:     document.getElementById("metric-risk"),
  metricRiskSub:  document.getElementById("metric-risk-sub"),
  restaurantInput:document.getElementById("restaurant-input"),
  btnVibe:        document.getElementById("btn-vibe"),
  foodieResult:   document.getElementById("foodie-result"),
  cardGood:       document.getElementById("card-good"),
  cardBad:        document.getElementById("card-bad"),
  cardTip:        document.getElementById("card-tip"),
  loadingOverlay: document.getElementById("loading-overlay"),
  loadingText:    document.getElementById("loading-text"),
};

els.navBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    els.navBtns.forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    const view = btn.dataset.view;
    els.viewOwner.classList.toggle("active", view === "owner");
    els.viewFoodie.classList.toggle("active", view === "foodie");
    els.viewOwner.classList.toggle("hidden", view !== "owner");
    els.viewFoodie.classList.toggle("hidden", view !== "foodie");
  });
});

function showLoading(msg) {
  els.loadingText.textContent = msg;
  els.loadingOverlay.classList.remove("hidden");
}

function hideLoading() {
  els.loadingOverlay.classList.add("hidden");
}

function markdownToHtml(text) {
  return text
    .replace(/^### (.+)$/gm, "<h3>$1</h3>")
    .replace(/^## (.+)$/gm, "<h3>$1</h3>")
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/^\- (.+)$/gm, "<li>$1</li>")
    .replace(/(<li>.*<\/li>)/gs, "<ul>$1</ul>")
    .replace(/\n{2,}/g, "<br/>")
    .replace(/^(?!<[hul]|<br)(.+)$/gm, "<p>$1</p>");
}

function setMetrics(rating, feedback, risk) {
  els.metricRating.textContent  = rating;
  els.metricFeedback.textContent = feedback;
  els.metricRisk.textContent    = risk;
  els.metricRisk.className      = "metric-value";
  if (risk.includes("HIGH"))   { els.metricRisk.classList.add("risk-high"); els.metricRiskSub.textContent = "immediate action needed"; }
  if (risk.includes("MEDIUM")) { els.metricRisk.classList.add("risk-med");  els.metricRiskSub.textContent = "monitor closely"; }
  if (risk.includes("LOW"))    { els.metricRisk.classList.add("risk-low");  els.metricRiskSub.textContent = "looking healthy"; }
}

async function callBackend(endpoint, payload) {
  const res = await fetch(`${BACKEND}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ...payload, api_key: els.apiKey.value.trim() }),
  });
  if (!res.ok) throw new Error(`Server error: ${res.status}`);
  return res.json();
}

els.btnAnalyze.addEventListener("click", async () => {
  const reviews = els.reviewsInput.value.trim();
  if (!reviews) return;

  els.btnAnalyze.disabled = true;
  showLoading("Analyzing reviews with AI...");

  try {
    const data = await callBackend("/analyze", { reviews });

    setMetrics(data.rating, data.feedback_rate, data.risk_level);

    els.analysisContent.innerHTML = markdownToHtml(data.analysis);
    els.analysisResult.classList.remove("hidden");
    els.btnCampaign.classList.remove("hidden");

    els.campaignResult.classList.add("hidden");
    els.campaignContent.innerHTML = "";
  } catch (err) {
    els.analysisContent.innerHTML = `<p style="color:red">Error: ${err.message}. Is the Flask server running?</p>`;
    els.analysisResult.classList.remove("hidden");
  } finally {
    hideLoading();
    els.btnAnalyze.disabled = false;
  }
});

els.btnCampaign.addEventListener("click", async () => {
  const reviews = els.reviewsInput.value.trim();
  if (!reviews) return;

  els.btnCampaign.disabled = true;
  showLoading("Crafting your recovery campaign...");

  try {
    const data = await callBackend("/campaign", { reviews });
    els.campaignContent.innerHTML = markdownToHtml(data.campaign);
    els.campaignResult.classList.remove("hidden");
  } catch (err) {
    els.campaignContent.innerHTML = `<p style="color:red">Error: ${err.message}. Is the Flask server running?</p>`;
    els.campaignResult.classList.remove("hidden");
  } finally {
    hideLoading();
    els.btnCampaign.disabled = false;
  }
});

els.copyCampaign.addEventListener("click", () => {
  const text = els.campaignContent.innerText;
  navigator.clipboard.writeText(text).then(() => {
    els.copyCampaign.textContent = "Copied!";
    setTimeout(() => (els.copyCampaign.textContent = "Copy post"), 2000);
  });
});

els.btnVibe.addEventListener("click", async () => {
  const name = els.restaurantInput.value.trim();
  if (!name) return;

  els.btnVibe.disabled = true;
  showLoading(`Looking up "${name}"...`);

  try {
    const data = await callBackend("/vibe", { restaurant: name });
    els.cardGood.innerHTML = markdownToHtml(data.good);
    els.cardBad.innerHTML  = markdownToHtml(data.bad);
    els.cardTip.innerHTML  = markdownToHtml(data.tip);
    els.foodieResult.classList.remove("hidden");
  } catch (err) {
    els.cardGood.innerHTML = `<p style="color:red">Error: ${err.message}. Is the Flask server running?</p>`;
    els.foodieResult.classList.remove("hidden");
  } finally {
    hideLoading();
    els.btnVibe.disabled = false;
  }
});


