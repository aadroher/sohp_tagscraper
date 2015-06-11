from requests import get as http_get
from bs4 import BeautifulSoup
import re
from datetime import datetime
from tag import Tag

class Page:

    def __init__(self, url=None):
        self.url = url
        self.req_time = None
        self._dom = self._load_dom()
        # self.questions = self._get_questions()


    def _load_dom(self):
        dom = BeautifulSoup(http_get(self.url).text)
        self.req_time = datetime.now()
        return dom

    def tags(self):
        result_set = self._dom.find_all('a', class_='post-tag')
        tags = [Tag(dom_node) for dom_node in result_set]
        return tags

    def questions(self):
        result_set = self._dom.find_all('div', class_='question-summary')
        questions = [Question(dom_node) for dom_node in result_set]
        return questions

    def get_tag_freqs(self):
        patterns = {'php': '^php$',
                    'python': '^python(-2\.7|-3\.x)?$',
                    'java': '^java$'}
        tags = self.tags()
        freqs = {}
        for k,pat in patterns.iteritems():
            freqs[k] = self._tag_count(tags, pat)
        return freqs

    def _tag_count(self, tags, pat):
         r = re.compile(pat, re.IGNORECASE)
         return len(filter(r.match, [tag.get_name() for tag in tags]))

