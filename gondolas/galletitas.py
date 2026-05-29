from producto import Producto


class Galletitas(Producto):
    def __init__(self, gondola, codigo_barra, marca, nombre, gramos, precio):
        super().__init__(gondola, codigo_barra, marca, nombre, precio)
        self._gramos = gramos

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

    def gramos(self):
        return self._gramos