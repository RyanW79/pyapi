#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE IF NOT EXISTS company
 (ID INT    NOT NULL,
 NAME           TEXT     NOT NULL,
 POSITION       TEXT     NOT NULL,
 TEAM           TEXT     NOT NULL);''')
print("Table created successfully")
conn.close()

