import sqlite3
from datetime import datetime

conn = sqlite3.connect("cloud_secure.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("Preetta", "preetta@example.com"))
cursor.execute("INSERT INTO sessions (user_id, active, login_time) VALUES (?, ?, ?)", (1, 1, str(datetime.now())))
cursor.execute("INSERT INTO activities (activity, activity_time) VALUES (?, ?)", ("User logged in", str(datetime.now())))
cursor.execute("INSERT INTO alerts (alert, alert_time) VALUES (?, ?)", ("No threats detected", str(datetime.now())))

conn.commit()
conn.close()
print("✅ Real data inserted")

