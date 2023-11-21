#Lectura de archivo de datos archivo en modo input
arch=open("datos.txt","r")
contenido=arch.read()
print(contenido)
arch.close()#Siempre cerrar archivo
print("Lectura de Archivo finalizada!!!")
