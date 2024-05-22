class Layout:
    def __init__(self):
        self.children = []

    def add_element(self, element):
        self.children.append(element)

    def add_elements(self, *args):
        for element in args:
            self.add_element(element)

    def reset(self):
        for element in self.children:
            element.reset()

    def draw(self, surface, auto_render=False):
        for child in self.children:
            child.draw(surface, auto_render)

    def render(self):
        for child in self.children:
            child.render()

    def event(self, event, sender):
        for child in self.children:
            if child._event(event, sender):
                break
