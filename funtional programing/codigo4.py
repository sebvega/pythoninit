numeros=[1,2,3,4,5]
#def duplicar (num):
 #   return num*2

duplicar=lambda num:num*2

duplicados=list(map(duplicar, numeros))
print(duplicados)

lista1=[1,2,3,4,5]
lista2=[1,1,1,1,1]

suma = list(map(lambda l1, l2 : l1 + l2, lista1, lista2))
print(suma)