from Library.TokenIdentifier import TokenIdentifier


class Grammar:
    productions = []
    __variables = []
    __terminals = []
    LL1 = True

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
        return self.__variables

    def get_terminal_list(self):
        if len(self.__terminals) == 0:
            # list all terminals
            for i in self.productions:
                for j in i.rhs:
                    if type(j) == TokenIdentifier:
                        self.__terminals.append(j)
            self.__terminals = list(set(self.__terminals))
        return self.__terminals

    def add_production(self, production):
        self.productions.append(production)

    def first(self, x):
        first = {}
        prods = []
        for i in self.productions:
            if i.variable == x:
                prods.append(i)

        for i in prods:
            for j in i.rhs:
                finish = 1
                if type(j) is TokenIdentifier:
                    try:
                        first[j].append(i)
                    except:
                        first[j] = [i]
                else:
                    fir = self.first(j)
                    for k in fir:
                        try:
                            first[k].append(i)
                        except:
                            first[k] = [i]
                    for k in fir:
                        if k.id == "null":
                            finish = 0
                if finish == 1:
                    break
        return first

    def follow(self, x):
        follow = []

        prods = []
        for i in self.productions:
            for j in i.rhs:
                if j == x:
                    prods.append(i)

        for i in prods:
            for j in range(len(i.rhs)):
                if i.rhs[j] == x:
                    finish = 1
                    off = 1
                    while True:
                        if len(i.rhs) == j + off:
                            if i.variable != x:
                                follow += self.follow(i.variable)
                                finish = 1
                        else:
                            if type(i.rhs[j + off]) is TokenIdentifier:
                                follow.append(i.rhs[j + off])
                                finish = 1
                            else:
                                fir = self.first(i.rhs[j + off])
                                for k in fir:
                                    if k.id == "null":
                                        off += 1
                                        finish = 0
                                    else:
                                        follow.append(k)
                        if finish == 1:
                            break
        follow = list(set(follow))
        return follow
