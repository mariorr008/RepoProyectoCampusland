from gestionar_Json import cargar, guardar, generar_id
from validacion import validarEntero, validarMenu, nombre_valido, validarFloat
from JsonLogs import log
from datetime import date, datetime

HERRAMIENTAS_ARCHIVO = 'herramientas.json'

def listar_herramientas():
    herramientas=cargar(HERRAMIENTAS_ARCHIVO)
    if herramientas==[]:
        print('La categoria de herramientas se encuentra vacia')
    else:
        for elementos in herramientas:
            print('==================================================')
            print(f"id:{elementos['id']}")
            print(f"nombre:{elementos['nombre']}")
            print(f"categoria:{elementos['categoria']}")
            print(f"stock:{elementos['stock']}")
            print(f"estado:{elementos['estado']}")
            print(f"valor:{elementos['valor']}")
            print('==================================================')

def registrar_herramienta():
    herramienta=cargar(HERRAMIENTAS_ARCHIVO)
    ################################################
    nombre=input('ingrese el nombre de la herramienta: ')
    while nombre_valido(nombre)==False or nombre_existente(nombre)==True:
        nombre=input('ingrese el nombre de la herramienta: ')
    ###################################################
    categoria=validarMenu('''
                ingrese la categoria de la herramienta
                    1.construccion
                    2.jardineria
                    3.mecanica
                ''',1,3)
    while categoria==None:
        categoria=validarMenu('''error,
                ingrese la categoria de la herramienta
                    1.construccion
                    2.jardineria
                    3.mecanica
                ''',1,3)
    if categoria==1:
            categoria='construccion'
    elif categoria==2:
            categoria='jardineria'
    else:
         categoria='mecanica'
    ##################################################
    stock=validarEntero('ingrese el numero de stock disponible que habra: ')
    while stock==None or stock<=0:
        stock=validarEntero('Error, ingrese el numero de stock disponible que habra: ')
    ########################################################
    estado=validarMenu('''
                ingrese el estado de la herramienta
                    1.Activa
                    2.En reparacion
                    3.Fuera de servicio
                ''',1,3)
    while estado==None:
        estado=validarMenu('''
                Error, ingrese el estado de la herramienta
                    1.Activa
                    2.En reparacion
                    3.Fuera de servicio
                ''',1,3)
    if estado==1:
            estado='Activa'
    elif estado==2:
            estado='En reparacion'
    else:
            estado='Fuera de servicio'
    #######################################################
    valor=validarFloat('Ingrese el valor del producto: ')
    while valor==None or valor<=0:
        valor=validarFloat('Error, ngrese el valor del producto: ')
    #########################################################

    nueva_herramienta={
            'id':generar_id(herramienta),
            'nombre':nombre,
            'categoria':categoria,
            'stock':stock,
            'estado':estado,
            'valor':valor
        }
    herramienta.append(nueva_herramienta)
    guardar(HERRAMIENTAS_ARCHIVO,herramienta)
    print('Herramienta guardada correctamente!')

def nombre_existente(nombre):
    herramientas=cargar(HERRAMIENTAS_ARCHIVO)
    for elementos in herramientas:
        if nombre.lower()==elementos['nombre'].lower():
            return True
    return False

def buscar_herramienta():
    herramienta=cargar(HERRAMIENTAS_ARCHIVO)
    buscar=input('Ingrese el nombre de la herramiena que desea buscar: ')
    while nombre_valido(buscar)==False:
        buscar=input('Ingrese el nombre de la herramiena que desea buscar: ')
    for elementos in herramienta:
        if buscar.lower()==elementos['nombre'].lower():
            print('==================================================')
            print(f"Nombre: {elementos.get('nombre', 'atributo no encontrado')}")
            print(f"categoria: {elementos.get('categoria', 'atributo no encontrado')}")
            print(f"stock: {elementos.get('stock', 'atributo no encontrado')}")
            print(f"estado: {elementos.get('estado', 'atributo no encontrado')}")
            print(f"valor: {elementos.get('valor', 'atributo no encontrado')}")
            print('==================================================')
            return
    print('HERRAMIENTA NO ENCONTRADA')

