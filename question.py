from tag import Tag

class Question:

    def __init__(self, dom_node):
        self._dom_node = dom_node

    def _str_to_int(self, s):
        facts = {'k': 10**3,
                 'm': 10**6}
        fact = s[-1]

        if fact in facts.keys():
            n = int(s[:-1]) * facts[fact]
        else:
            n = int(s)
        return n

    def title(self):
        h3 = self._dom_node.find('h3')
        return h3.a.string

    def votes(self):
        node = self._dom_node.find('div', class_="votes")
        return self._str_to_int(node.div.span.string)

    def answers(self):
        node = self._dom_node.find('div', class_="status")
        return self._str_to_int(node.div.span.string)

    def views(self):
        node = self._dom_node.find('div', class_="views")
        return self._str_to_int(node.div.span.string)

    def tags(self):
        nodes = self._dom_node.find_all('a', class_="post-tag")
        return [Tag(node) for node in nodes]



