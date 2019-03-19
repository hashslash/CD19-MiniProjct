from Library.LexicalAnalyser import LexicalAnalyser
from Library.TokenIdentifier import TokenIdentifier
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

print("-" * (len(terminals) - 1) * 44)
print("variables".center(10), end="|")
for i in terminals:
    if i.id != 'null':
        print("|", str(i).center(39), end="|")
print()
print("-" * (len(terminals) - 1) * 44)
for i in parse_table:
    if i.name != "3":
        print(str(i).center(10), end="|")
        for j in terminals:
            if j.id != 'null':
                print("|", end="")
                try:
                    pr = ""
                    for k in parse_table[i][j]:
                        pr += str(k) + ","
                    print(pr[:-1].center(40), end="|")
                except Exception:
                    print("".center(40), end="|")
        print()

print("-" * (len(terminals) - 1) * 44)

if grammar.LL1:
    pass
else:
    print("Grammer is not LL(1) cannot parse")
'''
lex = LexicalAnalyser(
    [TokenIdentifier("flt", "float"),
     TokenIdentifier("int", "int"),
     TokenIdentifier("id", "[a-zA-Z][a-zA-Z0-9_]*")
     ],
    "int a,b,ab,ab_cd,ab09,a;float a,b;")
for i in range(10):
    try:
        # print("main -", lex.get_next_token().id, lex.get_next_token().lexeme)
        lex.get_next_token()
        pass
    except:
        print(None)
'''
