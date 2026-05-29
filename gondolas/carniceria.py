from producto import Producto


class Carniceria(Producto):
    def __init__(self, gondola,codigo_barra, marca, nombre, peso, precio):
        super().__init__(gondola,codigo_barra, marca, nombre, precio)
        self._peso = peso

    def peso(self):
        return self._peso

    def _get_nombre(self):
        return self._nombre

    def _get_precio(self):
        if self._nombre.lower() == "morcilla" or self._nombre.lower() == "chorizo":
            return self._precio
        return self._peso * self._precio

    def _get_codigo_barra(self):
        return self._codigo_barra

    def _get_marca(self):
        return self._marca

    def _get_gondola(self):
        return self._gondola
