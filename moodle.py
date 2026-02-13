from pymongo import MongoClient
import os
import random

def obtener_coleccion():
    cliente = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
    db = cliente["bayeta"]
    return db["frases"]

def inicializar_frases():
    coleccion = obtener_coleccion()

    if coleccion.count_documents({}) == 0:
        with open("frases.txt", "r", encoding="utf-8") as f:
            frases = [{"frase": linea.strip()} for linea in f]

        coleccion.insert_many(frases)

def obtener_frases_aleatorias(n=1):
    coleccion = obtener_coleccion()
    frases = list(coleccion.find({}, {"_id": 0}))

    seleccion = random.sample(frases, min(n, len(frases)))
    return [f["frase"] for f in seleccion]
