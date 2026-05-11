from src.servicio import Servicio

class Asesoria (Servicio):
    def __init__(self, id_servicio: int, nombre: str, costo_base: float, tipo_asesoria: str, duracion_sesion_minutos: int):
        super().__init__(id_servicio, nombre, costo_base)
        if not isinstance(tipo_asesoria, str) or not tipo_asesoria.strip():
            raise ValueError("El tipo de asesoria no puede estar vacio.")
        if not isinstance (duracion_sesion_minutos, int) or duracion_sesion_minutos <= 0:
            raise ValueError ("La duracion de la sesion debe ser un valor positivo")
        self.__tipo_asesoria = tipo_asesoria
        self.__duracion_sesion_minutos = duracion_sesion_minutos

    def get_tipo_asesoria(self) -> str:
        return self.__tipo_asesoria

    def set_tipo_asesoria(self, tipo_asesoria:str):
        if not isinstance (tipo_asesoria, str) or not tipo_asesoria.strip():
            raise ValueError ( "el tipo de asesoria no puede estar vacio")
        self.__tipo_asesoria = tipo_asesoria
    
    def get_duracion_sesion_minutos(self) -> int:
        return self.__duracion_sesion_minutos