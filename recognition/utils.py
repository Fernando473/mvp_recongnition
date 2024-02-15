import re

from recognition.tests import fusionar_palabras_con_y

UNIDADES_NUM = {
    'cero': 0,
    'uno': 1,
    'dos': 2,
    'tres': 3,
    'cuatro': 4,
    'cinco': 5,
    'seis': 6,
    'siete': 7,
    'ocho': 8,
    'nueve': 9
}

DECENAS_NUM = {
    'diez': 10,
    'once': 11,
    'doce': 12,
    'trece': 13,
    'catorce': 14,
    'quince': 15,
    'dieciseis': 16,
    'diecisiete': 17,
    'dieciocho': 18,
    'diecinueve': 19,
    'veinte': 20,
    'treinta': 30,
    'cuarenta': 40,
    'cincuenta': 50,
    'sesenta': 60,
    'setenta': 70,
    'ochenta': 80,
    'noventa': 90
}

CIENTOS_NUM = {
    'ciento': 100,
    'doscientos': 200,
    'trescientos': 300,
    'cuatrocientos': 400,
    'quinientos': 500,
    'seiscientos': 600,
    'setecientos': 700,
    'ochocientos': 800,
    'novecientos': 900
}


def letras_a_numero(letras):
    palabras = letras.split()

    resultado = 0
    acumulador = 0

    for palabra in palabras:
        if palabra in UNIDADES_NUM:
            acumulador += UNIDADES_NUM[palabra]
        elif palabra in DECENAS_NUM:
            acumulador += DECENAS_NUM[palabra]
        elif palabra in CIENTOS_NUM:
            acumulador += CIENTOS_NUM[palabra]
        elif palabra == "mil":
            acumulador *= 1000
        elif palabra == "millon":
            acumulador *= 1000000
            resultado += acumulador
            acumulador = 0
        elif palabra == "millones":
            acumulador *= 1000000
            resultado += acumulador
            acumulador = 0

    resultado += acumulador

    return resultado


def extraer_palabras(texto):
    palabras = re.findall(r'\b\w+\b', texto)
    return palabras


complex_words = {
    "veintiuno": "veinte y uno",
    "veintidós": "veinte y dos",
    "veintitrés": "veinte y tres",
    "veinticuatro": "veinte y cuatro",
    "veinticinco": "veinte y cinco",
    "veintiséis": "veinte y seis",
    "veintisiete": "veinte y siete",
    "veintiocho": "veinte y ocho",
    "veintinueve": "veinte y nueve",
}


def words_to_numbers_from_array(texto):
    array = fusionar_palabras_con_y(texto)
    array = [word.lower() for word in array]
    result = ""
    print(array)
    i = 0
    while i < len(array):
        word = array[i]

        if word in complex_words:
            print("Complex words" + word)
            array[i] = complex_words[word]
            print(array[i])
            result += str(letras_a_numero(array[i])) + " "
            i += 1

        elif word:
            print("Word ", word)
            result += str(letras_a_numero(word)) + " "
            i += 1
    return result.strip()  #


string2 = "Veintitrés Cuarenta y Siete ochenta y ocho ciento "
string2 = "veintitrés mil"
result = words_to_numbers_from_array(string2)
print(result)
