import os
import duckdb
from config import INPUT_DIR

def parquet_to_duckdb(db_name='temp.db'):
    conn = duckdb.connect(db_name)
    
    for file in os.listdir(INPUT_DIR):
        if file.endswith('.parquet'):
            table_name = os.path.splitext(file)[0]
            file_path = os.path.join(INPUT_DIR, file)
            
            # Cargar Parquet en DuckDB
            conn.execute(f"CREATE TABLE {table_name} AS SELECT * FROM parquet_scan('{file_path}')")
            
            print(f"Loaded {file} into table {table_name}")
    
    conn.close()
    print("All Parquet files loaded into DuckDB")

if __name__ == "__main__":
    parquet_to_duckdb()