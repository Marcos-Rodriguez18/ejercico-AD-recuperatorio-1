#opcion1
def mostrar_listas (lista:list, lista2:list):
    """La funcion recibe 2 listas como parametro.\n
    muestra los elementos de ambas listas a la par."""
    for i in range (len(lista)):
        print(f"{lista[i]}: {lista2[i]}")



#opcion3
def buscar_alumno (lista1:list,lista2:list):
    """Recibe dos listas paralelas como parametro.\n
    Pide un elemento de la lista 1 y muestra el elemento correspondiente de la lista 2."""
    nombre = input("Ingrese el nombre del alumno: ")
    while nombre not in lista1:
        nombre = input("ERROR. No se encontro el alumno.\nPor favor, intente nuevamente: ")
    for i in range (len(lista1)):
        if lista1[i] == nombre:
            print(f"Notas del alumno: {lista2[i]}")



#opcion4
# Buscar una calificación en la matriz y mostrar a qué estudiante y materia pertenece.
def pedir_numero ():
    """La funcion pide un numero al usuario y lo retorna."""
    nota = float(input("Ingrese una nota: "))
    return nota

def buscar_por_nota (lista1,lista2,lista3,nota):
    """Recibe 3 listas como parametro y un dato ingresado por el usuario.\n
    Recorre las listas paralelamente y busca el dato del usuario.\n
    Indica si lo encuentra o no."""
    encontrado = False
    for i in range (len(lista3)): #lista calificaciones
        for j in range (len(lista3[i])):
            if lista3[i][j] == nota:
                encontrado = True
                print(f"El/la alumno/a {lista1[i]} se saco un {nota} en la materia {lista2[j]}")
    if encontrado == False:
        print("No se encontro la nota indicada")

#opcion2 --> primera forma
def promediar (lista):
    """La funcion recibe una lista de listas como parametro y la recorre con un doble for.\n
    Para cada elemento de la lista saca el promedio, los añade a una nueva lista y la retorna."""
    promedios = []
    for i in range (len(lista)):
        suma = 0
        for j in range (len(lista[i])):
            #suma = lista[i]
            suma += lista[i][j]
        promedio = suma / len(lista[i])
        #print(f"promedio del alumno {lista2[i]}: {promedio}")
        promedios.append(promedio)
    return promedios
    
def ordenar_por_mayor (lista,lista2,lista3):
    """La funcion recibe una lista de numeros, otra lista  de nombres y una matriz.\n
    Las ordena segun el mejor promedio y los muestra por pantalla."""
    for i in range (len(lista)-1):
        for j in range (i+1,len (lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

                aux = lista2[i]
                lista2[i] = lista2[j]
                lista2[j] = aux

                aux = lista3[i]
                lista3[i] = lista3[j]
                lista3[j] = aux

        #print(f"{estudiantes[i]}: {promedios[i]}")
                
'''def mostrar_listas(lista,lista2):
    """Recibe dos listas paralelas y las muestra simultaneamente."""
    for i in range (len(lista)):
        print(f"{lista[i]}: {lista2[i]}")'''



estudiantes = ["Ana","Bruno","Carla","Diego"]

materias = ["Matematica", "Historia", "Biologia"]

calificaciones = [[9,8,10], #ana
                  [6,7,8], #bruno
                  [10,10,9], #carla
                  [7,6,5]] #diego

programa_encendido= "s"