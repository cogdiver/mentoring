import psycopg2

# Configuración de conexión
DB_CONFIG = {
    "dbname": "mydatabase",
    "user": "admin",
    "password": "admin123",
    "host": "localhost",  # O usa el nombre del contenedor si estás en otro servicio dentro de Docker
    "port": "5432"
}

try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    print("Conectado a:", cursor.fetchone()[0])

    # Cierra la conexión
    cursor.close()
    conn.close()
except Exception as e:
    print("Error al conectar:", e)



def extract():
    pass

def transform():
    pass

def load():
    pass


def main():
    pass

