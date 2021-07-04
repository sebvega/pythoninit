conjunto={1,2,3}
conjunto.add('pablito')
conjunto.add('B')
print(conjunto)

existe='B'in conjunto
print(existe)

lista_convertida=list(conjunto)

# set() no e pueden repetir elementos en un conjuto por lo que el 2 no se agrega en el conjunto porque ya existe en el conjunto, pero si en la lista
lista_convertida.append(2)
conjunto.add(2)

print(lista_convertida)
print(conjunto)

#ejemplo de un conjunto set() convierte en conjunto una cadena de caracteres,
# pero como hay elementos que se repiten estos solo los guarda una vez y no respeta el orden
prueba='anita lava la tina'
print(set(prueba))



# discard
conjunto.discard('B')
print(conjunto)

conjunto.clear()
print(conjunto)