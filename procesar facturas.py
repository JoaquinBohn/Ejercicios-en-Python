"""Dado el archivo ventas.txt(ordenado por nroFactura) con informacion de las ventas del ultimo mes y el siguiente formato: nroCliente;fecha;nroFactura;monto

Ejemplo:
00058;10/06/2019;000101;1500
00130;11/06/2019;000102;2400
00058;11/06/2019;000103;1100
00074;15/06/2019;000104;900
00130;16/06/2019;000105;1500
00058;16/06/2019;000106;1000

Y el diccionario clientes, conteniendo informacion de los clientes.

clientes = {"00058": "Cosme Fulanito", "00074": "Homero Simpson", "00099": "Ned Flanders", "00130": "Homero Thompson"}

Se pide:
    1. Leer y procesar el archivo ventas.txt.
    2. Imprimir la suma y el promedio de los montos facturados en el ultimo mes.
    3. Imprimir un listado, ordenado por cliente, indicando la cantidad de compras y los montos totales
       comprados por cada uno de ellos.

Numero de cliente    Nombre de cliente   Cantidad de compras    Monto total comprado
NNN                     NNNNNNNNNN          NNNNNNNN                NNNNN,NN
"""
clientes = {"00058": "Cosme Fulanito", "00074": "Homero Simpson", "00099": "Ned Flanders", "00130": "Homero Thompson"}
nombre_archivo = "ventas.txt"

import csv

#Main de pruebas

def main(nombre_archivo):
    lista_lineas = leer_archivo(nombre_archivo)
    print(lista_lineas)
    imprimir_montos(nombre_archivo, clientes)
    facturacion_clientes(nombre_archivo, clientes)



#funciones

def leer_archivo(nombre_archivo):
    """Recibe el nombre o la ruta de un archivo y devuelve una lista con su contenido."""
    try:
        with open(nombre_archivo) as archivo_ventas:
            lista_lineas = []
            archivo_ventas_csv = csv.reader(archivo_ventas, delimiter=";")
            for linea in archivo_ventas_csv:
                numero_cliente = linea[0]
                fecha = linea[1]
                numero_factura = linea[2]
                monto = linea[3]
                lista_lineas.append([numero_cliente,fecha,numero_factura,monto])
            return lista_lineas
    except IOError:
        print("Error al abrir el archivo solicitado.")


def imprimir_montos(nombre_archivo, diccionario):
    """Recibe el nombre o ruta de un archivo y un diccionario de clientes e imprime por pantalla
     la suma y el promedio de los montos facturados el ultimo mes."""
    datos_archivo = leer_archivo(nombre_archivo)
    suma = 0
    if len(datos_archivo)==0:
        print("El archivo se encuentra vacio.")
        return
    for linea in datos_archivo:
        suma += float(linea[3])
    promedio = suma/len(datos_archivo)
    print("Suma de los montos facturados el ultimo mes: {}\n".format(suma)+"Promedio de los montos facturados: {}\n".format(promedio))


def facturacion_clientes(nombre_archivo,diccionario):
    """Recibe el nombre o ruta de un archivo y un diccionario e imprime las facturas totales de cada cliente."""
    datos_archivo = leer_archivo(nombre_archivo)
    lista_clientes = []
    if len(datos_archivo)==0:
        print("Archivo vacio")
        return
    for linea in datos_archivo:
        if not linea[0] in lista_clientes:
            numero_cliente = linea[0]
            nombre = diccionario.get(numero_cliente)
            monto = linea[3]
            cantidad_facturas = 1
            lista_clientes.append([numero_cliente,nombre,cantidad_facturas,monto])
        else:
            for i in range (len(lista_clientes)):
                if linea[0]==lista_clientes[i][0]:
                    lista_clientes[i][3] += linea[3]
                    lista_clientes[i][2] += 1
    lista_clientes.sort()
    print("Numero de cliente - Nombre cliente - Cantidad de compras - Monto total")
    for x in lista_clientes:
        print(x)

#main("ventas.txt")


