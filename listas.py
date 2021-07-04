lista_combinada=['hola',0,12.2,True,'bienvenido', 'hola']
print(lista_combinada)

nueva_lista=[[1,2,3,],[4,5,6],[7,8,9]]
print(nueva_lista[1][1])

#comando append agrega lo que sea en una lista
nueva_lista.append(lista_combinada)
print(nueva_lista)

# insert agrega elementos en un listado en la N posicion los que se dea agregar
lista_combinada.insert(0,'dato lo que sea')
print(lista_combinada)

# pop elimina elementos dentro de una lista
lista_combinada.pop(0)
print(lista_combinada)

# remove es por el elemento
lista_combinada.remove('bienvenido')
print(lista_combinada)

# len es el length para obtener la longitud de una lista
print(len(lista_combinada))

hola="holaaa"
print(len(hola))

# count cuenta las veces que hay un elemento en una lista
print(lista_combinada.count('hola'))

# index encuentra la posicion en la que se se encuentra el elemento
print(lista_combinada.index(True))
