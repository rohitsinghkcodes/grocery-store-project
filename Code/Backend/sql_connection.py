import mysql.connector
# global variable created to avoid multiple creation of sql connection
__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='loggingin',
                                    host='127.0.0.1',
                                    database='grocery_store')
    
    return __cnx