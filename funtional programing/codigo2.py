duplicado=lambda num: num*2
sumado=lambda num1,num2: num1+num2
mensajero=lambda mensaje: f'su mensaje es {mensaje}'
es_par=lambda num: num%2==0

print(es_par(4))
print(mensajero('hola mundo'))
print(sumado(2,4))
print(duplicado(2))