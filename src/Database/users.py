import sqlite3


class UsersDB:
    def __init__(self):
        self.connection = sqlite3.connect(".money_counter.db")
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

    def insert(self, *args) -> None:  # args = (user_name, password, birthday)
        self.cursor.execute('''INSERT INTO users(user_nm, password, birthday)
                                VALUES (?, ?, ?);''', args)
        self.connection.commit()

    def update_balance(self, *args) -> None:  # args = (user_name, new_balance)
        self.cursor.execute('''UPDATE users
                               SET balance = (?)
                               WHERE user_nm = (?);''', (args[1], args[0]))
        self.connection.commit()

    def in_database(self, *args) -> bool:  # args = (user_name) or args = (user_name, password)
        if len(args) == 2:
            self.cursor.execute('''SELECT ((?, ?) IN
                                            (SELECT user_nm, password FROM users));''', args)
        elif len(args) == 1:
            self.cursor.execute('''SELECT ((?) IN
                                            (SELECT user_nm FROM users));''', args)
        return bool(self.cursor.fetchone()[0])

    def get_balance(self, *args) -> int:  # args = (user_name)
        self.cursor.execute('''SELECT balance FROM users
                                            WHERE user_nm = (?)''', args)
        return int(self.cursor.fetchone()[0])


users_db = UsersDB()