from flask import Flask, abort
import os
import psycopg2
from psycopg2.extras import RealDictCursor


app = Flask(__name__)

dbname = os.environ['POSTGRES_DB']
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = 'postgres_db'
port = '5432'

params = f'dbname={dbname} user={user} password={password} host={host} port={port}'
print(params)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path == '':
        con = psycopg2.connect(params)
        cur = con.cursor(cursor_factory=RealDictCursor)
        cur.execute('select * from test')
        data = cur.fetchall()
        con.close()
        return data, 200
    elif path == 'health':
        return {'status': 'OK'}, 200
    else:
        abort(404)


app.run(host='0.0.0.0', port=8000)
