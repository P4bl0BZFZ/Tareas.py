class Vehiculo:
    def __init__(self, patente, marca, modelo, valor):
        self.patente=patente
        self.marca=marca
        self.modelo=modelo
        self.valor=valor

class Menu:
    def __init__(self):
        self.vehiculos={}

    def menu(self):
        while True:
            print("   MENU DE CONTROL")
            print("---------------------")
            print("1. Ingreso de datos")
            print("2. Consulta de datos")
            print("3. Modificación de datos")
            print("4. Eliminación de datos")
            print("5. Despliegue de datos")
            print("6. Salir")
            opcion=input("Ingrese una opción: ")

            if opcion=="1":
                self.ingresar_datos()
            elif opcion=="2":
                self.consultar_datos()
            elif opcion=="3":
                self.modificar_datos()
            elif opcion=="4":
                self.eliminar_datos()
            elif opcion=="5":
                self.desplegar_contenido()
            elif opcion=="6":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def ingresarDatos(self):
        patente=input("Ingrese la patente del vehículo: ")
        marca=input("Ingrese la marca del vehículo: ")
        modelo=input("Ingrese el modelo del vehículo: ")
        valor=float(input("Ingrese el valor del vehículo: "))

        vehiculo=Vehiculo(patente, marca, modelo, valor)
        self.vehiculos[patente] = vehiculo
        print("Datos del vehículo ingresados correctamente.")

    def consultarDatos(self):
        patente=input("Ingrese la patente del vehículo a consultar: ")

        if patente in self.vehiculos:
            vehiculo=self.vehiculos[patente]
            print("Datos del vehículo:")
            print("Patente:", vehiculo.patente)
            print("Marca:", vehiculo.marca)
            print("Modelo:", vehiculo.modelo)
            print("Valor:", vehiculo.valor)
        else:
            print("No se encontró el vehículo con la patente ingresada.")

    def modificarDatos(self):
        patente = input("Ingrese la patente del vehículo a modificar: ")

        if patente in self.vehiculos:
            vehiculo=self.vehiculos[patente]
            print("Datos actuales del vehículo:")
            print("Patente:", vehiculo.patente)
            print("Marca:", vehiculo.marca)
            print("Modelo:", vehiculo.modelo)
            print("Valor:", vehiculo.valor)

            print("Ingrese los nuevos datos del vehículo:")
            marca=input("Ingrese la nueva marca del vehículo: ")
            modelo=input("Ingrese el nuevo modelo del vehículo: ")
            valor=float(input("Ingrese el nuevo valor del vehículo: "))

            vehiculo.marca=marca
            vehiculo.modelo=modelo
            vehiculo.valor=valor

            print("Datos del vehículo modificados correctamente.")
        else:
            print("No se encontró el vehículo con la patente ingresada.")

    def eliminarDatos(self):
        patente=input("Ingrese la patente del vehículo a eliminar: ")

        if patente in self.vehiculos:
            del self.vehiculos[patente]
            print("Vehículo eliminado correctamente.")
        else:
            print("No se encontró el vehículo con la patente ingresada.")

    def desplegarDatos(self):
        print("Contenido del diccionario de vehículos:")
        for patente, vehiculo in self.vehiculos.items():
            print("Patente:", vehiculo.patente)
            print("Marca:", vehiculo.marca)
            print("Modelo:", vehiculo.modelo)
            print("Valor:", vehiculo.valor)
            print()

menu=Menu()
menu.menu()
