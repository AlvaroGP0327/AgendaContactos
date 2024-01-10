import sqlite3
from time import sleep
from funcionalidades import *

def conexion() -> object:
    #Conecta a una db y retorna la conexion
    #Base de datos: Agenda.db
    try:
        conexion = sqlite3.connect("Agenda.db")
        print('Estableciendo conexion a db...')    
        sleep(2)
        return conexion
    except sqlite3.Error as e:
        print("Error al conectar a la base de datos", e)
        return None

def create_cursor(conexion) -> object:
    #Toma una conexion y retorna un cursor
    #para la base de datos requerida
    cursor = conexion.cursor()
    print('Creando cursor...')
    sleep(2)
    return cursor

'''Crear una tabla de prueba con las columnas nombre,apellido,ocupacion'''

def create_table():
    #Crear tabla para cualquier conexion dada
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE contactos_empresa(id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    empresa TEXT NOT NULL,
                    telefono TEXT NOT NULL,
                    email TEXT NOT NULL,
                    residencia TEXT NOT NULL
                    )''')
    print('Tabla creada...')
    sleep(2)
    conn.commit()
    conn.close()

def borrar_tabla(nombre_tabla):
    #Toma un nombre de tabla y una conexion
    #borra la tabla solicitada
    conn = conexion()
    cursor = create_cursor(conn)
    cursor.execute(f'DROP TABLE {nombre_tabla}')
    conn.commit()
    conn.close()
    print(f'tabla {nombre_tabla} borrada')

'''Recibir los datos para ingresarlos a la db'''

def ingresar_nuevo_db(datos_contacto):
    #los datos_contactos se obtienen llamando
    #a la funcion pedir_datos_contacto()
    conn = conexion()
    print('Conexion para ingresar datos')
    cursor = create_cursor(conn)
    
    sql = ('''INSERT INTO contactos_empresa (nombre, apellido, empresa, telefono, email, residencia)
            VALUES (?,?,?,?,?,?) ''')
    cursor.execute(sql,datos_contacto)
    conn.commit()
    conn.close()
    print('Nuevo registro de contacto agregado ')
    sleep(2)


def extraer_contactos_db() -> list:
    #Retorna lista de tuplas de toda la tabla
    conn = conexion()
    print("conexion para extraer contactos")
    cursor = create_cursor(conn)
    sql= ('SELECT * FROM contactos_empresa')
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return data

def obtener_titulos_columnas():
    conn =  conexion()
    print("conexion para extraer titulos") 
    cursor = create_cursor(conn)
    cursor.execute("SELECT * FROM contactos_empresa")
    headers = [columna[0] for columna in cursor.description]
    conn.close()
    return headers

def busqueda_de_id(id):
    
    conn = conexion()
    cursor = create_cursor(conn)
    sql = '''SELECT * FROM contactos_empresa WHERE id=?'''
    cursor.execute(sql, (id,))
    contacto= cursor.fetchall()
    conn.close()
    return contacto


