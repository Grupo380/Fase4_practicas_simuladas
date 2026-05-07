from .servicio import Servicio
from datetime import datetime

import re


class Reserva(Servicio):
    
    reservas = []
    
    
    
    def __init__(self,id_servicio, nombre, costo_base, fecha_inicio, fecha_final, hora_inicio, hora_final):

        self.__fecha_inicio__ = self.verifica_fecha_inicio(fecha_inicio)
        self.__fecha_final__ = self.verifica_fecha_final(fecha_final)
        self.__hora_inicio__ = self.verifica_hora_inicio(hora_inicio)
        self.__hora_final__ = self.verifica_hora_final(hora_final)
        
        super().__init__(id_servicio, nombre, costo_base)
    
        #verificar duplicado
        self.verificar_disponibilidad()
    
        #guardar reserva
        Reserva.reservas.append((
            self.__fecha_inicio__,
            self.__fecha_final__,
            self.__hora_inicio__,
            self.__hora_final__
        ))
    
    def __str__(self):
        return f" reserva: {self.__fecha_inicio__} a {self.__fecha_final__} y de las {self.__hora_inicio__} a las {self.__hora_final__}"
        
    def verificar_disponibilidad(self):
        for reserva in Reserva.reservas:
            
            fecha_i, fecha_f, hora_i, hora_f = reserva
            
            if (
                fecha_i == self.__fecha_inicio__
                and fecha_f == self.__fecha_final__
                and hora_i == self.__hora_inicio__
                and hora_f == self.__hora_final__
            ):
                raise ValueError (" ya se encuentra reservado")
        
    def verifica_fecha_inicio (self, fecha_inicio):
        patron = r'^\d{2}-\d{2}-\d{4}$'
        if not re.match(patron, fecha_inicio):
            raise ValueError(f"fecha invalida: {fecha_inicio}")
        return fecha_inicio
    
    def verifica_fecha_final (self, fecha_final):
        patron = r'^\d{2}-\d{2}-\d{4}$'
        if not re.match(patron, fecha_final):
            raise ValueError(f"fecha invalida: {fecha_final}")
        return fecha_final

    def verifica_hora_inicio (self, hora_inicio):
        patron = r'^\d{2}:\d{2}$'
        if not re.match(patron, hora_inicio):
            raise ValueError(f"fecha invalida: {hora_inicio}")
        return hora_inicio
    
    def verifica_hora_final(self, hora_final):
        patron = r'^\d{2}:\d{2}$'
        if not re.match(patron, hora_final):
            raise ValueError(f"fecha invalida: {hora_final}")
        return hora_final
    
    
        
        
    def calcular_duracion(self):
        
    
        inicio = datetime.strptime(f"{self.__fecha_inicio__} {self.__hora_inicio__}", "%d-%m-%Y %H:%M")
        
        final = datetime.strptime(f"{self.__fecha_final__} {self.__hora_final__}", "%d-%m-%Y %H:%M")
        
        if final <= inicio:
            raise ValueError ("la fecha final debe ser mayor a la fecha inicial")
        
        duracion = final - inicio
        
        
        horas = duracion.total_seconds()/3600
        
        return horas
    
    def calcular_costo(self, descuento: float = 0.0):
        
        duracion = self.calcular_duracion()
        costo = self._costo_base * duracion
        costo = costo - (costo*descuento)
        
        return costo
    
        
    def  to_dict (self):
        return {"id servicio": self._id, "nombre_servicio": self._nombre,
                "costo_base": self._costo_base, "fecha_inicio": self.__fecha_inicio__, "fecha_final": self.__fecha_final__,
                "hora_inicio": self.__hora_inicio__, "hora_final": self.__hora_final__}
        
        


