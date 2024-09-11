# External dependencies
import pandas as pd

def filtar_workers(df):
    filter1 = df["age"] >= 25
    filter2 = ~df["is_worker"]
    _filter = filter1 & filter2
    return df[_filter]


def process_df(df):
    # si se modifica dentro de la funcion
    temp = df.copy(deep=True)

    # Define filters
    temp = filtar_workers(temp)

    # Si no se modifica pero se quiere entregar una variable independiente
    # return df[_filter].copy(deep=True)
    return temp.copy()


def export_df(df, path):
    temp = df.copy(deep=True)

    if not df.empty:
        temp.to_csv(path, index=False)
        temp.to_excel(path.replace(".csv", ".xlsx"), index=False)
    else:
        print("No hay datos")
        pass
