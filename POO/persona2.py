class Usuario:
    #constructor
    def __init__(self):
        self.__nombre='ana'
        self.__edad=23

    #geter and seter

    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad

    def setNombre(self, nombre):
        if nombre== 'ana':
            self.__nombre=nombre
        else:
            return 'no se puede asignar ese nombre'

    def setEdad(self, edad):
        if edad== 23:
            self.__edad=edad
        else:
            return 'no se puede asignar esa edad'

    def __registrar(self):
        print('El usuario {} ha sido registrado'.format(self.__nombre))

    def __str__(self):
        return 'El usuario se llama {} y su edad es {}'.format(self.__nombre,self.__edad)
    
    def consultarTipo(self):
        self.__registrar()
        print('sin especificar')

#usuario=Usuario('benito', 13)
#print(usuario.nombre)
#print(usuario.edad)
usuario=Usuario()
print(usuario.getNombre())
print(usuario.getEdad())


#usuario.consultarTipo()