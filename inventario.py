class Inventario:

    def __init__(self,proovedor):
        self._gondolas = []
        self._proovedor=proovedor

    def agregar_gondola(self, gondola):
        self._gondolas.append(gondola)

    def reponer_gondola(self,producto,gondola,deposito):
        a=(gondola._get_umbral())*2
        for i in range(a):
            aux=deposito.eliminar(producto)
            if aux !=0:
                gondola.agregar(aux)
            else:
                self.contactar(producto,gondola,deposito)
                break

        #return self._deposito.eliminar(producto)

    def mostrar_stock(self):
        for gondola in self._gondolas:
            print("Stock de " + gondola._nombre_gondola)

            for nombre, cantidad in gondola._contador.items():
                print("Hay " + str(cantidad) + " de " + nombre)

            print("-----------------")

    def contactar(self,producto,gondola,deposito):
        print("Contactando proveedor para reponer " + producto._get_nombre())
        a=(gondola._get_umbral())*2
        for i in range(a):
            self._proovedor.generar_pedido(producto)
            deposito.agregar(producto)

        

        
        

        
    