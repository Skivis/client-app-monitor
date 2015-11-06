import sqlite3


con = sqlite3.connect('data.db')

con.execute("""
CREATE TABLE clients (
  id INTEGER PRIMARY KEY,
  client_id VARCHAR NOT NULL UNIQUE,
  node VARCHAR NULL,
  platform VARCHAR NULL,
  processor VARCHAR NULL,
  system VARCHAR NULL,
  cpu_count INTEGER NULL
)""")

con.execute("""
CREATE TABLE logs (
  id INTEGER PRIMARY KEY,
  client_id VARCHAR NOT NULL,
  level VARCHAR NOT NULL,
  cpu_percent REAL NOT NULL,
  system_cpu REAL NOT NULL,
  memory_percent REAL NULL,
  num_threads INTEGER,
  time VARCHAR NOT NULL
)""")

con.commit()
