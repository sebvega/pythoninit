numero1=input('ingrese el numero 1: ')
numero2=input('ingrese el numero 2: ')
try:
    suma= int(numero1)+int(numero2)
    print(suma)
except:
    print('a ocurrido un error')

try:
    division=int(numero1)/int(numero2)
    print(division)
except ZeroDivisionError:
    print('no se puede dividir en cero')
except:
    print('ingrese los numeros correctos')
finally:
    print('finalizado el programa')


print('------------------------------------')
try:
    print(nombre)
except NameError:
    print('debe declarar la variable')

try:
    numero=2
    texto='hola'
    suma=numero+texto
except TypeError as error:
    print('el error es: '+str(error))