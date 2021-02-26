#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO company (ID,NAME,POSITION,TEAM) VALUES (1, 'Mike', 'CF', 'Angels' )")

conn.execute("INSERT INTO company (ID,NAME,POSITION,TEAM) VALUES (2, 'Corey', 'CF', 'Dodgers' )")

conn.execute("INSERT INTO company (ID,NAME,POSITION,TEAM) VALUES (3, 'Fernando, 'SS', 'Padres' )")

conn.execute("INSERT INTO company (ID,NAME,POSITION,TEAM) VALUES (4, 'Juan', 'RF', 'Phillies' )")

conn.commit()
print("Records created successfully")
conn.close()

