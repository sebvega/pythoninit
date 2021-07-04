mi_diccionario={
    'hola':'hello','rojo':'red','libro':'book'
}
print(mi_diccionario)

# modificar elemento por medio de la llave
mi_diccionario['rojo']='blue'
print(mi_diccionario)

# del elimina elementos de un diccionario por medio de la llave
del(mi_diccionario['hola'])
print(mi_diccionario)

estudiante1={'Nombre':'Juan',
'Apellido':'Rodrigez',
'edad':24,
'cursos':[
    {'nombreCurso':'Python','nivel':'basico'},
    {'nombreCurso':'Java','nivel':'intermedio'},
    {'nombreCurso':'Php','nivel':'avanzado'}
    ]
    }

estudiante2={'Nombre':'Juan',
'Apellido':'Rodrigez',
'edad':20,
'cursos':[
    {'nombreCurso':'Python','nivel':'basico'},
    {'nombreCurso':'Java','nivel':'intermedio'},
    {'nombreCurso':'Php','nivel':'avanzado'}
    ]
    }
    
    #append agrega a una nueva lista elementos que se deseen agregar, ya sea un entero o un objeto o una nueva lista dentro de la lista, asi concatenando un sin fin de listas


estudiantes=[]
estudiantes.append(estudiante1)
estudiantes.append(estudiante2)

#print(estudiantes)

print(estudiantes[0]['cursos'])