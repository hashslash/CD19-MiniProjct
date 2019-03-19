from Library.LexicalAnalyser import LexicalAnalyser
from Library.TokenIdentifier import TokenIdentifier
from Library.Variables import Variable
from Library.util import Stack
from Library.Token import Token


class Parser:
    parse_table = {}
    parse_tree = {}
    __result = False

    def __init__(self, tid_s, grammar, data):
        self.tid_s = tid_s
        self.grammar = grammar
        self.__generate_parse_table()
        self.__parse(tid_s, data)

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

    def __parse(self, token_id, data):
        stack = Stack()
        stack.push(Variable("St"))
        lex = LexicalAnalyser(token_id, data)
        while True:
            if stack.is_empty():
                next_token = lex.get_next_token()
                if next_token.id == "eoc":
                    __result = True
                    print("Parsing Successfull")
                    print("Valid Input")
                else:
                    print("Error Occured at >>", next_token.lexeme)
            else:
                top_of_stack = stack.pop()
                if type(top_of_stack) is Token and top_of_stack.id == "null":
                    continue
                next_token = lex.get_next_token()
                print("token-", next_token.lexeme)
                if next_token.id == "eoc":
                    print("Error Occured ... Extra tokens Found")
                    return
                if type(top_of_stack) is Token:
                    if top_of_stack == next_token:
                        pass
                    else:
                        print("Expected", top_of_stack.lexeme, "Found", next_token.lexeme)
                        __result = False
                        return
                else:
                    print(type(top_of_stack), next_token, next_token.__hash__())
                    for i in self.parse_table[top_of_stack][TokenIdentifier("a", "a")]:
                        print(i.__hash__())
                    exit(0)
                    try:
                        prod = self.parse_table[top_of_stack][next_token][0]
                    except:
                        print("Error at >", next_token.lexeme)
                        return
                    for i in prod.rhs[::-1]:
                        stack.push(i)

    def get_result(self):
        return self.__result

    def get_parse_table(self):
        return self.parse_table
