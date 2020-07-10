class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.taken = False

    def on_take(self):
        self.taken = True

    def on_drop(self):
        self.taken = False
