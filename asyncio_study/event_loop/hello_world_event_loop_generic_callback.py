import selectors
from bisect import insort
from collections import namedtuple
from time import time
from typing import List

import sys
from utils import timed_fib

"""
For each event type(stdin of fib n or timer every 3 second),
    user adds the corresponding function as event handler
"""

Timer = namedtuple('Timer', ['timestamp', 'handler'])

class EventLoop:
    """
    Implements a callback based single-threaded event loop

    source: http://sahandsaba.com/understanding-asyncio_study-node-js-python-3-4.html
    """

    def __init__(self, *tasks):
        self._running = False
        self._stdin_handlers: List[function] = []
        self._timers: List[Timer] = []
        self._selector = selectors.DefaultSelector()
        self._selector.register(sys.stdin, selectors.EVENT_READ)

    def run_forever(self):
        self._running = True
        while self._running:
            for key, mask in self._selector.select(0.1):
                line: str = key.fileobj.readline().strip()
                for callback in self._stdin_handlers:
                    callback(line)

            # While the current time has not exeeded the previous time + 3
            # (created by add timer from the callback), ignore.
            # Otherwise, execute the following sequence
            while self._timers and self._timers[0].timestamp < time():
                handler = self._timers[0].handler # print_hello() from main()
                del self._timers[0]
                handler()

    def add_stdin_handler(self, callback):
        self._stdin_handlers.append(callback)

    def add_timer(self, wait_time, callback):
        timer = Timer(timestamp=time() + wait_time, handler=callback)
        insort(self._timers, timer)

    def stop(self):
        self._running =False

def main():
    loop = EventLoop()

    def on_stdin_input(line):
        if line == 'exit':
            loop.stop()
            return
        n = int(line)
        print(f'fib({n}) = {timed_fib(n)}')

    def print_hello():
        """
        Takes current time and adds a timer to loop with +3 seconds to current time
        :return:
        """
        curr = int(time())
        print(f"{curr} - Hello world!")
        loop.add_timer(3, print_hello)

    def f(x):
        def g():
            print(x)
        return g

    loop.add_stdin_handler(on_stdin_input)
    loop.add_timer(0, print_hello)
    loop.run_forever()

if __name__ == '__main__':
    main()