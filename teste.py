from lexer import lexer
from parserr import parser

data = "6 + 10 (2 ** 4) - 42 / 2"

lexer.input(data)
for token in lexer:
    print(token)

result = parser.parse(data)
print(f"Resultado: {result}")