from logger import registrar_error
from src.cliente import Cliente
from src.servicio import Servicio

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

if __name__ == "__main__":
    main()