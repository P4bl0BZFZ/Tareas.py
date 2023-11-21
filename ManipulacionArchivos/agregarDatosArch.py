#apertura de archivo de datos para append en modo output
arch=open("datos.txt","a")
arch.write("Zara\n")
arch.write("Waldo\n")
arch.write("Sabrina\n")
arch.close()
print("Escritura como addendum finalizada!!!")
arch=open("datos.txt","r")
contenido=arch.read()
print(contenido)
arch.close()#Siempre cerrar archivo
print("Lectura de Archivo finalizada!!!")

arch=open("datos.txt","r")
lineas=arch.readlines()
print("El archivo contiene :",len(lineas)," registros")
arch.close()
