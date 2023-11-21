#Creacion de archivo de datos archivo en modo output
arch=open("datos.txt","w") #integracion fisico/logica
arch.write("Adrian\n")
arch.write("Bastian\n")
arch.write("Cecilia\n")
arch.write("Diana\n")
arch.write("Bryan\n")
arch.close()#Siempre cerrar archivo
print("Archivo creado con datos, verifique contenido!!!")
