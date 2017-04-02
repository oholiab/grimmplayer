import mpd
from contextlib import contextmanager

inc = 5

@contextmanager
def connection():
    try:
        client = mpd.MPDClient(use_unicode=True)
        client.connect('localhost', 6600)
        yield client
    finally:
        client.close()
        client.disconnect()

def getvol(client):
    return int(client.status()["volume"])

def togglePlay():
    with connection() as client:
        if client.status()['state'] == 'play':
            client.pause()
        else:
            client.play()

def skip():
    with connection() as client:
        client.next()

def previous():
    with connection() as client:
        client.previous()

def vol_inc(increment):
    with connection() as client:
        volume = getvol(client)
        newvol = volume + increment
        if newvol > 100:
            newvol = 100
        elif newvol < 0:
            newvol = 0
        client.setvol(newvol)

def vol_up():
    vol_inc(inc)

def vol_down():
    vol_inc(-inc)
