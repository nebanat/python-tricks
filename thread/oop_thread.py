import time
from threading import Thread
import socket


class CountDownTask:
    """
    represents an example of when you want to poll for a thread termination

    key notes:
    1. Polling for thread termination for threads that perform blocking operation such as I/O. for example
    a thread blocked indefinitely on an I/O operation may never return to check if its been killed. To deal with
    this case you will need to carefully program threads to use timeout loops see IOTask class below

    2.
    """
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


# carefully using timeout loops for threads that do I/O operation
class IOTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(5)
        while self._running:
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue


if __name__ == '__main__':
    c = CountDownTask()
    t = Thread(target=c.run, args=(10,))

    t.start()

    c.terminate()

    t.join()  # wait for actual termination if possible
