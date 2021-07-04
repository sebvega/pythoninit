class Usuario:
    #constructor
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def registrar(self):
        print('El usuario {} ha sido registrado'.format(self.nombre))

    def __str__(self):
        return 'El usuario se llama {} y su edad es {}'.format(self.nombre,self.edad)
    
class Empleado:
    def __init__(self, area_trabajo):
        self.area_trabajo=area_trabajo
    
    def generar_reporte(self):
        print(f'generando reporte del empleado del area de {self.area_trabajo}')


class Cliente(Usuario):
    def __init__(self, nombre, edad, numero_compras):
        super().__init__( nombre, edad)
        self.numero_compras=numero_compras

        #self.nombre=nombre
        #self.edad=edad
    def ver_compras():
        print(f'el numero de compras es {self.numero_compras}')
    
class Vendedor(Usuario, Empleado):
    def __init__(self, nombre, edad, numero_ventas, area_trabajo):
        Usuario.__init__(self, nombre, edad)
        Empleado.__init__(self, area_trabajo)
        self.numero_ventas=numero_ventas

        #self.nombre=nombre
        #self.edad=edad
    def ver_ventas():
        print(f'el numero de compras es {self.numero_compras}')

cliente=Cliente('lalo',30,22)
cliente.registrar()

vendedor=Vendedor('luis', 44,20, 'ventas')
vendedor.generar_reporte()

usuario= Usuario('pedro', 18)
usuario.registrar()
