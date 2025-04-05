import mysql.connector # type: ignore

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5431sabi",
    database="fast_api_python_db"
)