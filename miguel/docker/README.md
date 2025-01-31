docker image ls | grep prueba
docker build -t prueba_python_miguel .
docker ps
docker stop $(docker ps -q)
docker rm $(docker ps -q -a)
docker run --rm -it prueba_python_miguel
docker exec -it prueba_python_miguel bash