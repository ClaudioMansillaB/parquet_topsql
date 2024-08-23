import duckdb
import psycopg2
from psycopg2.extras import execute_batch
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import DB_CONFIG

def duckdb_to_psql(duckdb_name='temp.db'):
    # Conectar a DuckDB
    duck_conn = duckdb.connect(duckdb_name)
    
    # Conectar a PostgreSQL
    pg_conn = psycopg2.connect(**DB_CONFIG)
    pg_conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    pg_cursor = pg_conn.cursor()
    
    # Obtener lista de tablas en DuckDB
    tables = duck_conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    
    for table in tables:
        table_name = table[0]
        
        # Verificar si la tabla existe en PostgreSQL
        pg_cursor.execute(f"SELECT to_regclass('{table_name}')")
        if pg_cursor.fetchone()[0] is None:
            print(f"Table {table_name} does not exist in PostgreSQL. Creating it.")
            create_table_sql = duck_conn.execute(f"SHOW CREATE TABLE {table_name}").fetchone()[0]
            create_table_sql = create_table_sql.replace('CREATE TABLE', f'CREATE TABLE IF NOT EXISTS {table_name}')
            pg_cursor.execute(create_table_sql)
            print(f"Table {table_name} created in PostgreSQL.")
        else:
            print(f"Table {table_name} already exists in PostgreSQL. Proceeding with data insertion.")
        
        # Obtener datos y nombres de columnas de DuckDB
        data = duck_conn.execute(f"SELECT * FROM {table_name}").fetchall()
        columns = duck_conn.execute(f"PRAGMA table_info({table_name})").fetchall()
        column_names = ', '.join([col[1] for col in columns])
        
        # Preparar la sentencia INSERT
        insert_sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({', '.join(['%s']*len(columns))})"
        
        # Insertar datos
        try:
            execute_batch(pg_cursor, insert_sql, data, page_size=1000)
            print(f"Inserted {len(data)} rows into table {table_name} in PostgreSQL")
        except psycopg2.Error as e:
            print(f"Error inserting data into {table_name}: {e}")
    
    duck_conn.close()
    pg_conn.close()
    print("Data transfer to PostgreSQL completed")

if __name__ == "__main__":
    duckdb_to_psql()