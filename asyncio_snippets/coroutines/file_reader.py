"""
file_reader.py

An example of how coroutines can be utilized as pipelines.
This is a modified version of the code snippets from https://soooprmx.com/archives/5625.

The source uses an example of follow where it will go to the end of the file(in this case a log)
and everytime a new line is added to a log, check if it matches certain conditions delineated by grepper/greppers,
and if it does, prints using the printer().

However, for demonstrating purposes, I didn't want to make an actual log reader since it would require a client of some sort
and instead wanted a working version of what coroutine is, how it all falls together.

The print statements in each of the function was put to see how the function call happens.
You can uncomment them to see how it works too.

-----------------

This file will take a file as user input with default log.txt.
Then, it will ask for what type of execution of coroutines you want to see.
Direct will simply read through the lines in the text,
Grepper will add a gateway in which it will check if the line contains the keyword.
Broadcast will add multiple gateways in which it will check if the line contains any of the keywords.


GREPPER
You can perhaps restrict what gets sent to the end coroutine by having a "gateway" of some sort.
This is what grepper() does.

BROADCAST
The gateway accepts only one condition. If we want to allow multiple conditions that uses the same gateway logic,
we could perhaps try using many gateways.
"""
import time
from functools import wraps
from typing import Callable, Generator, List


def coroutine(func):
    @wraps(func)
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


def follow(file, target: Generator=None):
    # file.seek(0, 2)
    while True:
        line = file.readline().strip('\n')
        if not line:
            time.sleep(0.1)
            continue
        # If there is a target,
        # Send the line(the line that we read from the file)
        #   TO the target.
        # Else, return the line.
        if target:
            # print(f"FOLLOW: sent to target function {target}")
            yield target.send(line)
        else:
            yield line
        # print('-----')

@coroutine
def grepper(word: str, target: Generator=None):
    """
    A coroutine that takes a word.
    If the sent value(line) has the word,
    then it sends the line to the target coroutine.

    If target coroutine is not given, just yields the word.
    :param word:
    :param target:
    :return:
    """
    line = yield
    while True:
        if word in line:
            if target:
                # print(f"GREPPER: sent to target function {target}")
                line = yield target.send(line)
            else:
                line = yield line
        else:
            # print(f"GREPPER: '{word}' not in '{line}'")
            line = yield line



@coroutine
def broadcast(targets: List[Generator]):
    """
    A coroutine that takes a list of coroutines.
    It can be sent values which can then send it to each of the coroutine in the list.
    :param targets:
    :return:
    """
    while True:
        msg: str = yield
        for t in targets:
            # print(f"BROADCAST: sent to target function {t}")
            t.send(msg)


@coroutine
def printer():
    while True:
        line = yield
        print(f'\nPRINT: {line}')


# --------- main functions

def main_direct(file):
    prn = printer()
    loglines = follow(file, prn)
    for _ in loglines:
        pass


def main_grepper(file):
    prn = printer()
    keyword = 'Failed'
    grep = grepper(keyword, prn)
    log_lines = follow(file, grep)
    for _ in log_lines:
        pass


def main_broadcast(file):
    prn = printer()
    keywords = ('Failed', 'Could not')
    filters = [grepper(keyword, prn) for keyword in keywords]
    caster = broadcast(filters)
    log_lines = follow(file, caster)
    for _ in log_lines:
        pass


if __name__ == "__main__":
    main_functions = {"direct": main_direct,
                      "grepper": main_grepper,
                      "broadcast": main_broadcast}
    file = input("Enter the name of the file. If you don't enter any file, "
                 "the default file in this folder 'log.txt' will be used. "
                 "You can create a new file and input that file instead too: ")
    if not file:
        file = "log.txt"
    file = open(file)
    while True:
        function_type = input("Enter the type of main you want to execute. "
                              "Options: direct, grepper, broadcast: ")
        if function_type == "direct" or function_type == "grepper" or function_type == "broadcast":
            main_functions[function_type](file)
            break
