from desarrollo import *

while programa_encendido == "s":
    print("\n          ---- MENU DE OPCIONES ----")
    print("1-Mostrar la lista de estudiantes y la matriz de calificaciones.\n2-Ordenar a los estudiantes de mayor a menor según su promedio general (promedio de sus 3 materias).\n3-Buscar un estudiante por nombre y mostrar sus calificaciones.\n4-Buscar una calificación en la matriz y mostrar a qué estudiante y materia pertenece.\n5-Apagar programa.")
    opcion = int(input("\nIngrese una opcion (1/5): "))
    while opcion>5 or opcion<1:
        opcion = int(input("\nERROR. ingrese una opcion entre el 1 y 5: "))

    if opcion == 1:
        mostrar_listas(estudiantes, calificaciones)

    elif opcion == 2:
        promedios = promediar(calificaciones)
        ordenar_por_mayor(promedios, estudiantes, calificaciones)
        mostrar_listas(estudiantes, promedios)

    elif opcion == 3:
        buscar_alumno(estudiantes, calificaciones)

    elif opcion == 4:
        nota = pedir_numero()
        buscar_por_nota(estudiantes, materias, calificaciones, nota)

    elif opcion == 5:
        print("Programa apagado.")
        programa_encendido = "n"

