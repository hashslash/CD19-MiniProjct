from Library.LexicalAnalyser import LexicalAnalyser
from Library.TokenIdentifier import TokenIdentifier
from Library.Variables import Variable
from Library.util import Stack


class Parser:
    parse_table = {}
    parse_tree = {}
    __result = False

    def __init__(self, tid_s, grammar):
        self.tid_s = tid_s
        self.grammar = grammar
        self.__generate_parse_table()

    def __generate_parse_table(self):
        variables = self.grammar.get_variable_list()
        for i in variables:
            sync = True
            self.parse_table[i] = {}
            fir = self.grammar.first(i)
            for j in fir:
                if j.id != "null":
                    try:
                        self.parse_table[i][j] += fir[j]
                    except:
                        self.parse_table[i][j] = fir[j]
                else:
                    sync = False
                    fol = self.grammar.follow(i)
                    for k in fol:
                        try:
                            self.parse_table[i][k] += fir[j]
                        except:
                            self.parse_table[i][k] = fir[j]
            if sync:
                for j in self.grammar.follow(i):
                    self.parse_table[i][j] = ["sync"]

        for i in self.parse_table:
            for j in self.parse_table[i]:
                if len(self.parse_table[i][j]) > 1:
                    self.grammar.LL1 = False

    def __getToken(self, Idn, lexer):
        # panic mode recovey
        while True:
            token = lexer.get_next_token()
            try:
                if token.id == Idn.id:
                    return token
            except:
                print("Parsing failed...")
                exit(1)

    def __tree(self, root, lexer):
        print("tree for", root)
        tree = {}
        token = production = None
        while True:
            token = lexer.get_next_token()
            try:
                # production = self.parse_table[root][token]
                for i in self.parse_table:
                    if i == root:
                        for j in self.parse_table[i]:
                            if j.id == token.id:
                                production = self.parse_table[i][j][0]
                if production is None:
                    continue
                print("Production--", production)
                break
            except KeyError:
                pass
            except:
                print("Parsing failed...")
                exit(1)
        children = []
        for i in production.rhs:
            if type(i) is TokenIdentifier:
                children.append(self.__getToken(i, lexer))
            else:
                children.append(self.__tree(i, lexer))
        return tree

    def __parse(self, token_id, data):
        '''

        lexer = LexicalAnalyser(token_id, data)
        self.parse_tree = self.__tree(Variable("St"), lexer)

        '''
        top_of_stack = next_token = None
        stack = Stack()
        stack.push(Variable("St"))
        lex = LexicalAnalyser(token_id, data)

        while True:
            print()
            print(str(stack).center(50, " "), end="|")
            if stack.is_empty():
                next_token = lex.get_next_token()
                if next_token is None:
                    self.__result = True
                    print()
                    print("-" * 152)
                    print("\nParsing Successfull\nValid")
                    return
                else:
                    print("\nError Occured at >>", next_token.lexeme)
                    print("Parsing Failed")
                    exit(0)
            else:
                # print("stack-----", str(stack))
                top_of_stack = stack.pop()
                # print("top===", top_of_stack)
                # check for epsilon
                if type(top_of_stack) is TokenIdentifier and top_of_stack.id == "null":
                    print("null".center(50), end="|")
                    print(str("match null").center(50), end="|")
                    continue
                # next token
                if next_token is None:
                    next_token = lex.get_next_token()
                print(str(next_token).center(50, " "), end="|")
                # print("token-", next_token.lexeme)
                # check if input is at end
                if next_token is None or next_token.id == "eoc" and type(
                        top_of_stack) is TokenIdentifier and top_of_stack.id != "eoc":
                    print("Error")
                    return
                if type(top_of_stack) is TokenIdentifier:
                    if top_of_stack.id == next_token.id:
                        next_token = None
                        print(str("match " + str(top_of_stack)).center(50), end="|")
                    else:
                        print("\nExpected", top_of_stack.id, "Found", next_token.id)
                        print()
                        __result = False
                        return
                else:
                    try:
                        prod = None
                        for i in self.parse_table:
                            if i == top_of_stack:
                                for j in self.parse_table[i]:
                                    if j.id == next_token.id:
                                        prod = self.parse_table[i][j][0]
                                        print(str(prod).center(50, " "), end="|")
                                        # print(prod)
                        if prod is None:
                            continue
                    except:
                        print("Error at >", next_token.lexeme)
                        return
                    for i in prod.rhs[::-1]:
                        stack.push(i)

    def parse(self, data):
        print("Parsing...")
        print("-" * 152)
        print(str("stack").center(50, " "), end="|")
        print(str("Input").center(50, " "), end="|")
        print(str("Action").center(50, " "), end="|")
        print()
        print("-" * 152)
        self.__parse(self.tid_s, data)

    def get_result(self):
        return self.__result

    def get_parse_table(self):
        return self.parse_table
