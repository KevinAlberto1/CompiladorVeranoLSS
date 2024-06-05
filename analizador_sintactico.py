import ply.yacc as yacc

# Tokens contiene toda la información necesaria y palabras_reservadas podría servir para el analisis sintáctico
from analizador_lexico import tokens, palabras_reservadas


# Lista para almacenar errores de sintaxis
errores = []


# Precedencia de operadores (si es necesario)
precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
)

# Definición de la gramática
def p_programa(p):
    'programa : declaraciones'
    p[0] = ('programa', p[1])

def p_declaraciones(p):
    '''
    declaraciones : declaracion_variable declaraciones
                  | declaracion_variable
                  | declaracion_cad
    '''

def p_declaracion_cad(p):
    '''declaracion_cad : ID PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE ASIGNAR COMILLAS_DOBLES CADENA COMILLAS_DOBLES PUNTO_COMA'''

    
def p_declaracion_cad_e1(p):
    '''declaracion_cad : ID PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE ASIGNAR COMILLAS_DOBLES CADENA COMILLAS_DOBLES'''
    mensaje = "Error de sintaxis: Falta el punto y coma ';' al final de la declaración de variable"
    errores.append(mensaje)
def p_declaracion_cad_e2(p):
    '''declaracion_cad : PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE ASIGNAR COMILLAS_DOBLES CADENA COMILLAS_DOBLES PUNTO_COMA'''
    mensaje = "Error de sintaxis: Se esperaba un nombre de variable 'ID' válido antes del paretensis de apertura"
    errores.append(mensaje)
def p_declaracion_cad_e3(p):
    '''declaracion_cad : ID tipo_dato PARENTESIS_CIERRE ASIGNAR COMILLAS_DOBLES CADENA COMILLAS_DOBLES PUNTO_COMA'''
    mensaje = "Error de sintaxis: Se esperaba un '(' de apertura"
    errores.append(mensaje)
def p_declaracion_cad_e4(p):
    '''declaracion_cad : ID PARENTESIS_APERTURA PARENTESIS_CIERRE ASIGNAR COMILLAS_DOBLES CADENA COMILLAS_DOBLES PUNTO_COMA'''
    mensaje = "Error de sintaxis: Se esperaba un 'int', 'float', 'bool' o 'string'"
    errores.append(mensaje)
def p_declaracion_cad_e5(p):
    '''declaracion_cad : ID PARENTESIS_APERTURA tipo_dato ASIGNAR COMILLAS_DOBLES CADENA COMILLAS_DOBLES PUNTO_COMA'''
    mensaje = "Error de sintaxis: Se esperaba un ')' de cierre"
    errores.append(mensaje)    
def p_declaracion_cad_e6(p):
    '''declaracion_cad : ID PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE COMILLAS_DOBLES CADENA COMILLAS_DOBLES PUNTO_COMA'''
    mensaje = "Error de sintaxis: Falta el operador de asignación '='"
    errores.append(mensaje)
def p_declaracion_cad_e7(p):
    '''declaracion_cad : ID PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE ASIGNAR COMILLAS_DOBLES COMILLAS_DOBLES PUNTO_COMA'''
    mensaje = "Error de sintaxis: Se esperaba un número entero, flotante, una cadena de texto o un verdadero / falso"  
    errores.append(mensaje)
def p_declaracion_cad_e8(p):
    'declaracion_cad : ID PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE ASIGNAR CADENA COMILLAS_DOBLES PUNTO_COMA'
    mensaje = "Error de sintaxis: Se esperaban comillas dobles de apertura para cadena "  
    errores.append(mensaje)
def p_declaracion_cad_e9(p):
    'declaracion_cad : ID PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE ASIGNAR COMILLAS_DOBLES CADENA PUNTO_COMA'
    mensaje = "Error de sintaxis: Se esperaban comillas dobles de cierre "  
    errores.append(mensaje)
def p_declaracion_cad_e10(p):
    'declaracion_cad : ID PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE ASIGNAR COMILLAS_DOBLES CADENA caracteres_adicionales'
    mensaje = "Error de sintaxis: Se esperaban comillas dobles de cierre después de la cadena"
    errores.append(mensaje)

def p_caracteres_adicionales(p):
    '''caracteres_adicionales : caracteres_adicionales CADENA
                              | caracteres_adicionales NUMERO_ENTERO
                              | caracteres_adicionales NUMERO_FLOTANTE
                              | caracteres_adicionales ID
                              | caracteres_adicionales PUNTO_COMA
                              | caracteres_adicionales COMA
                              | caracteres_adicionales ASIGNAR
                              | CADENA
                              | NUMERO_ENTERO
                              | NUMERO_FLOTANTE
                              | ID
                              | PUNTO_COMA
                              | COMA
                              | ASIGNAR'''
    p[0] = p[1:]

