import sqlite3


con = sqlite3.connect('data.db')

con.execute("""
CREATE TABLE clients (
    id INTEGER PRIMARY KEY,
    client_id INTEGER NOT NULL,
    platform char(100) NOT NULL
)""")

con.commit()
