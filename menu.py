from inicializador import *

def menu():
    while True:
        try:
            mostrar_menu_principal()
            opcion=input("Ingrese a que gondola quiere ir: ")
            if opcion.lower()== "a":
                mostrar_producto(productos_alcohol)
            elif opcion.lower()== "b":
                mostrar_producto(productos_carniceria)
            elif opcion.lower()== "c":
                mostrar_producto(productos_galletitas)
            elif opcion.lower()== "d":
                mostrar_producto(productos_gaseosa)
            elif opcion.lower()== "e":
                mostrar_producto(productos_golosinas)
            elif opcion.lower()== "f":
                mostrar_producto(productos_panaderia)
            elif opcion.lower()== "g":
                mostrar_producto(productos_perfumeria)
            elif opcion.lower()== "h":
                mostrar_producto(productos_verduleria)
            elif opcion.lower()== "i":
                ver_stock()
            # elif opcion.lower()=="j":
            #     pass
            #     #eliminar
            elif opcion.lower()=="k":
                total()


        except ValueError:
            print("Ingrese una entrada valida.")