def p_declaracion_variable(p):
    '''declaracion_variable : ID PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE ASIGNAR valor_dato PUNTO_COMA'''
    
def p_declaracion_variable_e1(p):
    '''declaracion_variable : ID PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE ASIGNAR valor_dato'''
    mensaje = "Error de sintaxis: Falta el punto y coma ';' al final de la declaración de variable"
    errores.append(mensaje)
def p_declaracion_variable_e2(p):
    '''declaracion_variable : PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE ASIGNAR valor_dato PUNTO_COMA'''
    mensaje = "Error de sintaxis: Se esperaba un nombre de variable 'ID' válido antes del paretensis de apertura"
    errores.append(mensaje)
def p_declaracion_variable_e3(p):
    '''declaracion_variable : ID tipo_dato PARENTESIS_CIERRE ASIGNAR valor_dato PUNTO_COMA'''
    mensaje = "Error de sintaxis: Se esperaba un '(' de apertura"
    errores.append(mensaje)
def p_declaracion_variable_e4(p):
    '''declaracion_variable : ID PARENTESIS_APERTURA PARENTESIS_CIERRE ASIGNAR valor_dato PUNTO_COMA'''
    mensaje = "Error de sintaxis: Se esperaba un 'int', 'float', 'bool' o 'string'"
    errores.append(mensaje)
def p_declaracion_variable_e5(p):
    '''declaracion_variable : ID PARENTESIS_APERTURA tipo_dato ASIGNAR valor_dato PUNTO_COMA'''
    mensaje = "Error de sintaxis: Se esperaba un ')' de cierre"
    errores.append(mensaje)    
def p_declaracion_variable_e6(p):
    '''declaracion_variable : ID PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE valor_dato PUNTO_COMA'''
    mensaje = "Error de sintaxis: Falta el operador de asignación '='"
    errores.append(mensaje)
def p_declaracion_variable_e7(p):
    '''declaracion_variable : ID PARENTESIS_APERTURA tipo_dato PARENTESIS_CIERRE ASIGNAR PUNTO_COMA'''
    mensaje = "Error de sintaxis: Se esperaba un número entero, flotante, una cadena de texto o un verdadero / falso"  
    errores.append(mensaje)


def p_tipo_dato(p):
    '''
    tipo_dato : INT
              | FLOAT
              | BOOL
              | STRING
    '''
    p[0] = p[1]
def p_valor_dato(p):
    '''
    valor_dato : NUMERO_ENTERO
               | NUMERO_FLOTANTE
               | TRUE
               | FALSE
    '''
    p[0] = p[1]



# Manejo de errores de sintaxis
def p_error(p):
    print("Error de sintaxis en '%s'" % p.value if p else "Error de sintaxis en EOF")

# Construir el analizador sintáctico
parser = yacc.yacc()


# Función para realizar el análisis sintáctico
def analisis_sintactico(cadena):
    return parser.parse(cadena)

def recolectar_declaraciones(tree):
    if not tree:
        return []
    if tree[0] == 'declaracion':
        return [tree[1:]]
    else:
        return sum((recolectar_declaraciones(child) for child in tree[1:]), [])


# Armar arbol sintactico:
# def imprimir_arbol(nodo, nivel=0):
#     if isinstance(nodo, tuple):
#         print('  ' * nivel + nodo[0])
#         for elemento in nodo[1:]:
#             imprimir_arbol(elemento, nivel + 1)
#     else:
#         print('  ' * nivel + str(nodo))

if __name__ == '__main__':
    codigo = '''
    
    variableG(string) = "wasa ;
    
    ''' 
    
    # variableB(float) = 4.5;
    # varibleC(string) = "Grass Compiler";

    # if (variableA < variableB){

    #     while( variableA < variableB ){
    #         startRoute();
    #         goAhead();
    #         variableA = variableA + 0.5;
    #     }

    #     printMessage("El recorrido ha terminado");
    # }else{
    #     printMessage("Valores inválidos para iniciar el recorrido");
    # }
    
    resultado = analisis_sintactico(codigo)
    declaraciones = recolectar_declaraciones(resultado)
    print("Declaraciones:")
    for dec in declaraciones:
        print(dec)

    print("Errores encontrados:")
    for error in errores:
        print(error)