#Aldo Jesu Samaniego Silva A00825779
#poner varias expresiones adentro de un parenteris 
import ply.lex as lex
import ply.yacc as yacc
import sys

tabla_simbolos = {}

tokens = [
    'procedure',
    'id',
    'is',
    'begin',
    'end',
    'function',
    'return',
    'main',
    'int',
    'float',
	'intv',
    'floatv',
    'not',
    'if',
    'then',
    'for',
    'loop',
    'exit',
    'when',
    'else',
    'in',

	'dospuntos',
	'puntocoma',
	'ap',
	'dp',
	'mas',
	'menos',
	'mult',
	'div',
	'and',
	'or',
	'less',
	'greater',
	'equal',
	'coma',
    'punto',
	'range'

]
t_dospuntos= r'\:'
t_puntocoma= r'\;'
t_ap= r'\('
t_dp= r'\)'
t_mas= r'\+'
t_menos= r'\-'
t_mult= r'\*'
t_div= r'\/'
t_less= r'\<'
t_greater= r'\>'
t_equal= r'\='
t_coma= r'\,'
t_punto= r'\.'

def t_procedure(t):
	r'procedure'
	t.type = 'procedure'
	return t


def t_is(t):
	r'is'
	t.type = 'is'
	return t

def t_begin(t):
	r'begin'
	t.type = 'begin'
	return t

def t_end(t):
	r'end'
	t.type = 'end'
	return t

def t_function(t):
	r'function'
	t.type = 'function'
	return t

def t_return(t):
	r'return'
	t.type = 'return'
	return t

def t_main(t):
	r'main'
	t.type = 'main'
	return t

def t_int(t):
	r'int'
	t.type = 'int'
	return t

def t_float(t):
	r'float'
	t.type = 'float'
	return t

def t_floatv(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_intv(t):
	r'\d+'
	t.value = int(t.value)
	return t	

def t_not(t):
	r'not'
	t.type = 'not'
	return t

def t_if(t):
	r'if'
	t.type = 'if'
	return t

def t_then(t):
	r'then'
	t.type = 'then'
	return t

def t_for(t):
	r'for'
	t.type = 'for'
	return t

def t_loop(t):
	r'loop'
	t.type = 'loop'
	return t

def t_exit(t):
	r'exit'
	t.type = 'exit'
	return t

def t_when(t):
	r'when'
	t.type = 'when'
	return t

def t_else(t):
	r'else'
	t.type = 'else'
	return t

def t_in(t):
	r'in'
	t.type = 'in'
	return t

def t_id(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = 'id'
	return t

def t_error(t):
	print("Illegal characters!")
	t.lexer.skip(1)
t_ignore  = ' \t'

lexer = lex.lex()

def p_S(p):
	'''
	S : V  PF MAIN
	'''
	print("\tCORRECTO")

def p_MAIN(p):
	'''
    MAIN : main is V begin ST end main puntocoma
	'''


def p_V(p):
	'''
	V : id dospuntos TIPO V
	| 
	'''

	

def p_TIPO(p):
	'''
	TIPO : int ASIGNINT puntocoma
	| float ASIGNFLOAT puntocoma
	'''
	if (tabla_simbolos.get(p[-2]) != None):
		print(p[-2])
		print("ya existe")
		sys.exit()
	else:
		tabla_simbolos[p[-2]]=p[1]
		print(tabla_simbolos)
def p_ASIGNINT(p):
	'''
	ASIGNINT : dospuntos equal VALINT
	| 
	'''

def p_ASIGNFLOAT(p):
    '''
	ASIGNFLOAT : dospuntos equal VALFLOAT
				|
    '''

def p_VALINT(p):
    '''
    VALINT : intv
	         | ARRAYINT
    '''

def p_VALFLOAT(p):
    '''
    VALFLOAT : floatv
				| ARRAYFLOAT
    '''

def p_ARRAYINT(p):
	'''
	ARRAYINT : ap COMINT dp
	| ap COMINT dp coma ap COMINT dp
	| ap COMINT dp coma ap COMINT dp coma ap COMINT dp
	|
	'''

def p_ARRAYFLOAT(p):
	'''
	ARRAYFLOAT : ap COMFLOAT dp
	| ap COMFLOAT dp coma ap COMFLOAT dp
	| ap COMFLOAT dp coma ap COMFLOAT dp coma ap COMFLOAT dp
	|
	'''

def p_COMINT(p):
	'''
    COMINT : intv
	| intv coma COMINT
    '''

def p_COMFLOAT(p):
	'''
    COMFLOAT : floatv
	| floatv coma COMFLOAT
    '''
	

#Revisar la instruccion 3 para opner una E adentro de otra E
def p_E(p):
	'''
	E : NUM OPER
	| ap E dp OPER
	'''

def p_NUM(p):
	'''
	NUM : id
	| intv
	| floatv
	'''

def p_OPER(p):
	'''
	OPER : mas E
	| menos E
	| mult E
	| div E
	| 
	'''

def p_PF(p):
	'''
	PF : P PF
	| F PF
	|
	'''
def p_P(p):
	'''
	P : procedure id is V begin ST end id puntocoma
	'''

def p_F(p):
	'''
	F : function id return TIPO is V begin ST return id end id puntocoma
	'''

def p_ST(p):
	'''
	ST : id ARRAYFLOAT dospuntos equal E puntocoma ST
	| if E then ST ELSE end if puntocoma ST
	| for id in id punto punto id loop ST end loop puntocoma ST
	| loop ST exit when E puntocoma end loop puntocoma ST
	|

    '''
def p_ELSE(p):
	'''
	ELSE : else ST
	|
	'''



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