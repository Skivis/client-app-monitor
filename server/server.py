import bottle
from bottle import get, post, redirect


@get('/')
def index():
    if not logged_in():
        redirect('/login')
    else:
        redirect("/logs", code=None)


@get('/clients')
@get('/clients/<client_id>')
def show_clients(client_id=None):
    if not logged_in():
        redirect('/login')
    if client_id is not None:
        return "<p>Statistics for client: %s</p>" % client_id
    return "<p>All Clients</p>"


@post('/clients')
def save_client():
    # save client info to db
    pass


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
