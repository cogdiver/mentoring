docker pull python:alpine3.20

Para corre la imagen
```
docker run python:alpine3.20
```

Ver contenedores en ejecución
```
docker ps
docker ps -a # para ver también los detenidos
```

Quedar en la terminal
```
docker run -it python:alpine3.20
docker run -it --rm python:alpine3.20 # eliminar el contenedor al terminar
```

Detener contenedores
```
docker stop <CONTAINER_ID>
```

Eliminar contenedores
```
docker rm <CONTAINER_ID>
```

Construir imagen nombrada
```
docker build -t python_prueba .
```

Renombrar imagen
```
docker image tag python_prueba python_prueba_2
```

Contruir desde docker-compose
```
docker compose up -d
```

Explorar con logs o entrando (exec)
```
docker logs -f python_pruebas
docker exec -it python_pruebas bash
```
