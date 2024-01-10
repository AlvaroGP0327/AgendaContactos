from time import sleep
from conexion import *
from funcionalidades import*

def imprimir_cuadrado_con_texto(texto):
    longitud_texto = len(texto)
    ancho_cuadrado = longitud_texto + 4  # Ancho del cuadrado (texto + bordes)
    
    # Imprimir la línea superior del cuadrado
    print('*' * ancho_cuadrado)
    
    # Imprimir el contenido del cuadrado
    print(f'* {texto} *')
    
    # Imprimir la línea inferior del cuadrado
    print('*' * ancho_cuadrado)

def mostrar_menu() -> int:
    #Recibe una seleccion numerica y la retorna
    # La seleccion se utiliza para llamar funciones
    
    while True:
        imprimir_cuadrado_con_texto('CONTACTOS DE EMPRESA')
        print('Menu de aplicacion CONTACTOS DE EMPRESA')
        print('1. Agregar contacto')
        print('2. Mostrar todos los contactos')
        print('3. Buscar contacto')
        print('4. Modificar contacto')
        print('5. Eliminar contacto')
        print('6. Salir de la aplicacion')
        print('#@#@#@#@')
        try:
            seleccion = int(input('Seleccione opcion: '))
        except ValueError:
            print('Ingrese una opcion numerica del 1 al 6')
            sleep(3)
            continue #Indica que se regrese al inicio del ciclo
        if seleccion == 6:
            print('Saliendo de la aplicacion...')
            break
        elif seleccion > 6 or seleccion <= 0:
            print('Por favor ingrese una opcion valida...')
            sleep(2)
        else:
            print('redireccionando a la seleccion')
            match seleccion:
                #Llamado a las funciones
                case 1:
                    datos = pedir_datos_contacto()
                    ingresar_nuevo_db(datos)
                case 2:
                    data = extraer_contactos_db()
                    headers = obtener_titulos_columnas()
                    tabla = tabla_presentacion(data, headers)
                    print(tabla)
                    sleep(5)
                case 3:
                    id = buscar_idcontacto()
                    contacto = busqueda_de_id(id)
                    header = obtener_titulos_columnas()
                    tabla = tabla_presentacion(contacto,header)
                    print(tabla)
                    sleep(4)
                case 4:
                    pass
                case 5:
                    pass

if __name__ == '__main__':
    mostrar_menu()