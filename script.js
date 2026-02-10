const API_URL = "https://tfidf-node-api.onrender.com/search";

const searchBtn = document.getElementById("searchBtn");
const queryInput = document.getElementById("query");
const resultsEl = document.getElementById("results");
const statusEl = document.getElementById("status");

searchBtn.addEventListener("click", search);
queryInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") search();
});

async function search() {
  const query = queryInput.value.trim();

  if (!query) return;

  resultsEl.innerHTML = "";
  statusEl.textContent = "Searching...";

  try {
    const res = await fetch(`${API_URL}?q=${encodeURIComponent(query)}`);
    const data = await res.json();

    if (!data.results || data.results.length === 0) {
      statusEl.textContent = "No results found.";
      return;
    }

    statusEl.textContent = `Found ${data.results.length} results`;

    data.results.forEach(item => {
      const li = document.createElement("li");
      li.className = "result";

      // Logic matches your original template precisely
      li.innerHTML = `
        <a href="${item.url}" target="_blank">${item.title}</a>
        <div class="url">${item.url}</div>
        <div class="score">score: ${item.score.toFixed(4)}</div>
      `;

      resultsEl.appendChild(li);
    });

  } catch (err) {
    console.error(err);
    statusEl.textContent = "Search failed. Is the server running?";
  }
}
