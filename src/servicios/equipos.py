from src.servicio import Servicio

class Equipo(Servicio):
    def __init__(self, id_servicio: int, nombre: str, costo_base: float, tipo_equipo: str, cantidad_disponible: int):
        super().__init__(id_servicio, nombre, costo_base)

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise ValueError("El tipo de equipo no puede estar vacío.")
        if not isinstance(cantidad_disponible, int) or cantidad_disponible < 0:
            raise ValueError("La cantidad disponible debe ser un entero no negativo.")

        self.__tipo_equipo = tipo_equipo
        self.__cantidad_disponible = cantidad_disponible

    def get_tipo_equipo(self) -> str:
        return self.__tipo_equipo

    def set_tipo_equipo(self, tipo_equipo: str):
        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise ValueError("El tipo de equipo no puede estar vacío.")
        self.__tipo_equipo = tipo_equipo

    def get_cantidad_disponible(self) -> int:
        return self.__cantidad_disponible

    def set_cantidad_disponible(self, cantidad_disponible: int):
        if not isinstance(cantidad_disponible, int) or cantidad_disponible < 0:
            raise ValueError("La cantidad disponible debe ser un entero no negativo.")
        self.__cantidad_disible = cantidad_disponible

    def calcular_costo(self, duracion: int, descuento: float = 0.0) -> float:
        costo_total = self._costo_base
        return costo_total * (1 - descuento)

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict.update({
            "tipo_servicio_clase": "Equipo",
            "tipo_equipo": self.__tipo_equipo,
            "cantidad_disponible": self.__cantidad_disponible
        })
        return base_dict

    def __str__(self) -> str:
        return (f"Equipo: {self._nombre} (ID: {self._id}), "
                f"Costo base: ${self._costo_base:.2f}, "
                f"Tipo: {self.__tipo_equipo}, "
                f"Disponibles: {self.__cantidad_disponible}")