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

    def get_terminal_list(self):
        if len(self.__terminals) == 0:
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
        return self.__terminals

    def add_production(self, production):
        self.productions.append(production)

    def first(self, variable):
        prods = []
        first = {}
        for i in self.productions:
            if i.variable == variable:
                prods.append(i)

        for i in prods:
            if type(i.rhs[0]) is TokenIdentifier:
                try:
                    first[i.rhs[0]].append(i)
                except Exception:
                    first[i.rhs[0]] = [i]
            else:
                ter = self.first(i.rhs[0])
                for k in ter:
                    try:
                        first[k].append(i)
                    except Exception:
                        first[k] = [i]
        return first

    def follow(self, variable):
        return
