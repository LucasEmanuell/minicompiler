import ply.lex as lex

tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EXPONENT',
    'LPAREN',
    'RPAREN',
]
#Expressões para cada token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXPONENT = r'\*\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+(\.\d+)?' # Expressão regular para números inteiros e decimais
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

t_ignore = ' \t\n' #Ignora quebra de linha e tabulacao e espaço 

def t_error(t):
    print(f"Caractere nao suportado: {t.value[0]}") #Mostra se vc usar algum caractere não reconhecido
    t.lexer.skip(1)

lexer = lex.lex()