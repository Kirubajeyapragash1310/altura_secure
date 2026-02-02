import sqlite3

conn = sqlite3.connect("cloud_secure.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    active INTEGER,
    login_time TEXT
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity TEXT,
    activity_time TEXT
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alert TEXT,
    alert_time TEXT
)""")

conn.commit()
conn.close()
print("✅ Database created successfully")

