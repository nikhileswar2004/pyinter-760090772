import duckdb


def run_query(database_path, query):
    """Execute an SQL query against a DuckDB database"""
    con = duckdb.connect(database_path)
    try:
        return con.sql(query).df()
    finally:
        con.close()
