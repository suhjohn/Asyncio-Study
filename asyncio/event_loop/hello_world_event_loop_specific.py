import selectors
from time import time

import sys
from utils import timed_fib


def read_input_and_fibonacci(stream):
    text = stream.readline()
    n = int(text.strip())
    print(f'fib({n}) = {timed_fib(n)}')

def print_hello():
    curr = int(time())
    print(f"{curr} - Hello world!")

def main():
    # Register the selector to poll for "read" readiness on stdin
    selector = selectors.DefaultSelector()
    selector.register(sys.stdin, selectors.EVENT_READ)
    last_hello = 0
    while True:
        for event, mask in selector.select(0.1):
            read_input_and_fibonacci(event.fileobj)
        if time() - last_hello > 3:
            last_hello = time()
            print_hello()

if __name__ == "__main__":
    main()