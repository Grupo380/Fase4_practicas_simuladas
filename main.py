from logger import registrar_error
from src.cliente import Cliente
from src.servicio import Servicio
from src.reserva import Reserva

def main():
    print("="*50)
    print("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("="*50)
    
    try:
        # PRUEBA DE EJEMPLO (Líder)
        print("\n🔹 Probando creación de Cliente...")
        cliente1 = Cliente(1, "Ana Gómez", "ana@email.com", "123456789")
        print(cliente1)
        
        # Aquí los compañeros cargarán las demás clases
        
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")
        registrar_error(str(e))

    print("RESERVA ACTUALIZADA")
    try:
        # PRUEBA DE EJEMPLO (colaborador 1)
        print("\n🔹 Probando creación de reserva...")
        reserva1 =  Reserva (1, "cancha sintetica", 50000, "01-01-2025", "02-01-2025", "01:00", "02:00")
        print(reserva1)
        
    
        reserva2 =  Reserva (1, "cancha sintetica", 50000, "01-01-2025", "02-01-2025", "01:00", "02:00")
        print(reserva1)

 
    except Exception as e:
        print(f"{e}")
        registrar_error(str(e)) 


if __name__ == "__main__":
    main()