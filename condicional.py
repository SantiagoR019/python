print(" *** Bienvenido al sistema de validación aritmetico *** ")
numero = int(input("Hola, ingresa un número de 1 a 100: "))

if numero < 1:
    print("”Favor de ingresar un número mayor a 0”")
elif numero > 100 :
    print("“Favor de ingresar unnúmero menor o igual a 100”")
else :
    print("“¡Muy bien! El ", numero," es una gran opción”")