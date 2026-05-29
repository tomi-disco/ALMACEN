from collections import Counter

class Gondola:

    def __init__(self,nombre_gondola,umbral):
        self._nombre_gondola=nombre_gondola.lower()
        self._stock=[]
        self._contador=Counter()
        self._umbral=umbral
        

    def agregar(self,producto):
        if producto._get_gondola()._nombre_gondola.lower()==self._nombre_gondola:
            self._stock.append(producto)
            self._contador[producto._get_nombre().lower()] += 1


    def eliminar(self,producto,inventario,deposito):
        if self._contador[producto._get_nombre().lower()]>=1:
            for prod in self._stock:
                if prod._get_nombre().lower() == producto._get_nombre().lower():
                    self._stock.remove(prod)
                    self._contador[producto._get_nombre().lower()] -= 1

                    if self._contador[producto._get_nombre().lower()] == 0:
                        inventario.reponer_gondola(producto,self,deposito)       

                    return prod

        else:
            #print("La gondola esta vacia.")
            inventario.reponer_gondola(producto,self,deposito) 
            return None
            


    def mostrar_stock(self):
        print("Stock de " + self._nombre_gondola)

        for nombre, cantidad in self._contador.items():
            print("Hay " + str(cantidad) + " de " + nombre)

    def _get_umbral(self):
        return self._umbral


   