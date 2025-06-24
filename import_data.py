import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# Crenditals
CSV_PATH = os.getenv("CSV_PATH")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


#print(" Loading CSV...")
df = pd.read_csv(CSV_PATH) # LOAD CSV FILE


# Spliting up unique banks
#print(" Extracting unique banks...")
banks_df = df[['bank_name', 'bank_id']].drop_duplicates()
banks_df.columns = ['name', 'id']  

# Extracting branch data
# print(" Preparing branch data...")
branches_df = df[['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state']]


# DB connection
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()


print(f" Inserting {len(banks_df)} banks...") # inserting banks into DB
for _, row in banks_df.iterrows():
    cur.execute(
        "INSERT INTO banks (name, id) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING;",
        (row['name'], int(row['id']))
    )


print(f" Inserting {len(branches_df)} branches (this might take a minute)...")  # inserting branches into DB
for _, row in branches_df.iterrows():
    cur.execute(
        """
        INSERT INTO branches (ifsc, bank_id, branch, address, city, district, state)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (ifsc) DO NOTHING;
        """,
        tuple(row)
    )


conn.commit()
cur.close()
conn.close()

#print("Data inserted successfully!")
