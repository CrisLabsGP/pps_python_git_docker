#!/usr/bin/env python3

import random

# Lista de frases auspiciosas
FRASES = [
    "Hoy es un gran día para empezar algo nuevo.",
    "La fortuna sonríe a los valientes.",
    "Cada esfuerzo trae su recompensa.",
    "Confía en tu intuición y triunfarás.",
    "La paciencia trae grandes resultados.",
    "Una sonrisa puede cambiar tu día.",
    "El éxito viene a quien persiste.",
    "Cree en ti y todo será posible."
]

#Función frotar
def frotar(n_frases: int = 1) -> list:
    pass
    # Seleccionamos aleatoriamente las frases
    return random.choices(FRASES, k=n_frases)  
