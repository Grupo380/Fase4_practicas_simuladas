from src.cliente import Cliente
from src.servicios.asesoria import Asesoria
from src.servicios.equipos import Equipo
from src.servicios.sala import Sala
from logger import registrar_error


class GestorSistema:

    def __init__(self):

        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

        self.__next_cliente_id = 1
        self.__next_servicio_id = 1
        self.__next_reserva_id = 1

    # CLIENTES

    def agregar_cliente(self, nombre, email, telefono):

        try:

            cliente = Cliente(
                self.__next_cliente_id,
                nombre,
                email,
                telefono
            )

            self.__clientes.append(cliente)
            self.__next_cliente_id += 1

            return cliente

        except ValueError as e:

            registrar_error(f"Error al agregar cliente: {e}")
            return None

        except Exception as e:

            registrar_error(f"Error inesperado al agregar cliente: {e}")
            return None

    def buscar_cliente_por_id(self, id_cliente):

        for cliente in self.__clientes:

            if cliente.get_id() == id_cliente:
                return cliente

        return None

    def listar_clientes(self):

        return self.__clientes

    # SERVICIOS

    def agregar_sala(
        self,
        nombre,
        costo_base,
        capacidad,
        ubicacion
    ):

        try:

            sala = Sala(
                self.__next_servicio_id,
                nombre,
                costo_base,
                capacidad,
                ubicacion
            )

            self.__servicios.append(sala)
            self.__next_servicio_id += 1

            return sala

        except Exception as e:

            registrar_error(f"Error al agregar sala: {e}")
            return None

    def agregar_equipo(
        self,
        nombre,
        costo_base,
        tipo_equipo,
        cantidad_disponible
    ):

        try:

            equipo = Equipo(
                self.__next_servicio_id,
                nombre,
                costo_base,
                tipo_equipo,
                cantidad_disponible
            )

            self.__servicios.append(equipo)
            self.__next_servicio_id += 1

            return equipo

        except Exception as e:

            registrar_error(f"Error al agregar equipo: {e}")
            return None

    def agregar_asesoria(
        self,
        nombre,
        costo_base,
        especialidad
    ):

        try:

            asesoria = Asesoria(
                self.__next_servicio_id,
                nombre,
                costo_base,
                especialidad
            )

            self.__servicios.append(asesoria)
            self.__next_servicio_id += 1

            return asesoria

        except Exception as e:

            registrar_error(f"Error al agregar asesoría: {e}")
            return None

    def buscar_servicio_por_id(self, id_servicio):

        for servicio in self.__servicios:

            if servicio._id == id_servicio:
                return servicio

        return None

    def listar_servicios(self):

        return self.__servicios

    def listar_reservas(self):

        return self.__reservas