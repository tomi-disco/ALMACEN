from producto import Producto


class Gaseosa(Producto):
    def __init__(self, gondola, codigo_barra, marca, nombre, litros, precio):
        super().__init__(gondola, codigo_barra, marca, nombre, precio)
        self._litros = litros

    def litros(self):
        return self._litros

    def _get_marca(self):
        return self._marca

    def _get_nombre(self):
        return self._nombre

    def _get_precio(self):
        return self._precio

    def _get_codigo_barra(self):
        return self._codigo_barra

    def _get_gondola(self):
        return self._gondola
