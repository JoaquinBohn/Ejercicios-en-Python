"""El indec esta solicitando una funcion para incluir en un sistema general
que funciona en esta entidad. Esta funcion recibira un unico parametro que debera contener
un listado de marcas de leche , junto con su precio y cantidad total producida por mes. 
La funcion debera procesar un listado y mostrar por pantalla, el promedio de precio, la 
marca que mayor stock valorizado produce por mes, y las 3 marcas de menor produccion en
volumen. Toda esta informacion debera ser mostrada en pantalla, la funcion debera devolver
por su parte el numero total de marcas procesadas."""


lista = [["La Serenisima",60,20000],["Veronica",45,18000],["Coto",50,17000],["Tregar",50,19000]]

#Main de pruebas

def main(lista_de_marcas):
    procesar_listado_marcas_leche(lista_de_marcas)


#Funciones

def procesar_listado_marcas_leche(lista):
    """Recibe una lista con el formato [[marca,precio,produccion por mes],[...]...], 
    imprime por pantalla el promedio de precios, la marca con mayor stock valorizado,
    y las 3 marcas con menor volumen de produccion. A su vez devuelve la cantidad de 
    marcas procesadas."""
    promedio = calcular_promedio(lista)
    marca_mayor_stock_valorizado = calcular_mayor_stock_valorizado(lista)
    marcas_menor_produccion = calcular_tres_marcas_menor_produccion(lista)
    
    print("El promedio de precios es de: {}\n".format(promedio))
    print("La marca con mayor stock valorizado es: {}\n".format(marca_mayor_stock_valorizado))
    print("Las tres marcas de menor volumen de produccion son: ", marcas_menor_produccion[0], " ", marcas_menor_produccion[1], " ",marcas_menor_produccion[2])
    
    return len(lista)
    

def calcular_promedio(lista):
    """Recibe una lista con el formato [[marca,precio,produccion por mes],[...]...] 
    y devuelve el promedio de precios."""
    suma = 0
    promedio = 0
    
    for marca in lista:
        suma += marca[1]
    
    promedio = suma//len(lista)
    
    return promedio


def calcular_mayor_stock_valorizado(lista):
    """Recibe una lista con el formato [[marca,precio,produccion por mes],[...]...] 
    y devuelve la marca de mayor stock valorizado."""
    mayor_stock_valorizado = 0
    marca_mayor_stock = lista[0][0]
    
    for marca in lista:
        precio = marca[1]
        stock = marca[2]
        stock_valorizado = stock * precio
        
        if stock_valorizado > mayor_stock_valorizado:
            mayor_stock_valorizado = stock_valorizado
            marca_mayor_stock = marca[0]
    
    return marca_mayor_stock


def calcular_tres_marcas_menor_produccion(lista):
    """Recibe una lista con el formato [[marca,precio,produccion por mes],[...]...] 
    y devuelve otra lista con las 3 marcas de menor produccion."""
    lista_ordenada_menor_a_mayor = ordenar_lista_menor_a_mayor_produccion(lista)
    lista_marcas_menor_produccion = []
    for i in range(3):
        lista_marcas_menor_produccion.append(lista_ordenada_menor_a_mayor[i][0])
    
    return lista_marcas_menor_produccion



def ordenar_lista_menor_a_mayor_produccion(lista):
    """Recibe una lista y la ordena de menor a mayor segun la produccion mensual."""
    largo_lista = len(lista)
    for i in range(largo_lista):
        for j in range(largo_lista-1):
            if lista[j+1] and lista[j][2] > lista[j+1][2]:
                auxiliar = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = auxiliar
    return lista
 
    
#main(lista)