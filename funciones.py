def mi_funcion(parametro1,parametro2):
    print(parametro1, parametro2)

def mi_funcion2(parametro1,parametro2='sin parametros'):
    print(parametro1, parametro2)

def mi_funcion3(parametro1,parametro2,*otrosvalores):
    print(otrosvalores)

def mi_funcion4(parametro1,parametro2,**diccionarios):
    print(diccionarios)
    print(diccionarios['nombre'])

def asignar_valor (x,y):
    x=x+1
    y=y+1
    return x,y

mi_funcion('hola',0)
mi_funcion2('hola')
mi_funcion3('hola',' mundo','doble')
mi_funcion4('hola',' mundo',nombre='pablo',apellido='cifuentes')
print(asignar_valor(4,5))