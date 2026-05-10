from easysql import EasySQL

db = EasySQL(
    host="localhost",
    user="root",
    password="admin",
    database="assignment"
)

print(db.is_connected())