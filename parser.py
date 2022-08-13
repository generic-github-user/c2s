import lark
from lark import Lark
from lark.indenter import Indenter

with open('grammar.lark', 'r') as grammar:
    parser = Lark(grammar.read(), parser='earley', lexer='dynamic', debug=True)

class Token:
    def __init__(self, source, parent=None):
        self.parent = parent
        self.source = source
        for attr in 'type value line column'.split():
            setattr(self, attr, getattr(self.source, attr))
            self.length = len(self.source)

    def text(self): return self.value

    def __str__(self):
        return f'Token <{self.type}, {self.line}:{self.column}> {self.value}'

class Node:
    def __init__(self, source, parent=None, depth=0, root=None):
        self.parent = parent
        self.root = root if root else self
        self.children = []
        self.source = source

        self.meta = self.source.meta
        self.type = self.source.data
        self.depth = depth
        for c in self.source.children:
            if isinstance(c, lark.Tree): self.children.append(
                    Node(c, self, self.depth+1, root=self.root if self.root else self))
            elif c is None: self.children.append(c)
            else:
                assert isinstance(c, lark.Token), c
                self.children.append(Token(c))

    def text(self):
        return ''.join(c.text() for c in self.children)

    def __str__(self):
        return f'Node <{self.type}> ({self.depth})' + '\n' + '\n'.join('  '*self.depth + str(n) for n in self.children)

with open('test.c2s', 'r') as f:
    parsed = parser.parse(f.read())
print(parsed.pretty()[:2000])

