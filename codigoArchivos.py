# apre un archivo es su direccion de referencia y sus permisos de lectura y escritura
archivo=open('archivo.txt','r')

# lee solamente una linea del archivo
#print(archivo.readline())

#lee todo el archivo
#print(archivo.read())

# es un ciclo for para leer todo el archivo
for linea in archivo:
    print(linea, end='')

#cierra el archivo para liberar menoria y esfuerzo
archivo.close()

#reemplaza todo el archivo
#archivo=open('archivo.txt', 'w')

#adrega texto desde donde se dejo
archivo=open('archivo.txt', 'a')
archivo.write('texto desde python')

for linea in range(1,11):
    archivo.write('\nTexto: '+str(linea))

archivo.close