# ETL (Ingeneria de datos)
import pandas as pd

path_source = ""
path_target = ""


def tranform():
    # Load data
    # CSV, Excel, SQL(postgresql, mysql, bigquery, casandra,...),
    # API(json, xml, bin), Scraping, sink, colas
    data = pd.read_csv(path_source)

    # Tranform data
    # Excel, reglas de negocio, limpieza, normalizacion, enriquecimiento
    data = data.dropna()
    # ....

    # Save data
    # Tipado de datos
    # (float 2.36565 -> 2.36)
    # (date UTC)
    # (big int 155565445545 - > 1.55e11)
    data.to_csv(path_target, index=False)


class optimizacion:
    def __init__(self):
        # Funcionamiento del source
        # csv, excel, parquet
        # SQL(SELECT table ... JOIN ..., SELECT view materializada)

        # for row in df.iterrows(): -> df.apply()
        pass

    def __env__(self):
        # frontend -> backend -> db (OLTP) -> ETL -> db (OLAP) -> BI -> science
        #                                       |-> calidad de datos
        #                                       |-> predicion de datos
        # DevOps -> CI/CD -> Docker -> AWS, GCP -> Terraform
        pass
