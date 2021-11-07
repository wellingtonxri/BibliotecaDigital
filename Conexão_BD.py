import mysql.connector as db #Biblioteca MySQL para Python
banco = db.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="testebiblioteca"
)