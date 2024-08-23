import os
from parquet_to_duckdb import parquet_to_duckdb
from duckdb_to_psql import duckdb_to_psql
from config import OUTPUT_DIR

def main():
    # Convertir Parquet a DuckDB
    print("Step 1: Converting Parquet files to DuckDB...")
    parquet_to_duckdb()

    # Transferir de DuckDB a PostgreSQL
    print("\nStep 2: Transferring data from DuckDB to PostgreSQL...")
    duckdb_to_psql()

    # Generar resumen
    print("\nStep 3: Generating summary...")
    generate_summary()

    print("\nProcess completed successfully!")

def generate_summary():
    summary = "Conversion Summary:\n"
    summary += "===================\n"
    summary += f"Input files processed: {len([f for f in os.listdir('data/input') if f.endswith('.parquet')])}\n"

    with open(os.path.join(OUTPUT_DIR, 'summary.txt'), 'w') as f:
        f.write(summary)

    print("Summary generated in data/output/summary.txt")

if __name__ == "__main__":
    main()