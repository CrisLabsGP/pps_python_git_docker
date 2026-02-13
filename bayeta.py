#!/usr/bin/env python3

import random

def cargar_frases(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        frases_leidas = archivo.readlines()

    # Quitar saltos de línea
    frases_leidas = [frases_leidas.strip() for frases_leidas in frases_leidas]

    return frases_leidas
# Lista de frases auspiciosas
FRASES = cargar_frases("./frases.txt")

#Función frotar
def frotar(n_frases: int =1) -> list:
    pass
    # Seleccionamos aleatoriamente las frases
    return random.choices(FRASES, k=n_frases)  
