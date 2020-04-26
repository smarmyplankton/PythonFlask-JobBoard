from flask import Flask, render_template, g
import sqlite3

application = app = Flask(__name__)

def open_connection():
    getattr(g, connection[_connection, None])
    if connection == None:
        connection = sqlite3.connect(PATH)
        g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return(connection)

def execute_sql():
    connection = open_connection()
    values = ()
    commit = False
    single = False
    cursor = connection.execute(values, sql, values)
    if commit == True:
        results = connection.commit()
    else:
        if single == True:
            cursor.fetchone()
        else:
            cursor.fetchall()
    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    getattr(g, connection[_connection, None])
    if connection != None:
        connection.close()



@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template('index.html')