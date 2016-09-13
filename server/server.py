import logging
import bottle
import collections
import ast
import json
import sqlite3
import os

from bottle import Bottle, get, post, redirect, request, template

app = Bottle()

@app.get('/')
def index():
    redirect("/logs")


@app.get('/clients')
@app.get('/clients/<client_id>')
def show_clients(client_id=None):
    logging.basicConfig(level=logging.DEBUG)
    if client_id:
        with sqlite3.connect("data.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clients WHERE client_id=?", (client_id,))
            data = cursor.fetchone()

            cursor.close()

        if not data:
            bottle.abort(404, "Sorry, client not found.")

        return template('client', data=data)

    with sqlite3.connect("data.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, client_id, node, system, processor FROM clients")
        data = cursor.fetchall()
        cursor.close()

    return template('clients', clients=data)


@app.post('/clients')
def save_client():
    logging.basicConfig(level=logging.DEBUG)
    data = json.load(request.body, object_pairs_hook=collections.OrderedDict)
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO clients (client_id, cpu_count, node, platform, processor, system) VALUES (?, ?, ?, ?, ?, ?)", data.values())
        conn.commit()
        cursor.close()


@app.get('/logs')
@app.get('/logs/<client_id>')
def show_logs(client_id=None):
    logging.basicConfig(level=logging.DEBUG)

    if client_id:
        with sqlite3.connect("data.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM logs WHERE client_id=?", (client_id,))
            data = cursor.fetchall()
            cursor.close()

        # if not data:
        #     bottle.abort(404, "Sorry, you're lost!")

        return template("client_logs", client=client_id, logs=data)

    with sqlite3.connect('data.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, client_id, level, cpu_percent, memory_percent, system_cpu, num_threads, time FROM logs")
        data = cursor.fetchall()
        cursor.close()

    return template('logs', logs=data)


@app.post('/logs')
def save_logs():
    logging.basicConfig(level=logging.DEBUG)
    data = json.load(request.body, object_pairs_hook=collections.OrderedDict)

    client_id = data.pop(0)

    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        for row in data:
            row = ast.literal_eval(row)
            cursor.execute("INSERT INTO logs (client_id, level, cpu_percent, system_cpu, memory_percent, num_threads, time) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (client_id, row['level'], row['cpu_percent'], row['system_cpu'], row['memory_percent'], row['num_threads'], row['time']))
        conn.commit()
        cursor.close()


if __name__ == "__main__":
    bottle.debug(True)
    bottle.run(app=app, host='0.0.0.0', port=1337, reloader=True)
