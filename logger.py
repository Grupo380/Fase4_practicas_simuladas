from datetime import datetime

def registrar_error(mensaje: str):
    """Registra cualquier error en el archivo log.txt con fecha y hora."""
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha_hora}] ERROR: {mensaje}\n")