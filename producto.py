from abc import ABC, abstractmethod


class Producto(ABC):
    def __init__(self,gondola, codigo_barra, marca, nombre, precio):
        self._codigo_barra = codigo_barra
        self._marca = marca
        self._nombre = nombre
        self._gondola = gondola
        self._precio = precio


    @abstractmethod
    def _get_codigo_barra(self):
        pass

    @abstractmethod
    def _get_marca(self):
        pass

    @abstractmethod
    def _get_gondola(self):
        pass

    @abstractmethod
    def _get_precio(self):
        pass

    @abstractmethod
    def _get_nombre(self):
        pass

