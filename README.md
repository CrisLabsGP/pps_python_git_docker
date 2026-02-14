# pps_python_git_docker

# Título
- Bayeta de la fortuna

# Descripción 
- Aplicación web que consiste en que cada vez que accedamos a la web, nos dirá un texto auspicioso aleatorio.

# Instalación
## Instalar dependencias
Clonamos el repositorios y construimos la imagen Docker.
```
git clone https://github.com/CrisLabsGP/pps_python_git_docker.git; \
cd ./pps_python_git_docker; \
sudo docker compose up -d
```

# Ejecutar la aplicación
- Vamos al navegador y ejecutamos lo siguiente en la URL:
```
http://localhost:5000/frotar/<n>
```
    - "<n>" es es un número. Hay que poner un número (el que tu quieras) entre 1 y 13 para que salga una frase al frotar la bayeta.
