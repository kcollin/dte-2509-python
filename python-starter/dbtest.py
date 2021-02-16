
#MySQL connector må være installert
#Kommando i terminalvindu: pip install mysql-connector-python

import mysql.connector
from flask import Flask, render_template, request, escape
dbconfig = { 'host': 'kark.uit.no',
    'user': 'test_v19',
    'password': '*****',
    'database': 'test_v19', }
app = Flask(__name__)
@app.route('/')

def hello() -> 'html':
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """SELECT id, givenName, lastName, email, studyProgram FROM student_v21""";
    cursor.execute(_SQL)
    result = cursor.fetchall()
    return render_template('students.html',
                           students= result)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    app.run()
