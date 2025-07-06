from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="database-1.c2f46y28s2vw.us-east-1.rds.amazonaws.com",
    user="admin",
    password="Test#123",
    database="myprojectdb"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    cursor = db.cursor()
    cursor.execute("SELECT userid, username FROM users")
    data = cursor.fetchall()
    return render_template('users.html', users=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

