numeros=[1,2,3,4,5]

def duplicar(lista):
    numero_duplicados=[]
    for numero in numeros:
        numero_duplicados.append(numero*2)
    return numero_duplicados

duplicados=duplicar(numeros)
print(duplicados)