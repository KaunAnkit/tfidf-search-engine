import urllib
import requests
from bs4 import BeautifulSoup,Comment

def url_data_featcher(base_url):
    try:
        with urllib.request.urlopen(base_url) as response:
            html = response.read()
            return html

    except Exception as e :
        raise
