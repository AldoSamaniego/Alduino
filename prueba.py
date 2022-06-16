#Aldo Jesu Samaniego Silva A00825779
#Preguntar sobre := poner varias expresiones adentro de un parenteris y lo de procedure main
import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'id'
]


def t_id(t):
	r'id'
	t.type = 'id'
	return t

def t_error(t):
	print("Illegal characters!")
	t.lexer.skip(1)
t_ignore  = ' \t'

lexer = lex.lex()

def p_S(p):
	'''
	S : id
	'''
	print("\tCORRECTO")


def p_error(p):
	print("\tINCORRECTO")

parser = yacc.yacc()
newline_break = ""
with open("text.txt", "r") as file:
    for readline in file: 
        line_strip = readline.strip()
        newline_break += ' ' +line_strip
print(newline_break)

parser.parse(newline_break)