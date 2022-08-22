class Component:
    def __init__(self):
        self.child: 'List[Component]' = []
        pass

    def render_all(self):
        self.render()
        for child in self.child:
            child.render()

    def render(self):
        pass

    def add(self, component: 'Component'):
        self.child.append(component)
