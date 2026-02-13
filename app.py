#!/usr/bin/env python3

from bayeta import frotar
from flask import Flask, jsonify

app = Flask(__name__)
frases = ""
# Endpoint GET /frotar/<n_frases>
@app.route("/frotar/<int:frases>", methods=["GET"])


def endpoint_frotar(frases):
    # Devuelve n_frases frases auspiciosas en JSON.S
    frases = frotar(frases)
    return jsonify({"frases": frases})

if __name__ == '__main__':
   
    app.run()
    endpoint_frotar(frases)

