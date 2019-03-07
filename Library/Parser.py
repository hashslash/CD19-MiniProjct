class Parser:
    parse_table = {}
    parse_tree = {}
    __result = True

    def __init__(self, tid_s, grammar, data):
        self.tid_s = tid_s
        self.grammar = grammar
        self.__generate_parse_table()
        self.__parse(data)

    def __generate_parse_table(self):
        variables = self.grammar.get_variable_list()

        for i in variables:
            self.parse_table[i] = {}
            fir = self.grammar.first(i)
            for j in fir:
                if j.id != "null":
                    try:
                        self.parse_table[i][j] += fir[j]
                    except:
                        self.parse_table[i][j] = fir[j]
                else:
                    fol = self.grammar.follow(i)
                    for k in fol:
                        try:
                            self.parse_table[i][k] += fir[j]
                        except:
                            self.parse_table[i][k] = fir[j]
        for i in self.parse_table:
            for j in self.parse_table[i]:
                if len(self.parse_table[i][j]) > 1:
                    self.grammar.LL1 = False

    def __parse(self, data):
        stack = []
        pass

    def get_result(self):
        return

    def get_parse_table(self):
        return self.parse_table
