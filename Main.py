from Library.TokenIdentifiersGenerator import TokenIdentifiersGenerator
from Library.GrammerGenerator import GrammarGenerator
import Library.Parser

# Create Token Identifiers
tig = TokenIdentifiersGenerator(open("Sources/Raw Tokens"))
tid_s = tig.token_identifiers()

# Create Grammer

gra_gen = GrammarGenerator(open("Sources/Raw Grammar"))
grammar = gra_gen.get_grammer()
for i in tid_s:
    print(i)
print(grammar.get_productions())
for i in grammar.get_productions():
    print(i)
