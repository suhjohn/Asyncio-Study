from threading import Thread
from time import time, sleep

from utils import timed_fib


def print_hello():
    while True:
        curr = int(time())
        print(f"{curr} - Hello world!")
        sleep(3)

def read_input_and_fibonacci():
    while True:
        n = int(input())
        print(f'fib({n}) = {timed_fib(n)}')

def main():
    """
    Creates a new thread for the print_hello function
    :return:
    """
    # New Thread
    t = Thread(target=print_hello)
    t.daemon = True
    t.start()

    # Main Thread
    read_input_and_fibonacci()

if __name__=='__main__':
    main()