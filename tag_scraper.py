from requests import get as http_get
from bs4 import BeautifulSoup
import re

class TagScraper:

    def __init__(self, url=None):
        self.url = url
        self.load_html()

    def load_html(self):
        self.html_doc = BeautifulSoup(http_get(self.url).text)

    def get_tags(self, html):
        rs = html.find_all('a', class_='post-tag')
        tags = [html_tag.string for html_tag in rs]
        return tags

    def filter_tags(self, html):
        

    def get_tag_stats(self):
        tags = self.get_tags(self.html_doc)
        # print(self.get_tags(self.html_doc))
        return tags


