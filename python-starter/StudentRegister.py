import mysql.connector
from mysql.connector import errorcode

class StudReg:

    def __init__(self) -> None:
        dbconfig = {'host': 'kark.uit.no',
                    'user': 'test_v19',
                    'password': '$py@uit-v21',
                    'database': 'test_v19', }
        self.configuration = dbconfig

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def visAlle(self):
        try:
            self.cursor.execute("SELECT * FROM student_v21 ORDER BY lastName ASC");
            result = self.cursor.fetchall()
        except mysql.connector.Error as err:
                print(err)

        return result