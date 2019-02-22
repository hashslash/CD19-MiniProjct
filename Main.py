from Library.TokenIdentifiersGenerator import TokenIdentifiersGenerator
from Library.GrammerGenerator import GrammarGenerator
from Library.Parser import Parser

# Create Token Identifiers
tig = TokenIdentifiersGenerator(open("Sources/Raw Tokens"))
tid_s = tig.token_identifiers()

# Print Tokens
print("\n\n----------------***Tokens***----------------")
for i in tid_s:
    print("|   " + str(i))
print("--------------------------------------------\n\n")

# Create Grammar
gra_gen = GrammarGenerator(open("Sources/Raw Grammar"), tid_s)
grammar = gra_gen.get_grammar()

# Print Grammar
print("--------------***Grammar***-----------------")
for i in grammar.get_productions():
    print("|   " + str(i))
print("--------------------------------------------\n\n")

# Parsing

code_file = open("Sources/Input String")
code = str(code_file.read())
parser = Parser(tid_s, grammar, code)

print("-----------***parse table***--------------")

parse_table = parser.get_parse_table()
terminals = grammar.get_terminal_list()
print("variables".center(10), end="|")
for i in terminals:
    print("|", str(i).center(49), end="|")
print()
for i in parse_table:
    print(str(i).center(10), end="|")
    for j in terminals:
        print("|", end="")
        try:
            pr = ""
            for k in parse_table[i][j]:
                pr += str(k)+","
            print(pr[:-1].center(50), end="|")
        except Exception:
            print("".center(50), end="|")
    print()

print("\n--------------------------------------------\n\n")

print("------------***Parse Tree***---------------")

print(str(parser.get_parse_tree()))

print("--------------------------------------------\n\n")
