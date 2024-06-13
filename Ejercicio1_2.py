print("Escribe 'esc' para salir del programa")

#presione la tecla esc para salir del programa

materias = []
while True:
    materia = input("Escribe una materia: ")
    if materia == "esc":
        break
    materias.append(materia)

print(materias)

for materia in materias:
    print("Yo estudio la materia de " + materia)
