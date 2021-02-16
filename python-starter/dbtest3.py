
#MySQL connector må være installert
#Kommando i terminalvindu: pip install mysql-connector-python

from flask import Flask, render_template
from StudentRegister import StudReg

app = Flask(__name__)

@app.route('/')

def hello() -> 'html':

    with StudReg() as db:
        result = db.visAlle()
    return render_template('students.html',
                           students= result)

if __name__ == "__main__":
    app.run(debug=True)
