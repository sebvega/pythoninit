#recorriendo los elementos en un arreglo
numeros=[0,1,2,3,4,5,6,7,8,9,10]
for variable in numeros:
    print(variable)

#refcorriendo una lista y sus componetes
numerosTelefonicos={'contacto 1':32145642,'contacto 2':432143,'contacto 3':4321678754567}
for clave,valor in numerosTelefonicos.items():
    print('la clave es: '+str(clave)+ ' y el valor es: '+ str(valor))
    

#recorriendo una cadena de caracteres
mensaje='aprendiendo python'
for var in mensaje:
    print(var, end='')

# i=1 ; i<10
for var in range(1,10):
    print(var)