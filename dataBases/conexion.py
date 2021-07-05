import sqlite3
from sqlite3 import Error

def conectar():
    try:
        conexion= sqlite3.connect('database.db')
        print('se ha conectado a la base de datos correctamente')
        return conexion
    except Error:
        print('ha ocurrido un error')

def crearTabla(conexion):
    cursor=conexion.cursor()
    sentenciaSQL='''CREATE TABLE IF NOT EXISTS usuario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL)'''
    cursor.execute(sentenciaSQL)
    conexion.commit()
    conexion.close()
    
def insertarDatos(conexion,datos):
    cursor=conexion.cursor()
    sentenciaSQL='INSERT INTO usuario (nombre, apellido) VALUES (?, ?)'
    cursor.executemany(sentenciaSQL,datos)
    conexion.commit()
    conexion.close()

def consultar(conexion):
    cursor=conexion.cursor()
    sentenciaSQL=' SELECT * FROM usuario'
    cursor.execute(sentenciaSQL)
    datos=cursor.fetchall()
    conexion.close()
    return datos

def consultarPorId(conexion,id):
    cursor=conexion.cursor()
    sentenciaSQL=' SELECT * FROM usuario WHERE id=?'
    cursor.execute(sentenciaSQL,(id,))
    datos=cursor.fetchall()
    conexion.close()
    return datos

def editar(conexion,id, nombre,apellido):
    cursor=conexion.cursor()
    sentenciaSQL='UPDATE usuario SET nombre=?, apellido=? WHERE id=?'
    cursor.execute(sentenciaSQL,(nombre,apellido,id))
    conexion.commit()
    conexion.close()

def eliminar(conecion,id):
    cursor=conexion.cursor()
    sentenciaSQL='DELETE FROM usuario WHERE id=?'
    cursor.execute(sentenciaSQL,(id,))
    conexion.commit()
    conexion.close()

conexion=conectar()
#crearTabla(conexion) 

datos=[('pablo','espinoza'),('lola','drones')]
#insertarDatos(conexion, datos)
#dato=consultar(conexion)
#for d1 in dato:
#    print(d1[1]+' '+d1[2])
    


'''id=3
datos=consultarPorId(conexion, id)
if len(datos)>0:
    print(datos[0][1]+' '+datos[0][2])
else:
    print('no se encontro el usuario')'''

editar(conexion, 2, 'juan', 'juanito')