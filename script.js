const API_URL = "https://search-engine-node-backend.onrender.com/search";

const searchBtn = document.getElementById("searchBtn");
const queryInput = document.getElementById("query");
const resultsEl = document.getElementById("results");
const statusEl = document.getElementById("status");
const containerEl = document.getElementById("searchContainer");

searchBtn.addEventListener("click", search);
queryInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") search();
});

async function search() {
  const query = queryInput.value.trim();

  if (!query) return;

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