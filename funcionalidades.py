
from tabulate import tabulate
from time import sleep
'''Pedir los datos y retornarlos para enviarlos a db'''

def pedir_datos_contacto() -> list:
    #Recibe los datos, los convierte a lista y retorna    
    print('''Por favor ingrese: \n nombre,apellido,empresa,telefono,email,residencia 
           \n separados por coma (,)''')
    datos_entrada = input('->')
    datos_contactos = datos_entrada.split(",")
    print(datos_contactos)
    return datos_contactos

def buscar_idcontacto():
    #Funcion para retornar un contacto especifico
    id = input('Ingrese la Id de contacto que desea buscar: ')
    return id

def tabla_presentacion(data, headers):
    tabla = tabulate(data,headers,tablefmt='fancy_grid')
    print('Tabla de presentacion creada')
    sleep(1)
    return tabla