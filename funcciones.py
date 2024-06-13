"""
nombre="Santiago Rodriguez"
print("Longitud del nombre", len(nombre))
"""
import random
""""
resultado= random.randint(1,100)
print(resultado)
"""

"""
def saludar_y_sumar(nombre, num1, num2, num3):
    print("Saludos, ", nombre)
    print("Resultado de la suma", num1+num2)
    print("Resultado de la Multiplicacion", num1*num3)

saludar_y_sumar("Santiago", 3,6,7)
saludar_y_sumar("Santiago", 33,698,34)
saludar_y_sumar("Santiago", 12,987,34)
"""

def setup():
    size(980, 980)
    background(240)

    frutas = ["Kiwi","Banano","Mango"]
    numero = [1,12,21,42]

    for n in numero:
        line(n*100,200,350,450)