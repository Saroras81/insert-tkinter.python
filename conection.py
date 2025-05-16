def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="musicdb",
        port= 3306
    )