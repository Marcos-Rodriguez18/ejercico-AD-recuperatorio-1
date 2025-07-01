def temperatura_media_alta (lista,numero): #parametros formales
    """La funcion recibe una lista y un numero entero.\n
    Calcula el promedio de la lista y chequea si es mayor o menor que el numero ingresado."""
    suma = 0
    retorno = False
    for i in range (len(lista)):
        suma += lista[i]
    promedio = suma / len(lista)
    if promedio > numero:
        retorno = True
    return retorno

temperaturas = [18,22,25,20,21]
umbral = 20 
print(temperatura_media_alta(temperaturas,umbral)) #invocacion con parametros actuales