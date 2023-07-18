import sqlite3


class RecordsDB:
    def __init__(self):
        self.connection = sqlite3.connect(".money_counter.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS records
                        (record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                         user_nm VARCHAR(100) NOT NULL,
                         operation_type VARCHAR(100) NOT NULL,
                         value INTEGER NOT NULL,
                         send_to INTEGER DEFAULT NULL,
                         record_added_dttm TIMESTAMP DEFAULT current_timestamp,
                         FOREIGN KEY(send_to) REFERENCES users(user_id));
                         ''')
        self.connection.commit()

    def insert(self, *args) -> None:  # args = (user_name, operation_type, value, [recipient])
        if args[1] == "send":  # type of transaction is "transfer money to another user"
            self.cursor.execute('''INSERT INTO records(user_nm, operation_type, value, send_to)
                                        VALUES (?, ?, ?, ?);''', args)
        else:
            self.cursor.execute('''INSERT INTO records(user_nm, operation_type, value)
                                        VALUES (?, ?, ?);''', args)
        self.connection.commit()

    def get_records(self, *args) -> list:  # args = (user_name)
        self.cursor.execute(''' SELECT
                                    r.record_added_dttm, r.operation_type, r.value, u.user_nm
                                FROM
                                    records r LEFT JOIN users u ON r.send_to = u.user_id
                                WHERE
                                    r.user_nm = (?)
                                ORDER BY
                                    r.record_added_dttm''', args)
        return self.cursor.fetchall()


records_db = RecordsDB()
