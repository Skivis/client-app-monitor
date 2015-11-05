import logging
import bottle
import collections
import ast
import json
import sqlite3

from bottle import get, post, redirect, request, template


@get('/')
def index():
    redirect("/logs")


@get('/clients')
@get('/clients/<client_id>')
def show_clients(client_id=None):
    if client_id:
        with sqlite3.connect("data.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM clients WHERE client_id=?", (client_id,))
            data = cursor.fetchone()
            cursor.close()

        if not data:
            bottle.abort(404, "Sorry, client not found.")

        return "<p>Statistics for client: %s</p>" % client_id

    with sqlite3.connect("data.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, client_id, platform FROM clients")
        data = cursor.fetchall()
        cursor.close()

    return template('clients', clients=data)


@post('/clients')
def save_client():
    logging.basicConfig(level=logging.DEBUG)
    data = json.load(request.body, object_pairs_hook=collections.OrderedDict)
    logging.info(data)
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO clients (client_id, platform) VALUES (?, ?)", data.values())
        conn.commit()
        cursor.close()


@get('/logs')
def show_logs():
    logging.basicConfig(level=logging.DEBUG)
    with sqlite3.connect('data.db') as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT client_id, level, cpu_percent, memory_percent, num_threads, time FROM logs")
        data = c.fetchall()
        c.close()

    return template('logs', logs=data)


@post('/logs')
def save_logs():
    logging.basicConfig(level=logging.DEBUG)
    data = json.load(request.body, object_pairs_hook=collections.OrderedDict)

    client_id = data.pop(0)

    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        for row in data:
            row = ast.literal_eval(row)
            cursor.execute("INSERT INTO logs (client_id, level, cpu_percent, memory_percent, num_threads, time) VALUES (?, ?, ?, ?, ?, ?)",
                           (client_id, row['level'], row['cpu_percent'], row['memory_percent'], row['num_threads'], row['time']))
        conn.commit()
        cursor.close()


if __name__ == "__main__":
    bottle.debug(True)
    bottle.run(host='0.0.0.0', port=1337, reloader=True)
