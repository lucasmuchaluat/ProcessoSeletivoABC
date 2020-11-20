import mysql.connector
from functools import partial


def get_connection_helper():
    def run_db_query(connection, query, args=None):
        with connection.cursor() as cursor:
            print('Executando query:')
            cursor.execute(query, args)
            for result in cursor:
                print(result)

    connection = mysql.connector.connect(
        host='localhost',
        port=33062,
        user='megadados',
        password='megadados2020',
        database='clientes'
    )
    return connection, partial(run_db_query, connection)


connection, db = get_connection_helper()