def actualizar_herramienta():
    herramienta=cargar(HERRAMIENTAS_ARCHIVO)
    listar_herramientas()
    id_herramienta=validarEntero('ingrese el id a actualizar: ')
    while id_herramienta==None:
        id_herramienta=validarEntero('Error, ingrese el id a actualizar: ')
    op=validarMenu('''Ingrese la opcion a actualizar
            1.nombre
            2.categoria
            3.stock
            4.estado
            5.valor
    ''',1,5)
    while op==None:
            op=validarMenu('''error, ngrese la opcion a actualizar
            1.nombre
            2.categoria
            3.stock
            4.estado
            5.valor
    ''',1,5)
            
    match (op):
        case 1:
            for elemento in herramienta:
                if id_herramienta==elemento['id']:
                    nombre=input('ingrese el nombre de la herramienta: ')
                    while nombre_valido(nombre)==False or nombre_existente(nombre)==True:
                        nombre=input('Error, ingrese el nombre de la herramienta: ')
                    elemento['nombre']=nombre
                    log('cambio de nombre', date.today(), 'NO', elemento['id'])
        case 2:
            for elemento in herramienta:
                if id_herramienta==elemento['id']:          
                    categoria=validarMenu('''
                    ingrese la categoria de la herramienta
                        1.construccion
                        2.jardineria
                        3.mecanica
                    ''',1,3)
                    categoria=validarMenu('''error,
                            ingrese la categoria de la herramienta
                                1.construccion
                                2.jardineria
                                3.mecanica
                            ''',1,3)
                    if categoria==1:
                        categoria='construccion'
                    elif categoria==2:
                        categoria='jardineria'
                    else:
                         categoria='mecanica'
                    elemento['categoria']=categoria
                    log('cambio de categoria', date.today(), 'NO', elemento['id'])
        case 3:
            for elemento in herramienta:
                if id_herramienta==elemento['id']:
                        stock=validarEntero('ingrese el numero de stock disponible que habra: ')
                        while stock==None or stock<=0:
                            stock=validarEntero('Error, ingrese el numero de stock disponible que habra: ')
                        elemento['stock']=stock
                        log('cambio de stock', date.today(), 'NO', elemento['id'])
        case 4:
            for elemento in herramienta:
                if id_herramienta==elemento['id']:
                    estado=validarMenu('''
                    ingrese el estado de la herramienta
                        1.Activa
                        2.En reparacion
                        3.Fuera de servicio
                    ''',1,3)
                    while estado==None:
                        estado=validarMenu('''
                        Error, ingrese el estado de la herramienta
                            1.Activa
                            2.En reparacion
                            3.Fuera de servicio
                        ''',1,3)
                    if estado==1:
                        estado='Activa'
                    elif estado==2:
                        estado='En reparacion'
                    else:
                        estado='Fuera de servicio'
                    elemento['estado']=estado
                    log('cambio de estado', date.today(), 'NO', elemento['id'])
        case 5:
            for elemento in herramienta:
                if id_herramienta==elemento['id']:
                    valor=validarFloat('Ingrese el valor del producto: ')
                    while valor==None or valor<=0:
                        valor=validarFloat('Error, ingrese el valor del producto: ')
                    elemento['valor']=valor
                    log('cambio de valor', date.today(), 'NO', elemento['id'])
    guardar(HERRAMIENTAS_ARCHIVO, herramienta)

def eliminar_herramienta():
    herramienta=cargar(HERRAMIENTAS_ARCHIVO)
    listar_herramientas()
    id_herramienta=validarEntero('Escoga el id que desea eliminar: ')
    while id_herramienta==None:
        id_herramienta=validarEntero('Error, escoga el id que desea eliminar: ')
    for clave, elemento in enumerate(herramienta):
        if id_herramienta==elemento['id']:
            herramienta.pop(clave)
            guardar(HERRAMIENTAS_ARCHIVO,herramienta)
            log('se elimino una herramienta', date.today(), elemento['id'], 'NO')
            print('Herramienta eliminada!')
            return
    print('Herramienta no encontrada.')
