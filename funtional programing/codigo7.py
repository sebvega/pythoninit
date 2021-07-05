from functools import reduce


lista=['h','o','l','a']

def unir(x,y):
    return x + y

print(reduce(unir,lista))
