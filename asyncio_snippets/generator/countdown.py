"""
A simple generator function that prints counted down numbers according to user input.

Source: https://soooprmx.com/archives/5622
"""


def countdown(n):
    while n > 0:
        yield n
        n -= 1

if __name__=="__main__":
    n = int(input("input a number to count down from: "))
    for i in countdown(n):
        print(i, end =" ")