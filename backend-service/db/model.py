
import sqlite3


class Model:

    TABLE_NAME = "relays"

    def __init__(self):
        self.connection = sqlite3.connect("all_relays.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {Model.TABLE_NAME} (relayID INTEGER PRIMARY KEY, relayState INTEGER)")
        self.connection.commit()

    def checkIfRelayExists(self, id: int) -> bool:
        self.cursor.execute(f"SELECT 1 FROM {Model.TABLE_NAME} WHERE relayID='{id}';")
        ret = self.cursor.fetchone()
        return bool(ret)

    def addRelay(self, id: int, state: bool):
        if self.checkIfRelayExists(id):
            return False
        self.cursor.execute(f"INSERT INTO {Model.TABLE_NAME} VALUES ('{id}', '{state}')")
        self.connection.commit()
        return True

    def getRelayState(self, id: int):
        if not (self.checkIfRelayExists(id)):
            raise ValueError("Relay does not exist")
        self.cursor.execute(
            f"SELECT relayState FROM {Model.TABLE_NAME} WHERE relayID='{id}'")
        self.connection.commit()
        return bool(self.cursor.fetchone()[0])

    def dropRelay(self, id: int):
        if not (self.checkIfRelayExists(id)):
            return False
        self.cursor.execute(
            f"DELETE FROM {Model.TABLE_NAME} WHERE relayID='{id}'")
        self.connection.commit()
        return True

    def updateRelayState(self, state: bool, id: int):
        if not (self.checkIfRelayExists(id)):
            raise ValueError("Relay does not exist")
        self.cursor.execute(
            f"UPDATE {Model.TABLE_NAME} SET relayState='{state}' WHERE relayID='{id}'")
        self.connection.commit()
        return True

    def getAllRelays(self):
        self.cursor.execute(f"SELECT * FROM {Model.TABLE_NAME}")
        self.connection.commit()
        return self.cursor.fetchall()

    def clearAll(self):
        self.cursor.execute(f"DELETE FROM {Model.TABLE_NAME}")
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {Model.TABLE_NAME} (relayID INTEGER PRIMARY KEY, relayState INTEGER)")
        self.connection.commit()
