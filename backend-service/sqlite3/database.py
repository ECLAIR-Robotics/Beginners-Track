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
            self.cursor.execute(f"CREATE TABLE {Database.table_name} (id INTEGER PRIMARY KEY, state bool);") # Uncomment this line and fill out thing 
            print(f"The table '{self.table_name}' is online and instantiated ")
        
    
    def contains(self, id : int) -> bool:
        """
        Return
            :return True if a device entity with the 'id' exists
        """
        self.cursor.execute(f"SELECT id FROM {Database.table_name} WHERE id={id}")
        

    def add(self, id : int, state : bool, name, description):
        self.cursor.execute(f"insert into {Database.table_name} (id,state,name,description) values({id},{state}, {name}, {description})")
        print("Umer is the best boss")
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
    
    
    def getAllDevices(self) -> list:
        """
        Returns all the devices in the database

        Return:
            :return list of all the devices in the database
        """
        

    


    '''
        We will talk about next time:
        try-catch
        python formating
        parameter and return checking
        
    '''


