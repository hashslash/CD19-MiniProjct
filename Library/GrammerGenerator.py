from Library.Production import Production
from Library.Grammar import Grammar
from Library.Variables import Variable


class GrammarGenerator:

    def __init__(self, stream, tid_s):
        self.stream = stream
        self.tid_s = tid_s
        self.grammar = Grammar()
        self.__generate()

    def __generate(self):
        no_of_productions = 1
        for i in self.stream:
            var = Variable(i.split()[0])
            rhs = self.__rhs_of(i.split()[1:])
            production = Production(no_of_productions, var, rhs)
            self.grammar.add_production(production)
            no_of_productions += 1

    def get_grammar(self):
        return self.grammar

    def __rhs_of(self, str_arr):
        actual_rhs = []
        for i in str_arr:
            is_token = False
            for j in self.tid_s:
                if j.id == i:
                    is_token = True
                    actual_rhs.append(j)
            if not is_token:
                actual_rhs.append(Variable(i))
        return actual_rhs
