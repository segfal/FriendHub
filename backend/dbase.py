from encryption import encrypt
import string
import psycopg2 as pgres


class Dbase:
    '''
        This class will store user data in a postgres database and the passwords will be encrypted
    
    '''

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = pgres.connect(database=self.db_name, user="postgres", password="postgres")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
        self.conn.commit()
    
    def insert(self, username, password):
        #password = encrypt(password)
        #insert value if username does not exist
        
        if self.username_exists(username):
            return False
        self.cur.execute("INSERT INTO users VALUES (%s, %s)", (username, password))
        self.conn.commit()
        return True

    
    def view(self):
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        return rows
    
    def login(self, username, password):
        #password = encrypt(password)
        rows = self.cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        print(rows)
        return True
    def username_exists(self, username):
        self.cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        rows = self.cur.fetchall()
        self.conn.commit()
        
        return True if rows else False
    def get_data(self,username,password):
        find_user = ("SELECT * FROM users WHERE username = %s AND password = %s")
        self.cur.execute(find_user,[(username),(password)])
        results = self.cur.fetchall()
        return results
    def weak_password(self, password):
        if len(password) < 8 or password.isalpha() or password.isdigit():
            # check if it has special characters
            for char in password:
                if char not in string.ascii_letters + string.digits:
                    return False
            return True
        else:
            return False    
    def delete_everything(self):
        self.cur.execute("DELETE FROM users")
        self.conn.commit()
        return True



    




dbase = Dbase("postgres")
