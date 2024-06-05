import ply.lex as lex

# Diccionario de palabtas reservadas
palabras_reservadas = {
    
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOL',
    'string': 'STRING',
    
    'object': 'OBJECT',
    'class': 'CLASS',
    'void': 'VOID',
    'fun': 'FUN',
    
    'if': 'IF',
    'else': 'ELSE',
    
    'for': 'FOR',
    'while': 'WHILE',
    
    'or': 'OR',
    'and': 'AND',
    'not': 'NOT',
    'true': 'TRUE',
    'false': 'FALSE',

    
}
# Lista de tokens
tokens = [
    'PARENTESIS_APERTURA', 'PARENTESIS_CIERRE', 'LLAVE_APERTURA', 'LLAVE_CIERRE', 'CORCHETE_APERTURA', 'CORCHETE_CIERRE','RETURN',
    'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 
    'MENOR_QUE', 'MAYOR_QUE', 'IGUAL', 'MENOR_IGUAL', 'MAYOR_IGUAL',
    'ASIGNAR', 'PUNTO_COMA', 'COMA', 'COMILLAS_DOBLES',
    'ID','NUMERO_ENTERO', 'NUMERO_FLOTANTE', 'CADENA'
    
    
] + list(palabras_reservadas.values())

# Expresiones regulares para identificar los caracteres en el código
t_PARENTESIS_APERTURA = r'\('
t_PARENTESIS_CIERRE = r'\)'
t_LLAVE_APERTURA = r'\{'
t_LLAVE_CIERRE = r'\}'
t_CORCHETE_APERTURA = r'\['
t_CORCHETE_CIERRE = r'\]'

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'

t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_IGUAL = r'=='
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='

t_ASIGNAR = r'='
t_PUNTO_COMA = r';'
t_COMA = r','
t_COMILLAS_DOBLES = r'\"'

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_ignore = ' \t'

# Manejo de comentarios
def t_COMENTARIO_LINEA(t):
    r'//.*'
    t.lexer.lineno += t.value.count('\n')
    pass  # Ignorar comentarios de una sola línea

def t_COMENTARIO_BLOQUE(t):
    r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/'
    t.lexer.lineno += t.value.count('\n')
    pass  # Ignorar comentarios de múltiples líneas

# Métodos para iniciar la tokenización
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palabras_reservadas.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_NUMERO_FLOTANTE(t):
    r'[-]?\d+\.\d+?'
    t.value = float(t.value)
    return t

def t_NUMERO_ENTERO(t):
    r'[-]?\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
    r'\"([^\"\\]|\\.)*\"'
    t.value = t.value[1:-1]  # Eliminar comillas
    return t

errores = []

def t_error(t):
    mensaje_error = f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}, columna {find_column(t.lexer.lexdata, t)}"
    errores.append(mensaje_error)
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = -1
    return token.lexpos - last_cr

def analisis(cadena):
    lexer.input(cadena)  # Introducir la cadena de entrada al lexer
    tokens = []
    for tok in lexer:
        columna = find_column(cadena, tok)
        tokens.append({'value':tok.value, 'type':tok.type, 'line':tok.lineno, 'column':columna})
    return tokens, errores

if __name__ == '__main__':
    codigo = '''
    variableA(int) = 0;
    variableB(float) = 4.5;
    varibleC(string) = "Grass Compiler";

    if (variableA < variableB){

        while( variableA < variableB ){
            startRoute();
            goAhead();
            variableA = variableA + 0.5;
        }

        printMessage("El recorrido ha terminado");
    }else{
        printMessage("Valores inválidos para iniciar el recorrido");
    }
    '''
    resultado, errores = analisis(codigo)
    
    for token in resultado:
        print(token)
        
    if errores:
        print("Errores encontrados:")
        for error in errores:
            print(error)
