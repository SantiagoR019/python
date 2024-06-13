print("Bienvenido al sistema de materias")
#pregunta al usuario su nombre
nombre = input("Cual es tu nombre? ")
#pregunta al usuario su edad
edad = input("Cual es tu edad? ")
#pregunta al usuario su direccion
direccion = input("Cual es tu direccion? ")
#pregunta al usuario su telefono
telefono = input("Cual es tu telefono? ")
#guarda en un diccionario los datos del usuario
datos = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}
print(nombre, "tiene", edad, "años, vive en", direccion, "y su telefono es", telefono)

#pregunta cuales son las materias que esta estudiando y agregakas a una lista
materias = []
while True:
    materia = input("Cuales son las materias que estas estudiando?: ")
    if materia == "esc":
        break
    materias.append(materia)
#pregunte las notas de las materias y las guarde en un diccionario
notas = {}
for materia in materias:
    nota = input("Cual es la nota de " + materia + "? ")
    notas[materia] = nota
#imprima las materias y las notas
print("Las materias que estas estudiando son: ")
for materia in materias:
    print(materia + " con nota " + notas[materia])
# elimine de la lista las asignaturas aprobadas
for materia in materias:
    if int(notas[materia]) >= 6:
        materias.remove(materia)
#imprima las materias que tiene que repetir
print("Las materias que tienes que repetir son: ")
for materia in materias:
    print(materia)