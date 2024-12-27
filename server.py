import os
import psycopg2
from flask import Flask, render_template
from config import config
from connect import connect
from waitress import serve

app = Flask(__name__)

def get_db_connection():
    conn = connect()
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM weather;')
    weather = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))  # Get port from env, default to 5000
    app.run(host='0.0.0.0', port=port)