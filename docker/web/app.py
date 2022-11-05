from flask import Flask, request
import os
import psycopg2
from psycopg2.extras import RealDictCursor


app = Flask(__name__)
http_methods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'PATCH', 'CONNECT', 'OPTIONS', 'TRACE']

dbname = os.environ['POSTGRES_DB']
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = 'postgres_db'
port = '5432'

params = f'dbname={dbname} user={user} password={password} host={host} port={port}'


@app.route('/', defaults={'path': ''}, methods=http_methods)
@app.route('/<path:path>', methods=http_methods)
def catch_all(path):
    if request.method != 'GET':
        return '', 404

    if path == '':
        try:
            con = psycopg2.connect(params)
        except psycopg2.OperationalError as e:
            app.logger.error(e)
            return '', 404
        else:
            cur = con.cursor(cursor_factory=RealDictCursor)
            cur.execute('select * from test')
            data = cur.fetchall()
            cur.close()
            con.close()
            return data, 200
    elif path == 'health':
        return {'status': 'OK'}, 200
    else:
        return '', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
