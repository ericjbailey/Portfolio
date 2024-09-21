import psycopg2
from psycopg2 import OperationalError, ProgrammingError
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    Creates and connects to the sparkifydb.
    Returns the connection and cursor to sparkifydb.
    Handles potential errors in database creation.
    """
    conn = None
    cur = None
    try:
        # Connect to the default database
        conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
        conn.set_session(autocommit=True)
        cur = conn.cursor()

        # Create sparkify database with UTF8 encoding
        cur.execute("DROP DATABASE IF EXISTS sparkifydb")
        cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

        # Close connection to the default database
        conn.close()

        # Connect to the new sparkify database
        conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
        cur = conn.cursor()

        return cur, conn
    except OperationalError as e:
        print(f"Error during database creation: {e}")
        if conn:
            conn.close()
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        if conn:
            conn.close()
        raise


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    Handles any errors that occur during the process.
    """
    try:
        for query in drop_table_queries:
            cur.execute(query)
            conn.commit()
    except (OperationalError, ProgrammingError) as e:
        print(f"Error dropping tables: {e}")
        conn.rollback()
        raise


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list.
    Handles any errors that occur during the process.
    """
    try:
        for query in create_table_queries:
            cur.execute(query)
            conn.commit()
    except (OperationalError, ProgrammingError) as e:
        print(f"Error creating tables: {e}")
        conn.rollback()
        raise


def main():
    """
    Main function to manage the database creation, table dropping, and table creation process.
    Includes error handling and proper closing of connections.
    """
    conn = None
    cur = None
    try:
        cur, conn = create_database()

        drop_tables(cur, conn)
        create_tables(cur, conn)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    main()