#pip install db-dtypes
#pip install pandas
import os
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
os.environ.setdefault("GCLOUD_PROJECT", "smartphone")
client = bigquery.Client()

key_path = "/Users/lucyswain/Downloads/eighth-vehicle-416912-2f7dd9ed2272.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
print("********")
print(credentials.project_id)

client = bigquery.Client(
    credentials=credentials,
    project=credentials.project_id,
)

QUERY = (
    "SELECT model, price, rating,card "
    "FROM `eighth-vehicle-416912.smartphone.phonedata` "
    "WHERE card LIKE '%%iOS%%'"
)


query_job = client.query(QUERY)  # API request
#rows = query_job.result()  # Waits for query to finish
#for row in rows:
#    print(row)


df = query_job.to_dataframe()

# Print or manipulate the DataFrame as needed
print(df.head(10))  # Display the first 10 rows of the DataFrame
