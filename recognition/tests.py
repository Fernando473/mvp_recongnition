def fusionar_palabras_con_y(cadena):
    palabras = cadena.split()
    resultado = []

    i = 0
    while i < len(palabras):
        if i < len(palabras) - 1 and palabras[i + 1] == 'y':
            if 0 < i < len(palabras) - 2:
                nueva_palabra = palabras[i].lower() + " " + palabras[i + 1].lower() + " " + palabras[i + 2].lower()
                resultado.append(nueva_palabra)
                i += 2
            else:
                resultado.append(palabras[i])
        else:
            resultado.append(palabras[i])
        i += 1

    return resultado


cadena = "veintitrés Cuarenta y Siete ochenta y ocho"
resultado = fusionar_palabras_con_y(cadena)
print(resultado)
