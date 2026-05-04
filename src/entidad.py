from abc import ABC, abstractmethod

class Entidad(ABC):
    """Clase abstracta que representa una entidad general del sistema."""
    
    @abstractmethod
    def to_dict(self):
        """Convierte los datos de la entidad a un diccionario."""
        pass

    @abstractmethod
    def __str__(self):
        """Representación en string de la entidad."""
        pass