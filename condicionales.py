
numero1=4
numero2=5
condicion=numero1+numero2

if condicion==9:
    print('se cumple la condicion')
else:
    numero1=input('ingrese el primer numero: ')
    numero2=input('ingrese el segundo numero: ')
    condicion=int(numero2)+int(numero1)
    if condicion==9:
        print('por finnnn!!!!')
    else:
        print('no se cumple la condicion')

numero_ing=input('ingrese un num: ')
if numero_ing=='1':
    print('ingresaste el 1')
elif numero_ing =='2':
    print('ingresaste el 2')
elif numero_ing =='3':
    print('ingresaste el 3')
else: 
    print('no ingresaste los numero esperados')


if numero_ing=='1'or'2'or'3':
    print('ingresaste el {}'.format(numero_ing))
else: 
    print('no ingresaste los numero esperados')

