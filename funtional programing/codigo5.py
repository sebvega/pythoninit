numeros=[1,2,3,4,5]

def numeros_pares(lista):
    n_pares=[]
    for numero in numeros:
        if numero%2==0:
            n_pares.append(numero)
    return n_pares

pares=numeros_pares(numeros)
print(numeros)
print(pares)