# Client Application Monitor

A tiny experimental monitoring tingy that monitors a client applications CPU usage and sends the gathered information to a server.

## Dependencies

The client-part uses the psutil library to fetch cpu and related process information. It's available via pip:
```bash
$ pip install psutil
```

The web server part uses a micro web-framework called *Bottle* and is also availabla via pip:
```bash
$ pip install bottle
```

## How to run?

First launch the server:
```bash
python server.py
```
and then run the database setup script:
```bash
python dbsetup.py
```
and finally launch the client

```bash
python client.py
```
