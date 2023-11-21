import os
os.system('cls')#Limpiar consola
#programa que trata temas de uso de cadenas
print("TRATAMIENTO DE CADENAS O STRING")
cadena="Compilador Python"
cadena1='Python es un Interprete'
cadena3='Netbeans y Intellij son IDES'
cadena2="""
PYTHON
======
1)LENGUAJE DE ALTO NIVEL
2)PUEDE TRABAJAR CON SU SHELL O CON IDES
3)POSEE LA CLASE STRING
4)STRING POSEE METODOS O INTERFACES DE COMUNICACION
"""
print(cadena)
print(cadena1)
print(cadena2)
print(cadena1.split())
print("Los primeros 10 caracteres :",cadena[:10])
print("Imprimir a partir del byte 11 :",cadena[11:])
#Imprimir caracter a caracter por medio de for
for byte in cadena:
    print(byte)
print(cadena3)
#Reemplazar un byte en una cadena con replace
print(cadena3.replace("y","e"))
#Ajustar un string en un formato de texto-> {}
texto="Mi {} se llama {} tiene {} años y ladra"
format("Guardiana","Fedora","diez")
print(texto)