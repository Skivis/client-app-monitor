# Client Application Monitor

A tiny experimental monitoring tingy that monitors a client applications CPU usage and sends the gathered information to a server.

## Screenshot
![Screenshot](https://raw.githubusercontent.com/Skivis/client-app-monitor/master/server/screenshot.png)

## Dependencies

 - [psutil](https://pythonhosted.org/psutil/)
 - [bottle](http://bottlepy.org/)

```bash
$ pip install psutil
```

```bash
$ pip install bottle
```

## Usage?

Run the db setup script:
```bash
python dbsetup.py
```
Launch the server: (and browse to http://localhost:1337/)
```bash
python server.py
```
and finally launch the client

```bash
python client.py -n "skype"
```
where -n is simply the process name you want to monitor i.e "skype", "Dropbox", "Spotify" or whatever application you want to monitor.
