from collections import Counter

class Carrito:

    def __init__(self):
        self._productos = []
        self._total= 0

    def leer_codigo(self,producto,gondola,inventario,almacen,deposito):

        print(producto._get_marca())
        print(producto._get_nombre())

        if gondola._nombre_gondola=="alcohol":
            print(str(producto.litros()) + "lts")
            print("$" + str(producto._get_precio()))

        elif gondola._nombre_gondola=="carniceria":
            print(str(producto.peso()) + "kg")
            if producto._get_nombre().lower()=="asado":
                print("$" + str(producto._get_precio()) + "/kg")
            else:
                print("$" + str(producto._get_precio()))

        elif gondola._nombre_gondola=="galletitas":
            print(str(producto.gramos()) + "gr")
            print("$" + str(producto._get_precio()))
        
        elif gondola._nombre_gondola=="gaseosa":
            print(str(producto.litros()) + "lts")
            print("$" + str(producto._get_precio()))

        elif gondola._nombre_gondola=="golosinas":
            print(str(producto.gramos()) + "gr")
            print("$" + str(producto._get_precio()))

        elif gondola._nombre_gondola=="panaderia":
            if producto._get_nombre().lower()=="pan":
                print(str(producto.peso()) + "kg")
                print("$" + str(producto._get_precio()) + "/kg")
            print("$" + str(producto._get_precio()))

        elif gondola._nombre_gondola=="perfumeria":
            print(str(producto.cantidad()) + producto.unidad())
            print("$" + str(producto._get_precio()))

        elif gondola._nombre_gondola=="verduleria":
            print(str(producto.peso()) + "kg")
            print("$" + str(producto._get_precio()) + "/kg")

        a=producto._get_nombre().lower()
        stock_disponible = gondola._contador[a]

        if stock_disponible>0:
            print(f"Hay {stock_disponible} producto/s")
            consulta = input("¿Desea llevárselo? (si/no): ")
        

            while consulta != "si" and consulta != "no":
                print("Respuesta inválida. Escriba 'si' o 'no'.")
                consulta = input("¿Desea llevárselo? (si/no): ").lower()
                if consulta.lower()=="no":
                    break


            if consulta.lower() == "si":
                while True:
                    try:
                        cantidad = int(input("¿Cuántos?: "))

                        if cantidad <= 0:
                            print("No agregaste productos.")
                            break 

                        elif cantidad > stock_disponible:
                            print(f"No hay esa cantidad. Hay {stock_disponible}")

                        else:
                            break

                    except ValueError:
                        print("Ingrese un número válido.")

                for i in range(cantidad):
                    producto_eliminado = gondola.eliminar(producto,inventario,deposito)

                    if producto_eliminado != None:
                        self._productos.append(producto_eliminado)
                        self._total += producto_eliminado._get_precio()

                return "Lleva un total: $" + str(self._total)

            else:
                return "Producto no agregado."
            
            
        elif stock_disponible==0:
            print("No hay stock. Vuelva mas tarde.")
                  
    
    def _get_carro(self):
        return self._productos


# precio= "$"+ str(producto._get_precio())
            # self._productos.append(producto)
            # gondola.eliminar(producto)
            # self._total= self._total + producto._get_precio()
            # total= "Lleva un total de $"+ str (self._total)  
            # return producto._get_marca() + " " + producto._get_nombre() + " " + str (precio) + " " + str(total)