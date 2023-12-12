import ply.yacc as yacc
from lexer import tokens

def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | term
    '''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        else:
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]
#Define uma expressão matemática que pode ser composta por termos conectados por operadores de adição ou subtração.

def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
         | factor
    '''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        else:
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]
#Define um termo que pode ser composto por fatores conectados por operadores de multiplicação, divisão ou apenas um fator.
def p_factor(p):
    '''
    factor : base EXPONENT factor
           | base
    '''
    if len(p) == 4:
        p[0] = p[1] ** p[3]
    else:
        p[0] = p[1]
#Define um fator que pode ser uma base elevada a um expoente ou simplesmente uma base.
def p_base(p):
    '''
    base : NUMBER
         | LPAREN expression RPAREN
    '''
    if p[1] == '(':
        p[0] = p[2]
    else:
        p[0] = p[1]
#Define uma base que pode ser um número ou uma expressão entre parênteses.
def p_error(p):
    print(f"Erro de sintaxe em '{p.value}'")
#Mostra o erro.
parser = yacc.yacc()
