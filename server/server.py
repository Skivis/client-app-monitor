import logging
import bottle
import collections
import json
import sqlite3

from bottle import get, post, redirect, request, template


@get('/')
def index():
    if not logged_in():
        redirect('/login')
    else:
        redirect("/logs")


@get('/clients')
@get('/clients/<client_id>')
def show_clients(client_id=None):
    if not logged_in():
        redirect('/login')
    if client_id is not None:
        return "<p>Statistics for client: %s</p>" % client_id

    return "<p>All Clients</p>"


@get('/clients')
@get('/clients/<client_id>')
def show_clients(client_id=None):
    if not logged_in():
        redirect('/login')
    if client_id is not None:
        return "<p>Statistics for client: %s</p>" % client_id

    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT id, client_id, platform FROM clients")
    result = c.fetchall()
    c.close()

    return template('clients', clients=result)


@post('/clients')
def save_client():
    logging.basicConfig(level=logging.DEBUG)

    data = json.load(request.body, object_pairs_hook=collections.OrderedDict)

    logging.info(data)

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO clients (client_id, platform) VALUES (?, ?)", data.values())
    conn.commit()
    c.close()


@get('/logs')
def show_logs():
    # show all logs
    if not logged_in():
        redirect('/login')
    return "<p>All logs</p>"


@post('/logs')
def save_logs():
    # save logs to db
    pass


@get('/login')
def login_view():
    if not logged_in():
        return "<p>Login here</p>"
    else:
        redirect('/logs')


def logged_in():
    return True


if __name__ == "__main__":
    bottle.debug(True)
    bottle.run(host='0.0.0.0', port=1337, reloader=True)
