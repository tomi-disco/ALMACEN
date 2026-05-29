class Proovedor:
    def __init__(self):
        pass

    def generar_pedido(self,producto):
        detalle = None
        p=producto._get_gondola()._nombre_gondola.lower()

        if p == "alcohol":
            detalle = str(producto.litros()) + " lts"

        elif p == "gaseosa":
            detalle = str(producto.litros()) + " lts"

        elif p == "carniceria":
            detalle = str(producto.peso()) + " kg"

        elif p == "verduleria":
            detalle = str(producto.peso()) + " kg"

        elif p == "panaderia":
            if producto._get_nombre().lower() == "pan":
                detalle = str(producto.peso()) + " kg"

        elif p == "galletitas":
            detalle = str(producto.gramos()) + " gr"

        elif p == "golosinas":
            detalle = str(producto.gramos()) + " gr"

        elif p == "perfumeria":
            detalle = str(producto.cantidad()) + " " + producto.unidad()

        return (p,producto._get_codigo_barra(),producto._get_marca(),producto._get_nombre(),producto._get_precio(),detalle)

        
        



