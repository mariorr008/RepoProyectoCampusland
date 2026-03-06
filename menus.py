from validacion import validarEntero, validarMenu,nombre_valido
from gestionar_herramientas import listar_herramientas, registrar_herramienta, buscar_herramienta, actualizar_herramienta, eliminar_herramienta 
from gestionar_Usuarios import listar_usuario, registrar_usuarios, buscar_usuario, actualizar_usuario, eliminar_usuario, solicitudes, listar_Usadas, id_existente
from gestionar_prestamos import solicitud_usuario
from JsonLogs import listarLogs

def menu_login():
    print('''
    ===============================================
              Bienvenido a nuestra app
    ===============================================
    ''')
    while True:
        op=validarMenu('''Eliga su rol
    ======================================================
                    1.Administrador
                    2.Usuario
                    3.Salir
    ======================================================
                        ''',1,3)
        while op==None:
            op=validarMenu('''Error,escoga una opcion valida
    ======================================================
                        1.Administrador
                        2.Usuario
                        3.Salir
    ======================================================
                            ''',1,3)
        match op:
            case 1:
                contraseña_fija='1234'
                contraseña=input('ingrese su contraseña de administrador: ')
                while contraseña!=contraseña_fija:
                    contraseña=input('Error, ingrese su contraseña de administrador: ')
                menu_admin()
            case 2:
                id_usuario=validarEntero('Ingrese el id del usuario: ')
                while id_usuario==None:
                    id_usuario=validarEntero('Error, ingrese el id del usuario: ')
                id=id_existente(id_usuario)
                if id==True:
                    menu_de_usuarios(id_usuario)
                elif id==False:
                    print('Usuario no encontrado, por favor pedir al administrador registarlo')
            case 3:
                print('Gracias por usar nuestra app :)')
        if op==3:
            break

def menu_admin():
    while (True):
        op=validarMenu('''Eliga una 
    ======================================================
                1.Gestionar herramientas
                2.Gestionar usuarios
                3.cambios realizados
                4.Salir
    ======================================================
                       ''',1,4)
        while op==None:
            op=validarMenu('''Error, eliga una opcion
    ======================================================
                1.Gestionar herramientas
                2.Gestionar usurarios
                3.Cambios realizados
                4.Salir
    ======================================================
                       ''',1,4)
        match (op):
            case 1:
                menu_herramientas()
            case 2:
                menu_usuarios()
            case 3:
                listarLogs()
            case 4:
                break

def menu_herramientas():
    while(True):
        op=validarMenu('''Eliga una opcion
        ==========================================================
                    1.Listar herramientas
                    2.Registrar herramienta
                    3.Buscar herramienta
                    4.Actualizar herramienta
                    5.Eliminar herramienta
                    6.Salir
        ==========================================================
                    ''',1,6)
        while op==None:
            op=validarMenu('''Error, eliga una opcion
        ==========================================================
                    1.Listar herramientas
                    2.Registrar herramienta
                    3.Buscar herramienta
                    4.Actualizar herramienta
                    5.Eliminar herramienta
                    6.Salir
        ==========================================================
                    ''',1,6)
        match (op):
            case 1:
                listar_herramientas()
            case 2:
                registrar_herramienta()
            case 3:
                buscar_herramienta()
            case 4:
                actualizar_herramienta()
            case 5:
                eliminar_herramienta()
            case 6:
                break

def menu_usuarios():
        while True:
            op=validarMenu('''Eliga una opcion
        ==========================================================
                        1.Listar usuario
                        2.Registrar usuario
                        3.Buscar usuario
                        4.Actualizar usuario
                        5.Eliminar usuario
                        6.Solicitudes de usuarios
                        7.Salir
        ==========================================================
                        ''',1,7)
            while op==None:
                op=validarMenu('''Error, eliga una opcion
        ==========================================================
                        1.Listar usuario
                        2.Registrar usuario
                        3.Buscar usuario
                        4.Actualizar usuario
                        5.Eliminar usuario
                        6.Solicitudes de usuarios
                        7.Salir
        ==========================================================
                        ''',1,7)
            match (op):
                case 1:
                    listar_usuario()
                case 2:
                    registrar_usuarios()
                case 3:
                    buscar_usuario()
                case 4:
                    actualizar_usuario()
                case 5:
                    eliminar_usuario()
                case 6:
                    solicitudes()
                case 7:
                    break

def menu_de_usuarios(identificador):
    while True:
        op=validarMenu('''Ingrese la opcion que desea
        ==========================================================
                    1.ver todas las herramientas
                    2.ver herramientas usadas
                    3.realizar peticion de prestamo
                    4.salir
        ==========================================================
                    ''',1,4)
        while op==None:
            op=validarMenu('''Error, ingrese la opcion que desea
        ==========================================================

                    1.ver todas las herramientas
                    2.ver herramientas usadas o en petecion
                    3.realizar peticion de prestamo
                    4.salir
        ==========================================================
                    ''',1,4)
        match (op):
            case 1:
                listar_herramientas()
            case 2:
                listar_Usadas()
            case 3:
                solicitud_usuario(identificador)
            case 4:
                break
