print("********************************* \n *********BIENVENIDO A********** \n *********LA TIENDA DE ABARROTES ********** \n *********************************");

manzanas = 20;
peras = 5;
fresas = 15;
uvas = 20;
bananos = 5;

precio_manzanas = 2000;
precio_peras = 1500;
precio_fresas = 2500;
precio_uvas = 3000;
precio_bananos = 1000;

nombre = input("¿Cual es tu nombre?:")
print("Hola,",nombre, ", Te damos la Bienvenida a la tienda de Abarrotes");

print("Tenemos disponibles estos productos: \n 1. ", manzanas ," Manzanas. Precio: $",precio_manzanas," \n 2. ",peras, "Peras. Precio: $",precio_peras, "\n 3. ", fresas, " Fresas. Precio: $",precio_fresas," \n 4. ", uvas, " Uvas. Precio: $",precio_uvas,". \n 5. ", bananos, " Bananos. Precio: $",precio_bananos,"");

numeroProducto = int(input("¿Qué producto deseas adquirir? Digita un número del listado: "))
cantidadProductos = int(input("¿Cuántas unidades deseas adquirir? Ingresa la cantidad: "))


def switch(numeroProducto,cantidadProductos):
    if numeroProducto == 1:
        if cantidadProductos > manzanas:
            return f"Lo siento, solo tenemos {manzanas} Manzanas disponibles."
        return f"Has elegido {cantidadProductos} Manzanas.\nTotal: {cantidadProductos * precio_manzanas}\nManzanas disponibles: {manzanas - cantidadProductos}"
    elif numeroProducto == 2:
        if cantidadProductos > peras:
            return f"Lo siento, solo tenemos {peras} Peras disponibles."
        return f"Has elegido {cantidadProductos} Peras.\nTotal: {cantidadProductos * precio_peras}\nPeras disponibles: {peras - cantidadProductos}"
    elif numeroProducto == 3:
        if cantidadProductos > fresas:
            return f"Lo siento, solo tenemos {fresas} Fresas disponibles."
        return f"Has elegido {cantidadProductos} Fresas.\nTotal: {cantidadProductos * precio_fresas}\nFresas disponibles: {fresas - cantidadProductos}"
    elif numeroProducto == 4:
        if cantidadProductos > uvas:
            return f"Lo siento, solo tenemos {uvas} Uvas disponibles."
        return f"Has elegido {cantidadProductos} Uvas.\nTotal: {cantidadProductos * precio_uvas}\nUvas disponibles: {uvas - cantidadProductos}"
    elif numeroProducto == 5:
        if cantidadProductos > bananos:
            return f"Lo siento, solo tenemos {bananos} Bananos disponibles."
        return f"Has elegido {cantidadProductos} Bananos.\nTotal: {cantidadProductos * precio_bananos}\nBananos disponibles: {bananos - cantidadProductos}"
    else:
        return "Producto no válido"
    
resultado = switch(numeroProducto, cantidadProductos)
print(resultado)



