import mysql.connector as mysql
from mysql.connector import Error
import database.config as config

dataFile = 'storage/users_data.json'

class UserStorage:
    
    def __init__(self) -> None:
        self.connection = self.createConnection()

    # This function is to create a database connection
    def createConnection(self):
        try:
            connection = mysql.connect(
                host= config.host,
                user= config.user, 
                password= config.password,
                database= config.database,
                port = config.port
            )
            
            if connection.is_connected():
                return connection

        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
        return None
    
    # This function is finding user in database
    def loadUser(self,username):
        cursor = self.connection.cursor()
        query = "SELECT id, full_name, password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    # This function is save new user in database
    def saveUser(self,username,fullName,password):
        cursor = self.connection.cursor()
        query =  "INSERT INTO users (username, full_name, password) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (username, fullName, password))
            self.connection.commit()
            print('User created successfully!')
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()