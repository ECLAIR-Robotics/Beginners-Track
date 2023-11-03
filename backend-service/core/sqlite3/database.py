import sqlite3

class Database:
    table_name = "table" # We only want one table so dont change this often (it'll create a new one when name cchanges)

    def __init__(self):
        self.con = sqlite3.connect("sql.db")
        self.cursor = self.con.cursor()

        # Checking to see if table even exists
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{Database.table_name}'")
        result = self.cursor.fetchone()
        if result:
            print(f"{self.table_name} is online.")
        else:
            self.cursor.execute(f"CREATE TABLE {Database.table_name} (id INTEGER PRIMARY KEY, state BOOL, name TEXT, description TEXT);")  
            print(f"The table '{self.table_name}' is online and instantiated ")
        

    def contains(self, id : int) -> bool:
        """
        Return
            :return True if a device entity with the 'id' exists
        """
        self.cursor.execute(f"SELECT id FROM {Database.table_name} WHERE id={id}")
        if(self.cursor.fetchone()): 
            return True
        return False
        

    def add(self, id : int, state : bool, name, description):
        self.cursor.execute(f"insert into {Database.table_name} (id,state,name,description) values({id},{state}, {name}, {description})")
        print("Umer is the best boss")
        self.con.commit()
        """
        Adds a device entity into the database

        Args:
            :param id device Number
            :param state device state

        Raises:
            ValueError: If another device with the same ID already exists in the database
        """
        
    
    def getState(self, id : int) -> bool:
        """
        Returns the state of the device with the specific id

        Args:
            :param id of the device
        
        Return:
            :return the state of the device

        Raises:
            ValueError: If a device with the id doesn't exist
        """
        if(not self.contains(id)):
             raise ValueError(f"row with id {id} does not exist")
        self.cursor.execute(f"SELECT state FROM {Database.table_name} WHERE id = {id}")
        return self.cursor.fetchone()

    
    def remove(self, id : int) -> bool:

        """
        Drops a device with the passed in id

        Args:
        :param id of the device

        Return:
        :return True if the device was successfully dropped

        Return:
            :return True if device was successfully dropped
        """
        if(self.contains(id)):
            self.cursor.execute(f"Delete from {Database.table_name} where id={id}")
            self.con.commit()
            return True
        return False
    

    def setState(self, id: int, state: bool) -> bool:
        """
        Updates the state of the device with the passed in id

        Args:
            :param id of the device
            :param state of the device
        Return:
            :return True if the device was successfully updated
        Raises:
            ValueError: If a device with the id doesn't exist
        """
        if(not self.contains(id)):
             raise ValueError(f"row with id {id} does not exist")
        self.cursor.execute(f"UPDATE {Database.table_name} SET state = {state} WHERE id = {id}")
        self.con.commit()
        return True
    
    
    def getAllDevices(self) -> list:
        """
        Returns all the devices in the database

        Return:
            :return list of all the devices in the database
        """
        self.cursor.execute(f"SELECT * from {Database.table_name}")
        return self.cursor.fetchall()
        
        
        



    '''
        We will talk about next time:
        try-catch
        python formating
        parameter and return checking
        
    '''


'''
    What is PRIMARY KEY and UNIQUE?
    These are called "constraints". As the name implies, it creates a format that the column MUST follow. Common ones include:
    NOT NULL, CHECK (conditional like name.length > 3), DEFAULT (value), FOREIGN KEY ((column_name) REFERENCES table(column_name))
'''
'''
    Common SQL commands:
    INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...) {Add rows}

    SELECT column1, column2, ... FROM table_name WHERE conditional {Get columns when the row meets some conditional}

    UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE conditional {Sets colums to values when some row meets some conditional}

    DELETE FROM table_name WHERE condition {Delete row from column when some row meets some conditional}

    ALTER TABLE table_name ADD column_name datatype; {Adds column to existing table}
    ALTER TABLE table_name DROP COLUMN column_name; {Deletes column to existing table}

    DROP TABLE table_name {Deletes table}

'''
'''
    When the function takes a bunch of parameters, you can use multi-line strings (like this one with the 3 quotation marks)
    to seperate your paremeters in multiple lines for easy reading, such as the one below
'''
'''
    cursor.execute("create table tableName (id INTEGER, name TEXT, isOn INTEGER)") ->
    cursor.execute(\''' create table tableName (
        id INTEGER, 
        name TEXT, isOn INTEGER
        )
    \''') {You dont need \ it was just so I can put a multiline string in a multiline string}
'''
