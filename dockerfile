# ---------- Fase 1: resolución de dependencias ----------
FROM python:3.12-slim AS builder

#Directorio de trabajo
WORKDIR /app 

# Copiamos solo requirements
COPY requirements.txt .
COPY frases.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---------- Fase 2: ejecución ----------
FROM python:3.12-slim

#Directorio de trabajo
WORKDIR /app

# Copiamos dependencias instaladas desde builder
COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiamos código 
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
