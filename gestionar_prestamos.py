from validacion import validarEntero, validarFloat, validarMenu, nombre_valido
from gestionar_Json import cargar, guardar, generar_id
from gestionar_herramientas import listar_herramientas
from gestionar_Usuarios import listar_usuario
from datetime import date, datetime

PRESTAMOS_ARCHIVO='prestamos.json'
HERRAMIENTAS_ARCHIVO='herramientas.json'
USUARIOS_ARCHIVO='usuarios.json'

def solicitud_usuario(id_usuario):
    herramientas=cargar(HERRAMIENTAS_ARCHIVO)
    prestamos=cargar(PRESTAMOS_ARCHIVO)
    
    listar_herramientas()

    herramienta_id=validarEntero('Escoja el id de la herramienta que desea: ')
    while herramienta_id==None:
        herramienta_id=validarEntero('Error, escoja el id de la herramienta que desea: ')
    for elemento in herramientas:
        if elemento['id']==herramienta_id:
            if elemento['estado']=='En reparacion' or elemento['estado']=='Fuera de servicio':
                print('Herramienta no disponible')
                return


    cantidad=validarEntero('Ingrese la cantidad de herramientas que nesecita: ')
    while cantidad==None:
        cantidad=validarEntero('Error, ingrese la cantidad de herramientas que nesecita: ')
    for a in herramientas:
        if a['id']==herramienta_id:
            if a['stock']>=cantidad:
                a['stock']-=cantidad
            else:
                print('No hay suficiente cantidad en el stock')
                return
    fecha_inicioS=input('ingrese la fecha de inicio del prestamo: DD/MM/AAAA ')
    try:
        fecha_inicio=datetime.strptime(fecha_inicioS, '%d/%m/%Y')
    except Exception:
        print('Formato de fecha invalido')
        return
    fecha_finalS=input('Ingrese la fecha en la cual devolvera la/s herramientas: DD/MM/AAAA ')
    try:
        fecha_final=datetime.strptime(fecha_finalS, '%d/%m/%Y')
    except Exception:
        print('Formato de fecha invalido')
        return
    
    nuevo_prestamo={
        'id':generar_id(prestamos),
        'id_usuario':id_usuario,
        'herramienta_id':herramienta_id,
        'cantidad':cantidad,
        'fecha_inicio':str(fecha_inicio),
        'fecha_devolucion':str(fecha_final),
        'estado':'pendiente'
    }
    prestamos.append(nuevo_prestamo)
    guardar(HERRAMIENTAS_ARCHIVO, herramientas)
    guardar(PRESTAMOS_ARCHIVO, prestamos)
