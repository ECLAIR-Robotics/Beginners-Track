import sqlite3

class Database:
    table_name = "table" # We only want one table so dont change this often (itll create a new one)
    
    def __init__(self):
        self.con = sqlite3.connect("sql.db")
        self.cursor = self.con.cursor()
        # self.cursor.execute(f"CREATE TABLE {Database.table_name} (id INTEGER PRIMARY KEY, state bool);") # Uncomment this line and fill out thing and check if table already exists

    def setStatus(self, id, state):
        self.cursor.execute("UPDATE "+ Database.table_name + " SET state = " + state + "WHERE id = " + id)
        # alternitavly: self.cursor.execute(f"UPDATE {Database.table_name} SET state={state} WHERE id={id}")
        return True
    


    '''
        We will talk about next time:
        try-catch
        python formating
        parameter and return checking
        
    '''


