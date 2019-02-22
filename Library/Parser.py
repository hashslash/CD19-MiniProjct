class Parser:
    parse_table = {}
    parse_tree = {}

    def __init__(self, tid_s, grammar, data):
        self.tid_s = tid_s
        self.grammar = grammar
        self.__generate_parse_table()
        self.__parse(data)

    def __generate_parse_table(self):
        variables = self.grammar.get_variable_list()
        for variable in variables:
            first_set = self.grammar.first(variable)
            self.parse_table[variable] = first_set

    def __parse(self, data):
        pass

    def get_parse_tree(self):
        return self.parse_tree

    def get_parse_table(self):
        return self.parse_table
