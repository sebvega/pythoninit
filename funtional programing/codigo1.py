def duplicar(num):
    return num*2

def suma(num1,num2):
    return num2+num1

def mostrar_mensaje(mensaje):
    return f'su mensaje es {mensaje}'

def numero_par(num):
    return num%2==0

es_par=numero_par(4)
print(es_par)
mensajero=mostrar_mensaje('hola mundo')
print(mensajero)
sumado=suma(2, 4)
print(sumado)
duplicado=duplicar(2)
print(duplicado)