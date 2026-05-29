from collections import Counter

class Almacen:

    def __init__(self):
        pass

    def descuento_galletas(self,carrito):
        descuento=0
        cont_galletas= Counter()
        precio_galletas={}

        for producto in carrito._get_carro():
            if producto._get_gondola().lower()=="galletitas":
                cont_galletas[producto._get_nombre().lower()] += 1
                precio_galletas[producto._get_nombre().lower()] = producto._get_precio()


        for nombre in cont_galletas:
            cantidad = cont_galletas[nombre]
            precio = precio_galletas[nombre]

            pares = cantidad // 2
            descuento += pares * precio   

        return descuento
        
    
    def descuento_bebidas(self,carrito):
        descuento = 0
        cont_bebidas = Counter()
        precio_bebidas = {}

        for producto in carrito._get_carro():
            if producto._get_gondola().lower() == "gaseosa" or producto._get_gondola().lower()== "alcohol":
                marca = producto._get_marca().lower()
                cont_bebidas[marca] += 1
                precio_bebidas[marca] = producto._get_precio()

        for marca in cont_bebidas:
            cantidad = cont_bebidas[marca]
            precio = precio_bebidas[marca]

            pares = cantidad // 2
            descuento += pares * precio * 0.30

        return descuento
    
    def descuento_perfumeria(self,carrito):
        descuento=0

        for producto in carrito._get_carro():
            if producto._get_gondola().lower()== "perfumeria":
                descuento+= producto._get_precio() *0.5

        return descuento
    
    def total_a_pagar(self,carrito):
        total=carrito._total - self.descuento_bebidas(carrito) - self.descuento_galletas(carrito) - self.descuento_perfumeria(carrito)
        return total

    
