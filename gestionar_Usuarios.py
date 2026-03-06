from gestionar_Json import cargar, guardar, generar_id
from validacion import validarEntero, validarMenu, nombre_valido, validarFloat
from JsonLogs import log
from datetime import date, datetime

USUARIOS_ARCHIVO='usuarios.json'
PRESTAMOS_ARCHIVO='prestamos.json'
HERRAMIENTAS_USADAS='usadas.json'
HERRAMIENTAS_ARCHIVO='herramientas.json'
LOGS='gestionarLogs.json'

def registrar_usuarios():
    usuario=cargar(USUARIOS_ARCHIVO)
    ################################################
    nombre=input('ingrese el nombre del usuario: ')
    while nombre_valido(nombre)==False or nombre_existente(nombre)==True:
        nombre=input('Error,ingrese el nombre del usuario: ')
    ###################################################
    apellido=input('ingrese el apellido del usuario: ')
    while nombre_valido(apellido)==False:
        apellido=input('Error,ingrese el apellido del usuario: ')
    ######################################################
    telefono=input('Ingrese el numero de telefono del usuario: ')
    while not nombre_valido(telefono):
        telefono=input('Error,Ingrese el numero de telefono del usuario: ')
    ##########################################################
    direccion=input('ingrese la direccion del usuario: ')
    while not nombre_valido(direccion):
        direccion=input('Error,Ingrese la direccion del usuario: ')



    nuevo_usuario={
        'id':generar_id(usuario),
        'nombre':nombre,
        'apellido':apellido,
        'telefono':telefono,
        'direccion':direccion
    }
    usuario.append(nuevo_usuario)
    guardar(USUARIOS_ARCHIVO,usuario)
    print('Usuario guardado correctamente!')

def listar_usuario():
    usuario=cargar(USUARIOS_ARCHIVO)
    if usuario==[]:
        print('La categoria de herramientas se encuentra vacia')
    else:
        for elementos in usuario:
            print('==================================================')
            print(f"id:{elementos['id']}")
            print(f"nombre:{elementos['nombre']}")
            print(f"apellido:{elementos['apellido']}")
            print(f"telefono:{elementos['telefono']}")
            print(f"direccion:{elementos['direccion']}")
            print('==================================================')

def nombre_existente(nombre):
    herramientas=cargar(USUARIOS_ARCHIVO)
    for elementos in herramientas:
        if nombre.lower()==elementos['nombre'].lower():
            return True
    return False

def buscar_usuario():
    usuario=cargar(USUARIOS_ARCHIVO)
    buscar=input('Ingrese el nombre de la usuario que desea buscar: ')
    while nombre_valido(buscar)==False:
        buscar=input('Error, ingrese el nombre del usuario que desea buscar: ')
    for elementos in usuario:
        if buscar.lower()==elementos['nombre'].lower():
            print('==================================================')
            print(f"Nombre: {elementos.get('nombre', 'atributo no encontrado')}")
            print(f"apellido: {elementos.get('apellido', 'atributo no encontrado')}")
            print(f"telefono: {elementos.get('telefono', 'atributo no encontrado')}")
            print(f"direccion: {elementos.get('direccion', 'atributo no encontrado')}")
            print('==================================================')
            return
    print('USUARIO NO ENCONTRADO')

def actualizar_usuario():
        usuario=cargar(USUARIOS_ARCHIVO)
        listar_usuario()
        id_usuario=validarEntero('ingrese el id a actualizar: ')
        while (id_usuario==None):
            id_usuario=validarEntero('Error, ingrese el id a actualizar: ')
        op=validarMenu('''Ingrese la opcion a actualizar
        =========================================
                1.nombre
                2.apellido
                3.telefono
                4.direccion
        =========================================
    ''',1,4)
        while op==None:
                op=validarMenu('''error, ngrese la opcion a actualizar
        =========================================
                1.nombre
                2.apellido
                3.telefono
                4.direccion
        =========================================
    ''',1,4)
        
        match (op):
            case 1:
                for elemento in usuario:
                    if id_usuario==elemento['id']:
                        nombre=input('ingrese el nombre del usuario: ')
                        while nombre_valido(nombre)==False or nombre_existente(nombre)==True:
                            nombre=input('Error, ingrese el nombre del usuario: ')
                        elemento['nombre']=nombre
                        log('cambio de nombre', date.today(), elemento['id'], 'NO')
            case 2:
                for elemento in usuario:
                    if id_usuario==elemento['id']:
                        apellido=input('ingrese el apellido del usuario: ')
                        while nombre_valido(apellido)==False or nombre_existente(apellido)==True:
                            apellido=input('Error, ingrese el apellido del usuario: ')
                        elemento['apellido']=apellido
                        log('cambio de apellido', date.today(), elemento['id'], 'NO')
            case 3:
                for elemento in usuario:
                    if id_usuario==elemento['id']:
                        telefono=input('Ingrese el numero de telefono del usuario: ')
                        while not nombre_valido(telefono):
                            telefono=input('Error, ingrese el numero de telefono del usuario: ')
                        elemento['telefono']=telefono
                        log('cambio de telefono', date.today(), elemento['id'], 'NO')
            case 4:
                for elemento in usuario:
                    if id_usuario==elemento['id']:
                        direccion=input('ingrese la direccion del usuario: ')
                        while not nombre_valido(direccion):
                            direccion=input('Error, ingrese la direccion del usuario: ')
                        elemento['direccion']=direccion
                        log('cambio de direccion', date.today(), elemento['id'], 'NO')
        guardar(USUARIOS_ARCHIVO, usuario)

