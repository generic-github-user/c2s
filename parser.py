import lark
from lark import Lark
from lark.indenter import Indenter

with open('grammar.lark', 'r') as grammar:
    parser = Lark(grammar.read(), parser='lalr', lexer='contextual', debug=True)

with open('test.c2s', 'r') as f:
    parsed = parser.parse(f.read())
print(parsed.pretty()[:2000])

