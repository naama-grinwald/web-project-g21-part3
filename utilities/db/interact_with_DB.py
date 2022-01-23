import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# ------------- DATABASE CONNECTION --------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host=os.environ.get('DB_HOST'),
                                         user=os.environ.get('DB_USER'),
                                         passwd=os.environ.get('DB_PASSWORD'),
                                         database=os.environ.get('DB_NAME'))
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

# ------------------------------------------------- #
