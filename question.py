

class Question:

    def __init__(self, dom_node):
        self.dom_node = dom_node

    def title(self):
        pass

    def views(self):
        out = self.dom_node.find_all('div', class_="question_summary")
        return out