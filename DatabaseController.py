import mysql.connector
import config as c

db = mysql.connector.connect(
    host=c.HOST,
    user=c.USER,
    password=c.PASSWORD,
    database=c.DATABASE
)

# db.close()
