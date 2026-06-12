const API_URL = "https://search-engine-node-backend.onrender.com/search";

const searchBtn = document.getElementById("searchBtn");
const queryInput = document.getElementById("query");
const resultsEl = document.getElementById("results");
const statusEl = document.getElementById("status");
const containerEl = document.getElementById("searchContainer");

const SUGGEST_URL =
  "https://tfidf-search-engine-1.onrender.com/suggest";

const suggestionsEl =
  document.getElementById("suggestions");

  queryInput.addEventListener(
  "input",
  loadSuggestions
);

searchBtn.addEventListener("click", search);
queryInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") search();
});

async function search() {
  const query = queryInput.value.trim();

  

  if (!query) return;

  suggestionsEl.innerHTML = "";
  suggestionsEl.classList.remove("show");

  // Triggers leftward and vertical alignment layout changes
  containerEl.classList.add("has-searched");
  
  resultsEl.innerHTML = "";
  statusEl.textContent = "Searching database...";

  try {
    const res = await fetch(`${API_URL}?q=${encodeURIComponent(query)}`);
    const data = await res.json();

    if (!data.results || data.results.length === 0) {
      statusEl.textContent = "No results found.";
      return;
    }

    statusEl.textContent = `Found ${data.results.length} results matching your query`;

    data.results.forEach((item, index) => {
      const li = document.createElement("li");
      li.className = "result";
      li.style.animationDelay = `${index * 0.03}s`;

      // Extract hostname for meta text display and favicon retrieval
      const parsedUrl = new URL(item.url);
      const hostname = parsedUrl.hostname;
      const faviconUrl = `https://www.google.com/s2/favicons?domain=${hostname}&sz=32`;

      li.innerHTML = `
        <div class="result-identity">
          <img class="favicon" src="${faviconUrl}" alt="" onerror="this.style.display='none'">
          <span class="domain-name">${hostname}</span>
          <div class="score-badge">Match: ${(item.score * 100).toFixed(1)}%</div>
        </div>
        <a href="${item.url}" target="_blank" class="result-title">${item.title}</a>
        <div class="url-display">${item.url}</div>
      `;

      resultsEl.appendChild(li);
    });

  } catch (err) {
    console.error(err);
    statusEl.textContent = "Search failed. Is the server running?";
  }
}

async function loadSuggestions() {

  const query =
    queryInput.value.trim();

  if (query.length < 2) {

    suggestionsEl.innerHTML = "";
    suggestionsEl.classList.remove("show");

    return;
  }

  try {

    const res = await fetch(
      `${SUGGEST_URL}?q=${encodeURIComponent(query)}`
    );

    const data = await res.json();

    renderSuggestions(data);

  } catch(err) {

    console.error(err);
  }
}

function renderSuggestions(items) {

  suggestionsEl.innerHTML = "";

  if (!items.length) {

    suggestionsEl.classList.remove("show");
    return;
  }

  items.forEach(item => {

    const div =
      document.createElement("div");

    div.className = "suggestion-item";

    div.textContent = item.title;

    div.addEventListener("click", () => {

      queryInput.value = item.title;

      suggestionsEl.innerHTML = "";
      suggestionsEl.classList.remove("show");

      search();
    });

    suggestionsEl.appendChild(div);
  });

  suggestionsEl.classList.add("show");
}