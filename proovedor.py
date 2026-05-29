from producto import Producto

class Proovedor:
    def __init__(self):
        pass

    def generar_pedido(self,producto):
        detalle = None

        if producto._get_gondola()._nombre_gondola.lower() == "alcohol":
            detalle = str(producto.litros()) + " lts"

        elif producto._get_gondola()._nombre_gondola.lower() == "gaseosa":
            detalle = str(producto.litros()) + " lts"

        elif producto._get_gondola()._nombre_gondola.lower() == "carniceria":
            detalle = str(producto.peso()) + " kg"

        elif producto._get_gondola()._nombre_gondola.lower() == "verduleria":
            detalle = str(producto.peso()) + " kg"

        elif producto._get_gondola()._nombre_gondola.lower() == "panaderia":
            if producto._get_nombre().lower() == "pan":
                detalle = str(producto.peso()) + " kg"

        elif producto._get_gondola()._nombre_gondola.lower() == "galletitas":
            detalle = str(producto.gramos()) + " gr"

        elif producto._get_gondola()._nombre_gondola.lower() == "golosinas":
            detalle = str(producto.gramos()) + " gr"

        elif producto._get_gondola()._nombre_gondola.lower() == "perfumeria":
            detalle = str(producto.cantidad()) + " " + producto.unidad()

        return (producto._get_gondola(),producto._get_codigo_barra(),producto._get_marca(),producto._get_nombre(),producto._get_precio(),detalle)

        
        



