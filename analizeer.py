#Aldo Jesu Samaniego Silva A00825779
#Preguntar sobre := poner varias expresiones adentro de un parenteris y lo de procedure main
import ply.lex as lex
import ply.yacc as yacc

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
    'vectint',
    'vectfloat',
    'matint',
    'matfloat',
    'cubint',
    'cubfloat',
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
def t_id(t):
	r'id'
	t.type = 'id'
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

def t_vectint(t):
	r'vectint'
	t.type = 'vectint'
	return t

def t_vectfloat(t):
	r'vectfloat'
	t.type = 'vectfloat'
	return t

def t_matint(t):
	r'matint'
	t.type = 'matint'
	return t

def t_matfloat(t):
	r'matfloat'
	t.type = 'matfloat'
	return t

def t_cubint(t):
	r'cubint'
	t.type = 'cubint'
	return t

def t_cubfloat(t):
	r'cubfloat'
	t.type = 'cubfloat'
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
    V : 
	V : id dospuntos TIPO ASIGN puntocoma V
	'''
'''
def p_TIPO(p):

    TIPO : int
    TIPO : float
    TIPO : vectint
    TIPO : vectfloat
    TIPO : matint
    TIPO : matfloat
    TIPO : cubint
    TIPO : cubfloat

'''
def p_TIPO(p):
    '''
    TIPO : int
    TIPO : float
    '''

def p_ASIGN(p):
    '''
    ASIGN : 
	ASIGN : dospuntos equal VAL
    '''

def p_VAL(p):
    '''
    VAL : E
	VAL : ARRAY
    '''

def p_ARRAY(p):
	'''
    ARRAY : 
	ARRAY : ap COM dp
	ARRAY : ap COM dp coma ap COM dp
	ARRAY : ap COM dp coma ap COM dp coma ap COM dp
	'''
def p_COM(p):
	'''
    COM : E
    COM : E coma COM
    '''

#Revisar la instruccion 3 para opner una E adentro de otra E
def p_E(p):
	'''
	E : id
    E : not id
	E : ap E OPER E dp 
    E : id OPER id
	'''

def p_OPER(p):
	'''
	OPER : mas
    OPER : menos
    OPER : mult
    OPER : div
    OPER : less
    OPER : greater
    OPER : equal
    OPER : and
    OPER : or
    '''

def p_PF(p):
	'''
    PF : 
	PF : P PF
    PF : F PF
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
	ST :
	ST : id ARRAY dospuntos equal E puntocoma ST
	ST : if E then ST ELSE end if puntocoma ST
    ST : for id in id punto punto id loop ST end loop puntocoma ST
    ST : loop ST exit when E puntocoma end loop puntocoma ST

    '''
def p_ELSE(p):
	'''
	ELSE :
	ELSE : else ST
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