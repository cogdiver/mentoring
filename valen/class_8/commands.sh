find / -name python3 2> /dev/null
find / -name cryptography 2> /dev/null
ls /snap/core22/1564/usr/lib/python3/dist-packages/ | grep cryptography
# cryptography-3.4.8.egg-info

* para instalar pip para el manejo de librerias de python
sudo apt install python3-pip # isntalar pip
pip --version # verificar instalacion
pip install cryptography # instalar una libreria
pip install cryptography==43.0.0
pip install -r requirements.txt # instalar todas las dependencias de requirements

* ejecutar una imagen localmente
docker pull python:3.11.9
docker pull python:3.11.9-slim
docker run -it python:3.11.9-slim
docker run --rm -it python:3.11.9-slim

docker rmi python:3.12
docker rmi python:3.11.9
docker rmi esta_es_mi_imagen

docker build -t esta_es_mi_imagen .
docker run --rm -it esta_es_mi_imagen
docker compose up -d
docker exec -it python-test bash
docker compose up -d --build
docker cp python-test:/test/probando_copy.txt .
docker cp probando_copy.txt python-test:/test/probando_copy_2.txt
