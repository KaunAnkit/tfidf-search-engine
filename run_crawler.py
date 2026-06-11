from crawler.crawl_loop import crawl
from storage.storage import init_db

init_db()

seed_sites = [
    "https://www.kernel.org/doc",
    "https://www.eff.org",
    "https://www.freecodecamp.org/news",
    "https://www.smashingmagazine.com",
    "https://css-tricks.com",
    "https://www.digitalocean.com/community/tutorials",
    "https://www.howstuffworks.com",
    "https://www.ietf.org/rfc"
]

for site in seed_sites:
    crawl(site, max_pages=50, max_depth=2)
    print("done")