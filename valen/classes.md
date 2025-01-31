Temas
- Python Básico (def, if, else, while, for, dinamicas, tipos, try/except)
- Python Intermedio (listas, diccionarios, iteradores comprensivos, modulos, requirements)

```python
mi_lista = [1, 2, 3, 4]
l = []
for v in mi_lista:
    l.append(v**2)
mi_lista = l
mi_lista # [1, 4, 9, 16]
```
```python
mi_lista = [1, 2, 3, 4]
mi_lista = [v**2 for v in mi_lista]
mi_lista # [1, 4, 9, 16]
```
```python
def calcular_exp(v):
    return v**2

mi_lista = [1, 2, 3, 4]
mi_lista = [calcular_exp(v) for v in mi_lista]
mi_lista # [1, 4, 9, 16]
```
```python
def calcular_exp(v):
    return v**2

mi_dict = {"1": 10, "2": 20, "3": 30, "4": 40}
[key for key, value in mi_dict.items()] # ['1', '2', '3', '4']
{value: call_function(key) for key, value in mi_dict.items()}
{value: key for key, value in mi_dict.items()} | {value * 2: key for key, value in mi_dict.items()}
```
```python
matriz = [[1,2],[3,4],[5,6]]

for i in matriz:
    linea = matriz[i]
    for j in linea:
        pass

[call_funcion(i, j) for i in matriz for j in matriz[i] if ...]
```
```python
class Persona:
    def __init__(self):
        pass
```

```python
# MODULOS
# app/utils.py
def saludar(name):
    print(f"Hola, {name}")

# main.py
from app.utils import saludar
saludar("Valentina")
```

- Python Avanzado (conexion a sistemas externos, pandas, librerías) [Casos de uso]
```python
def mi_function(p1, *args, **kwargs):
    pass
```
```python
class Validation(Base):
    def __init__(self, query, to_adreesses, ...):
        super().__init__()
        self.query = query
        self.to_adreesses = to_adreesses
    def run_query_validacion(self):
        client.query(self.query)
    def execute(self):
        self.run_query_validacion()
        self.send_email()

for obj in validaciones:
    v = Validation(**obj)
    v.execute()
```

- Analitica / Ingenieria / Science / DevOps (.sh/bash/terminal)
