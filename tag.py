from bs4 import BeautifulSoup

class Tag:

    def __init__(self, dom_node):
        self._dom_node = dom_node

    def name(self):
        return self._dom_node.string
