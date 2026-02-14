#!/usr/bin/env python3

from bayeta import frotar, anadir_frases
from flask import Flask, jsonify, request
from moodle import obtener_frases_aleatorias, inicializar_frases


app = Flask(__name__)
frases = ""
# Endpoint GET /frotar/<n_frases>
@app.route("/frotar/<int:frases>", methods=["GET"])


def endpoint_frotar(frases):
    # Devuelve n_frases frases auspiciosas en JSON.S
    frases = frotar(frases)
    return jsonify({"frases": frases})


@app.route("/frotar/add", methods=["POST"])
def endpoint_add_frases():
    data = request.get_json()

    if not data or "frases" not in data:
        return jsonify({"error": "Formato incorrecto"}), 400

    cantidad = anadir_frases(data["frases"])

    return jsonify({
        "mensaje": "Frases añadidas correctamente",
        "cantidad_insertada": cantidad
    }), 200


if __name__ == '__main__':
    inicializar_frases()
    app.run(host="0.0.0.0", port="5000")
    #endpoint_frotar(frases)
    obtener_frases_aleatorias(frases)

