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
