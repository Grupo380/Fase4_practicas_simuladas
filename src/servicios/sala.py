from src.servicio import Servicio

class Sala(Servicio):
    def __init__(self, id_servicio: int, nombre: str, costo_base: float, capacidad: int, ubicacion: str):
        super().__init__(id_servicio, nombre, costo_base)

        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un número entero positivo.")
        if not isinstance(ubicacion, str) or not ubicacion.strip():
            raise ValueError("La ubicación no puede estar vacía.")

        self.__capacidad = capacidad
        self.__ubicacion = ubicacion

    def get_capacidad(self) -> int:
        return self.__capacidad

    def set_capacidad(self, capacidad: int):
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un número entero positivo.")
        self.__capacidad = capacidad

    def get_ubicacion(self) -> str:
        return self.__ubicacion

    def set_ubicacion(self, ubicacion: str):
        if not isinstance(ubicacion, str) or not ubicacion.strip():
            raise ValueError("La ubicación no puede estar vacía.")
        self.__ubicacion = ubicacion

    def calcular_costo(self, duracion: int, descuento: float = 0.0) -> float:
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a 0")

        costo_total = self._costo_base * (duracion / 60)
        return costo_total * (1 - descuento)

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict.update({
            "tipo_servicio_clase": "Sala",
            "capacidad": self.__capacidad,
            "ubicacion": self.__ubicacion
        })
        return base_dict

    def __str__(self) -> str:
        return (f"Sala: {self._nombre} (ID: {self._id}), "
                f"Costo base: ${self._costo_base:.2f}, "
                f"Capacidad: {self.__capacidad}, "
                f"Ubicación: {self.__ubicacion}")