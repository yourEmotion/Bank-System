import sqlite3


class UsersDB:
    def __init__(self):
        try:
            self.connection = sqlite3.connect(".money_counter.sql")
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                      CREATE TABLE IF NOT EXISTS users
                        (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                         user_nm VARCHAR(100) NOT NULL UNIQUE,
                         password VARCHAR(100) NOT NULL,
                         birthday DATE NOT NULL,
                         balance NUMERIC DEFAULT 0,
                         join_dttm TIMESTAMP DEFAULT current_timestamp);
                         ''')

        except sqlite3.Error:
            print("You have committed some cringe. Try again.")
            del self

    def insert(self, *args):  # args = (user_name, password, birthday)
        try:
            self.cursor.execute('''INSERT INTO users(user_nm, password, birthday)
                                VALUES (?, ?, ?);''', args)
            print(f"inserted username '{args[1]}'")
        except sqlite3.IntegrityError:
            print("This user already exists!")
        self.cursor.execute('''SELECT * FROM users;''')
        print(self.cursor.fetchmany(10))
        self.connection.commit()

    def update_balance(self, *args):  # args = (user_name, new_balance)
        self.cursor.execute('''UPDATE users
                               SET balance = (?)
                               WHERE user_nm = (?);''', (args[1], args[0]))
        self.connection.commit()
        print("updated!")
        self.cursor.execute('''SELECT * FROM users;''')
        print(self.cursor.fetchmany(10))

    def in_database(self, *args):  # args = (user_name, password)
        self.cursor.execute('''SELECT ((?, ?) IN
                              (SELECT user_nm, password FROM users));''', args)
        return bool(self.cursor.fetchone()[0])


users_db = UsersDB()

users_db.insert("ermachine", "qwerty", "2003-12-16")
users_db.insert("ermachine2", "qqq", "2023-01-01")