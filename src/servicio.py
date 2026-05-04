from abc import ABC, abstractmethod
from .entidad import Entidad

class Servicio(Entidad, ABC):
    """Clase abstracta que representa un servicio general."""
    
    def __init__(self, id_servicio: int, nombre: str, costo_base: float):
        self._id = id_servicio
        self._nombre = nombre
        self._costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, duracion: int, descuento: float = 0.0):
        """Método abstracto para calcular el costo con polimorfismo."""
        pass

    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "costo_base": self._costo_base
        }

    def __str__(self):
        return f"Servicio: {self._nombre} - Costo base: ${self._costo_base:.2f}"