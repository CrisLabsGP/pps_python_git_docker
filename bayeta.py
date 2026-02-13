#!/usr/bin/env python3

import random
from moodle import obtener_frases_aleatorias

def cargar_frases(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        frases_leidas = archivo.readlines()

    # Quitar saltos de línea
    frases_leidas = [frases_leidas.strip() for frases_leidas in frases_leidas]

    return frases_leidas
# Lista de frases auspiciosas
FRASES = cargar_frases("./frases.txt")

#Función frotar
def frotar(frases):
    resultado = obtener_frases_aleatorias(frases)
    return {"frases": resultado}

