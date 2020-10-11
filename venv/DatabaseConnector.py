import mysql.connector

class DatabaseConnector:


    def __init__(self):
        self.connector = self.connectToServer()
        self.connector = self.connector.cursor

    def connectToServer(self):
        try:
            cnx = mysql.connector.connect(user='root',
            password='SmokingWalnut58',  # Some boilerplate I have, dont touch it
            host='127.0.0.1',
            database='stockProj', )
            return cnx

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                return cnx


t = DatabaseConnector()
t.connectToServer()
