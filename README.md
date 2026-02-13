# pps_python_git_docker

# Título
- Bayeta de la fortuna

# Descripción 
- Aplicación web que consiste en que cada vez que accedamos a la web, nos dirá un texto auspicioso aleatorio.

# Instalación
## Instalar dependencias
1. Clonamos el repositorios y construimos la imagen Docker.
```
git clone https://github.com/CrisLabsGP/pps_python_git_docker.git; \
cd ./pps_python_git_docker; \
sudo docker build -t bayeta-fortuna .
```
2. Creamos una red virtual en Docker y levantamos MongoDB
``` 
sudo docker network create bayeta-net; \
sudo docker run -d \
  --name mongo-bayeta \
  --network bayeta-net \
  -p 27017:27017 \
  mongo
```
3. Levantamos el contenedor de la Bayeta de la Fortuna.
``
sudo docker run -d \
  --name bayeta-app \
  --network bayeta-net \
  -e MONGO_URI="mongodb://mongo-bayeta:27017/" 
  -p 5000:5000 \
  bayeta-fortuna
 
```

# Ejecutar la aplicación
- Vamos al navegador y ejecutamos lo siguiente en la URL:
```
http://localhost:5000/frotar/<n>
```
    - "<n>" es es un número. Hay que poner un número (el que tu quieras) entre 1 y 13 para que salga una frase al frotar la bayeta.
