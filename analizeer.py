#Aldo Jesu Samaniego Silva A00825779
#poner varias expresiones adentro de un parenteris 
import ply.lex as lex
import ply.yacc as yacc
import sys

tabla_simbolos = {}
pila_operandos=[]
pila_cuadruplos=[]
pila_saltos=[]
avail_temporales=["T1","T2","T3","T4","T5","T6","T7","T8","T9","T10"]
contador=[]
contador.append(0)

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

def p_ASIGNINT(p):
	'''
	ASIGNINT : dospuntos equal VALINT
	| 
	'''
	if(len(p)==1):
		if (tabla_simbolos.get(p[-3]) != None):
			print(p[-3])
			print("ya existe")
			sys.exit()
		else:
			tabla_simbolos[p[-3]]=[p[-1],int(0)]
			print(tabla_simbolos)

def p_ASIGNFLOAT(p):
	'''
	ASIGNFLOAT : dospuntos equal VALFLOAT
	|
    '''
	if(len(p)==1):
		if (tabla_simbolos.get(p[-3]) != None):
			print(p[-3])
			print("ya existe")
			sys.exit()
		else:
			tabla_simbolos[p[-3]]=[p[-1],float(0)]
			print(tabla_simbolos)


def p_VALINT(p):
	'''
	VALINT : intv
	| ARRAYINT
	'''
	if (tabla_simbolos.get(p[-5]) != None):
		print(p[-5])
		print("ya existe")
		sys.exit()
	else:
		tabla_simbolos[p[-5]]=[p[-3],p[1]]
		print(tabla_simbolos)

def p_VALFLOAT(p):
	'''
	VALFLOAT : floatv
	| ARRAYFLOAT
	'''
	if (tabla_simbolos.get(p[-5]) != None):
		print(p[-5])
		print("ya existe")
		sys.exit()
	else:
		tabla_simbolos[p[-5]]=[p[-3],p[1]]
		print(tabla_simbolos)

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
	E : E mas T
	| E menos T
	| T
	'''
	if (len(p) >3):
		print(p[2])
		op2=pila_operandos[-1]
		pila_operandos.pop()
		op1=pila_operandos[-1]
		pila_operandos.pop()
		temp=avail_temporales[0]
		avail_temporales.pop(0)
		pila_cuadruplos.append([p[2],op1,op2,temp])
		contador[0]+=1
		pila_operandos.append(temp)
		print(pila_operandos)
		print(pila_cuadruplos)

def p_T(p):
	'''
	T : T mult FE
	| T div FE
	| FE
	'''
	if (len(p) >3):
		print(p[2])
		op2=pila_operandos[-1]
		pila_operandos.pop()
		op1=pila_operandos[-1]
		pila_operandos.pop()
		temp=avail_temporales[0]
		avail_temporales.pop(0)
		pila_cuadruplos.append([p[2],op1,op2,temp])
		contador[0]+=1
		pila_operandos.append(temp)

		print(pila_operandos)
		print(pila_cuadruplos)


def p_FE(p):
	'''
	FE : NUM
	| ap E dp
	'''

def p_NUM(p):
	'''
	NUM : id
	| intv
	| floatv
	'''
	if(type(p[1]) is str):
		print("gols")
		if (tabla_simbolos.get(p[1]) == None):
			print(p[1])
			print("no existe")
			sys.exit()
		else:
			pila_operandos.append(p[1])
	else:
		pila_operandos.append(p[1])

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
	ST : ASIG ST
	| if E then THEN ST ELSE end END if puntocoma ST
	| for id in id punto punto id loop ST end loop puntocoma ST
	| loop LOOP ST exit when E JUMP puntocoma end loop puntocoma ST
	|
    '''

def p_LOOP(p):
	'''
	LOOP : 
	'''
	print("LOOP")
	pila_saltos.append(contador[0])

def p_JUMP(p):
	'''
	JUMP : 
	'''
	aux=pila_saltos[-1]
	pila_saltos.pop()
	res_exp=pila_operandos[-1]
	pila_operandos.pop()
	avail_temporales.append(res_exp)
	pila_cuadruplos.append(["gtt",res_exp,aux])
	

def p_THEN(p):
	'''
	THEN : 
	'''
	print("adentro then")
	res_exp=pila_operandos[-1]
	pila_operandos.pop()
	avail_temporales.append(res_exp)
	pila_cuadruplos.append(["gtf",res_exp])
	print(pila_cuadruplos)
	contador[0]+=1
	pila_saltos.append(contador[0]-1)

def p_END(p):
	'''
	END : 
	'''
	aux=pila_saltos[-1]
	pila_saltos.pop()
	tmp=pila_cuadruplos[aux]
	tmp.append(contador[0])
	pila_cuadruplos[aux]=tmp



def p_ASIG(p):
	'''
	ASIG : id ARRAYFLOAT dospuntos equal E puntocoma
    '''
	pila_cuadruplos.append(["=",pila_operandos[-1],p[1]])
	contador[0]+=1
	pila_operandos.pop()
	print(pila_operandos)
	print(pila_cuadruplos)

def p_ELSE(p):
	'''
	ELSE : else HELPERELSE ST
	|
	'''

def p_HELPERELSE(p):
	'''
	HELPERELSE : 
	'''
	print("adentro else")
	pila_cuadruplos.append(["goto"])
	print(pila_cuadruplos)
	contador[0]+=1
	print(pila_saltos)
	aux=pila_saltos[-1]
	pila_saltos.pop()
	tmp=pila_cuadruplos[aux]
	tmp.append(contador[0])
	pila_cuadruplos[aux]=tmp
	pila_saltos.append(contador[0]-1)



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