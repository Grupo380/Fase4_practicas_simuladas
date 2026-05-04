from .entidad import Entidad
import re

class Cliente(Entidad):
    """Clase que representa a un cliente con validaciones y encapsulamiento."""
    
    def __init__(self, id_cliente: int, nombre: str, email: str, telefono: str):
        self.__id = id_cliente
        self.__nombre = nombre
        self.__email = self.validar_email(email)
        self.__telefono = self.validar_telefono(telefono)

    def validar_email(self, email):
        """Valida que el email tenga formato correcto."""
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron, email):
            raise ValueError(f"Email inválido: {email}")
        return email

    def validar_telefono(self, tel):
        """Valida que el teléfono tenga números y longitud adecuada."""
        if not tel.isdigit() or len(tel) < 7:
            raise ValueError(f"Teléfono inválido: {tel}")
        return tel

    # Métodos Getters para acceder a los datos encapsulados
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "email": self.__email,
            "telefono": self.__telefono
        }

    def __str__(self):
        return f"Cliente: {self.__nombre} (ID: {self.__id})"