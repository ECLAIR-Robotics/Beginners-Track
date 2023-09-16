import sqlite3

class Model:

    def __init__(self, database_name) -> None:
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE relays(relayID, relayState)")

    def checkIfRelayExists(self, id: int):
        self.cursor.execute("SELECT relayID FROM relays WHERE relayID=?", (id))
        return bool(self.cursor.fetchone())
    
    def addRelay(id: int, state: bool, self):
        if self.checkIfRelayExists(id):
            raise ValueError("Relay already exists")
        self.cursor.execute("INSERT INTO relays (relayID, relayState) VALUES (?,?)", (id, state))
        self.connection.commit()

    def getRelayState(self, id: int):
        self.cursor.execute("SELECT relayState FROM relays WHERE relayID=?", (id))
        return self.cursor.fetchone()
    
    def dropRelay(self, id: int):
        self.cursor.execute("DELETE FROM relays WHERE relayID=?", (id))
        self.connection.commit()
    
    def updateRelayState(self, state: bool, id: int):
        self.cursor.execute("SELECT relayID FROM relays WHERE relayID=?", (id))
        try:
            self.cursor.execute("UPDATE relays SET relayState=? WHERE relayID=?", (state, id))
            self.connection.commit()
        except ValueError:
            print("Relay does not exist")
    
    def getAllRelays(self):
        self.cursor.execute("SELECT * FROM relays")
        return self.cursor.fetchall()
