from crawler.crawl_loop import crawl
from storage.storage import init_db

init_db()

seed_sites = [
    "https://docs.python.org",
    "https://realpython.com",
    "https://developer.mozilla.org",
    "https://docs.djangoproject.com",
    "https://flask.palletsprojects.com",
    "https://numpy.org/doc",
    "https://pandas.pydata.org/docs",
    "https://scikit-learn.org/stable",
    "https://fastapi.tiangolo.com",
    "https://www.geeksforgeeks.org",
    "https://martinfowler.com",
    "https://engineering.fb.com",
    "https://netflixtechblog.com",
    "https://cloud.google.com/blog",
    "https://aws.amazon.com/blogs",
    "https://opensource.google",
    "https://dev.to",
    "https://hashnode.com",
    "https://blog.cloudflare.com",
    "https://machinelearningmastery.com",
    "https://towardsdatascience.com",
    "https://distill.pub",
    "https://paperswithcode.com",
    "https://openai.com/research",
    "https://huggingface.co/blog",
    "https://ai.googleblog.com",
    "https://deepmind.com/blog",
    "https://karpathy.github.io",
    "https://colah.github.io",
    "https://www.khanacademy.org",
    "https://www.britannica.com",
    "https://plato.stanford.edu",
    "https://ocw.mit.edu",
    "https://www.w3.org/TR",
    "https://www.cs.cmu.edu/~15213",
    "https://www.nature.com/articles",
    "https://www.scientificamerican.com",
    "https://www.ibm.com/think",
    "https://www.oracle.com/technical-resources",
    "https://www.gnu.org/philosophy",
    "https://www.linux.org",
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