# Inner dependencies
from config import PROJECT_ID, DATASET
from database import read_query
from process import process_df, export_df


# Define your query
query = f"""
SELECT *
FROM `{PROJECT_ID}.{DATASET}.fake`
"""

df = read_query(query)
df_clean = process_df(df)
export_df(df_clean, "fake.csv")
# Saludos desde mi localhost:8085
