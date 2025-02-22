import pandas as pd

df = pd.DataFrame({f"col_{i+1}": [j for j in range(10)] for i in range(5)})
print(df)

def suma2(valor):
    """Suma 2 al valor ingresado"""
    return valor + 2