from Library.TokenIdentifier import TokenIdentifier


class Grammar:
    productions = []
    __variables = []
    __terminals = []

    def __init__(self):
        self.productions = []

    def get_productions(self):
        return self.productions

    def get_variable_list(self):
        if len(self.__variables) == 0:
            # list all variables
            for i in self.productions:
                self.__variables.append(i.variable)
            self.__variables = list(set(self.__variables))
            # list all terminals
            for i in self.productions:
                for j in i.rhs:
                    if type(j) == TokenIdentifier:
                        self.__terminals.append(j)
            self.__terminals = list(set(self.__terminals))
        return self.__variables

    def add_production(self, production):
        self.productions.append(production)

    def first(self, variable):
        prods = []
        for i in self.productions:
            if i.variable == variable:
                prods.append(variable)

    def follow(self, variable):
        return
