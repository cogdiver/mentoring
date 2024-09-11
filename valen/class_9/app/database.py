# External dependencies
import pandas as pd
from google.cloud import bigquery

# Initialize a BigQuery client
client = bigquery.Client()

def read_query(query):
    return client.query(query).to_dataframe()