def eliminar_usuario():
    usuario=cargar(USUARIOS_ARCHIVO)
    listar_usuario()
    id_usuario=validarEntero('Escoga el id que desea eliminar: ')
    while id_usuario==None:
        id_usuario=validarEntero('Error, escoga el id que desea eliminar: ')
    for clave, elemento in enumerate(usuario):
        if id_usuario==elemento['id']:
            usuario.pop(clave)
            guardar(USUARIOS_ARCHIVO,usuario)
            log('se elimino un usuario', date.today(), elemento['id'], 'NO')
            print('usuario eliminado!')
            return
    print('usuario no encontrado.')

def solicitudes():
    prestamo=cargar(PRESTAMOS_ARCHIVO)
    for elementos in prestamo:
        print('==================================================')
        print(f"id: {elementos['id']}")
        print(f"id_usuario: {elementos['id_usuario']}")
        print(f"id_herramienta: {elementos['herramienta_id']}")
        print(f"cantidad: {elementos['cantidad']}")
        print(f"fecha de inicio: {elementos['fecha_inicio']}")
        print(f"fecha de devolucion: {elementos['fecha_devolucion']}")
        print(f"estado: {elementos['estado']}")
        print('==================================================')

    id_prestamo=validarEntero('Ingrese el id del prestamo que desea ver: ')
    if id_prestamo==None:
        print('ID invalido')
        return

    for elemento in prestamo:
        if elemento['id']==id_prestamo:
            print('==================================================')
            print(f"id: {elemento['id']}")
            print(f"id_usuario: {elemento['id_usuario']}")
            print(f"id_herramienta: {elemento['herramienta_id']}")
            print(f"cantidad: {elemento['cantidad']}")
            print(f"fecha de inicio: {elemento['fecha_inicio']}")
            print(f"fecha de devolucion: {elemento['fecha_devolucion']}")
            print(f"estado: {elemento['estado']}")
            print('==================================================')

            op=validarMenu('''Desea aprovar esta solcitud de prestamo?
                       1.Si
                       2.No
                        ''',1,2)
            while op==None:
                op=validarMenu('''error, desea aprovar esta solcitud de prestamo?
                   1.Si
                   2.No
                ''',1,2)
            match op:
                case 1:
                    elemento['estado']='prestado'
                    guardar(PRESTAMOS_ARCHIVO, prestamo)
                    guardar(HERRAMIENTAS_USADAS, prestamo)
                case 2:
                    elemento['estado']='rechazado'
                    guardar(PRESTAMOS_ARCHIVO, prestamo)
            return
    print('Prestamo no encontrado')

def listar_Usadas():
    usadas=cargar(HERRAMIENTAS_USADAS)
    for elementos in usadas:
        print('==================================================')
        print(f"id: {elementos['id']}")
        print(f"id_usuario: {elementos['id_usuario']}")
        print(f"id_herramienta: {elementos['herramienta_id']}")
        print(f"cantidad: {elementos['cantidad']}")
        print(f"fecha de inicio: {elementos['fecha_inicio']}")
        print(f"fecha de devolucion: {elementos['fecha_devolucion']}")
        print(f"estado: {elementos['estado']}")
        print('==================================================')
            
def id_existente(id_usuario):
    usuario=cargar(USUARIOS_ARCHIVO)
    for elementos in usuario:
        if id_usuario==elementos['id']:
            return True
    return False