from Library.Production import Production
from Library.Grammar import Grammar


class GrammarGenerator:

    def __init__(self, stream):
        self.stream = stream
        self.grammar = Grammar()
        self.__generate()

    def __generate(self):
        for i in self.stream:
            var = i.split()[0]
            rhs = i.split()[1:]
            production = Production(var, rhs)
            self.grammar.add_production(production)

    def get_grammer(self):
        return self.grammar
