from gestionar_Json import cargar, guardar, generar_id

LOGS='gestionarLogs.json'

def log(accion, fecha, usuario, herramienta):
    lista=cargar(LOGS)
    lista.append({
        "accion": accion,
        "fecha": str(fecha),
        "usuario": usuario,
        "herramienta":herramienta,
        "id": generar_id(lista)
    })
    guardar(LOGS, lista)

def listarLogs():
    logs=cargar(LOGS)
    for elementos in logs:
        print('==========================================')
        print(f"accion: {elementos['accion']}")
        print(f"fecha: {elementos['fecha']}")
        print(f"usuario: {elementos['usuario']}")
        print(f"herramienta: {elementos['herramienta']}")
        print(f"id: {elementos['id']}")
        print('==========================================')
