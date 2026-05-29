from collections import Counter

class Deposito:
    def __init__(self,nombre_deposito,umbral):
        self._nombre_deposito=nombre_deposito.lower()
        self._stock=[]
        self._contador=Counter()
        self._umbral=umbral

    def agregar(self,producto):
        if producto._get_gondola()._nombre_gondola.lower()==self._nombre_deposito:
            self._stock.append(producto)
            self._contador[producto._get_nombre().lower()]+=1

    def eliminar(self,producto):
        if self._contador[producto._get_nombre().lower()]>=1:
            for prod in self._stock:
                if prod._get_nombre().lower() == producto._get_nombre().lower():
                    self._stock.remove(prod)
                    self._contador[producto._get_nombre().lower()]-=1
                    return prod
                
        else:
            print("El deposito esta vacio.")
            return 0

    