"""
Implementation of tail -f in Python.

Takes a file handler, goes to the end of the file and read any new line that is added to the file.

Source: https://soooprmx.com/archives/5622
"""

import time


def follow(file):
    file.seek(0, 2) # go to the end of the file
    while True:
        line = file.readline() # requests for one line of text
        if not line:
            time.sleep(0.1)
            continue # Since there is no break for the while,
                     # The fuction will try to read whatever is added every 0.1 second
        yield line
