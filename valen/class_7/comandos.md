<!-- Soy un archivo de Markdown -->

# Clase 7 con valen
## Ejecución en consola
Vamos a hacer pruebas de ejecución de código de python desde un IDE usando la consola (UNIX/ubuntu/debian)

Comandos usados en la clase
```bash
python3 ./class_7/saludo.py
sh class_7/ejecutar.sh
./class_7/ejecutar.sh # bash: ./class_7/ejecutar.sh: Permission denied
chmod 744 class_7/ejecutar.sh
chmod +x class_7/ejecutar.sh
```

Permisos de un archivo
-rw-r--r--

* Prámetros posicionales  (sys)
* Pasar parámetros nombrados (argparse)
* Para crear comando aislados (click)
# https://click.palletsprojects.com/en/8.1.x/arguments/