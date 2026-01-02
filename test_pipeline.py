from crawler.controller import url_input
from storage.storage import init_db, save_document

url = "https://docs.python.org/3/library/re.html"

init_db()
doc = url_input(url)

if doc:
    saved = save_document(doc)
    print("Saved:", saved)
else:
    print("Failed to crawl")

