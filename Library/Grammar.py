class Grammar:
    productions = []

    def __init__(self):
        self.productions = []

    def get_productions(self):
        return self.productions

    def add_production(self, production):
        self.productions.append(production)

    def first(self, variable):
        return

    def follow(self, variable):
        return
