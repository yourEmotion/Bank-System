import sqlite3


class RecordsDB:
    def __init__(self):
        try:
            self.connection = sqlite3.connect(".money_counter.sql")
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                      CREATE TABLE IF NOT EXISTS records
                        (record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                         user_nm VARCHAR(100) NOT NULL,
                         operation_type VARCHAR(100) NOT NULL,
                         value INTEGER NOT NULL,
                         send_to INTEGER DEFAULT NULL,
                         record_added_dttm TIMESTAMP DEFAULT current_timestamp);
                         ''')

        except sqlite3.Error:
            print("You have committed some cringe. Try again.")
            del self

    def insert(self, *args):
        try:
            if args[1] == "transfer":  # type of transaction is "transfer money to another user"
                self.cursor.execute('''INSERT INTO records(user_nm, operation_type, value, send_to)
                                    VALUES (?, ?, ?, ?);''', args)
            else:
                self.cursor.execute('''INSERT INTO records(user_nm, operation_type, value)
                                    VALUES (?, ?, ?);''', args)
            self.cursor.execute('''SELECT * FROM users;''')
            print(self.cursor)
            print(f"inserted {args[1]} with value = {args[2]}")
            self.connection.commit()
        except IndexError:
            print("You have committed some cringe. Try again.")
            self.cursor.execute('''SELECT * FROM users;''')

