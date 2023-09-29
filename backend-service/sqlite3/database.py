import sqlite3

try: 
    connection = sqlite3.connect('sqlite.db')
except sqlite3.Error as Error: 
    print (Error)