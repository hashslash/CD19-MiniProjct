class Parser:
    parse_table = []

    def __init__(self, tid_s, grammar, data):
        self.tid_s = tid_s
        self.grammar = grammar
        self.__parse_table()
        self.__parse(data)

    def __parse_table(self):
        pass

    def get_parse_table(self):
        return self.parse_table

    def __parse(self, data):
        pass

    def get_parse_tree(self):
        pass
