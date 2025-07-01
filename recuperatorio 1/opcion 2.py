estudiantes = ["Ana","Bruno","Carla","Diego"]

materias = ["Matematica", "Historia", "Biologia"]

calificaciones = [[9,8,10], #ana
                  [6,7,8], #bruno
                  [10,10,9], #carla
                  [7,6,5]] #diego

def sumar_notas (calificaciones):
    suma = 0
    sumas= []
    for notas in calificaciones:
        for nota in notas:    
            suma = suma + nota
            sumas.append(suma)
        print (f"{notas}: {suma}")
    return sumas

def promediar (sumas):
    for i in range (len(sumas)):
        promedio = sumas[i] / (len(sumas)) 

sumas = sumar_notas(calificaciones)