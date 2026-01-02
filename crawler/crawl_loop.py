from crawler.controller import url_input
from storage.storage import save_document
from collections import deque


def crawl(seed_url, max_pages=10, max_depth=2):

    queue = deque()
    visited = set()

    queue.append((seed_url, 0))
    pages_crawled = 0

    while queue and pages_crawled < max_pages:
        current_url, depth = queue.popleft()

        if current_url in visited:
            continue

        if depth > max_depth:
            continue

        data = url_input(current_url)

        visited.add(current_url)

        if data is None:
            continue

        saved = save_document(data)

        if saved:
            pages_crawled += 1

        for link in data.get("Links", []):
            if link not in visited:
                queue.append((link, depth + 1))

    
