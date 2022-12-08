import sqlite3 as sql
#import pynacl 
from encryption import encrypt
import string

class Dbase:
    '''
        This class will store user data in a sqlite3 database and the passwords will be encrypted
    
    '''

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sql.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
        self.conn.commit()
    
    def insert(self, username, password):
        password = encrypt(password)
        self.cur.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        return rows
    def login(self, username, password):
        password = encrypt(password)
        self.cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        rows = self.cur.fetchall()
        return True if rows else False
    
    def username_exists(self, username):
        self.cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        rows = self.cur.fetchall()
        return True if rows else False
    
    def weak_password(self, password):
        if len(password) < 8 or password.isalpha() or password.isdigit():
            # check if it has special characters
            for char in password:
                if char not in string.ascii_letters + string.digits:
                    return False
            return True
        else:
            return False
    def delete(self, username):
        self.cur.execute("DELETE FROM users WHERE username = ?", (username,))
        self.conn.commit()
    



dbase = Dbase("users.db")



