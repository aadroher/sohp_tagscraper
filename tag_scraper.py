from requests import get as http_get
from bs4 import BeautifulSoup
import re
from datetime import datetime

class TagScraper:

    def __init__(self, url=None):
        self.url = url
        self.req_time = None
        self.load_html()

    def load_html(self):
        self.html_doc = BeautifulSoup(http_get(self.url).text)
        self.req_time = datetime.now()

    def get_tags(self, html):
        rs = html.find_all('a', class_='post-tag')
        tags = [html_tag.string for html_tag in rs]
        return tags

    def get_tag_freqs(self):
        patterns = {'php': '^php$',
                    'python': '^python(-2\.7|-3\.x)?$',
                    'java': '^java$'}
        tags = self.get_tags(self.html_doc)
        freqs = {}
        for k,pat in patterns.iteritems():
            freqs[k] = self._tag_count(tags, pat)
        return freqs

    def _tag_count(self, tags, pat):
         r = re.compile(pat, re.IGNORECASE)
         return len(filter(r.match, tags))