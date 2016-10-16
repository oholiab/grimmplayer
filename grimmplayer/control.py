import mpd
from contextlib import contextmanager

@contextmanager
def connection():
    try:
        client = mpd.MPDClient(use_unicode=True)
        client.connect('127.0.0.1', 6600)
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
