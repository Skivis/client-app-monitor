import sqlite3


con = sqlite3.connect('data.db')

con.execute("""
CREATE TABLE clients (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  client_id VARCHAR NOT NULL UNIQUE,
  platform VARCHAR NOT NULL
)""")

con.execute("""
CREATE TABLE logs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  client_id VARCHAR NOT NULL,
  level VARCHAR NOT NULL,
  cpu_percent REAL NOT NULL,
  memory_percent REAL NULL,
  num_threads INTEGER,
  time VARCHAR NOT NULL
)""")

con.commit()
