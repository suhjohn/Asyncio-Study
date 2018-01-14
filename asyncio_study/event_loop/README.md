# Event Loop

We will explore various methods of how "Event Loop" is implemented behind the scenes.
The code and the text all belongs to here: http://sahandsaba.com/understanding-asyncio-node-js-python-3-4.html
I have summarized the main points.

> An event loop essentially manages and distributes the execution of different tasks. It registers them and handles distributing the flow of control between them.
https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e

# Hello World Revisited

Let's start by writing a program to solve a very simple problem.
We will use this problem and minor variations of it for the rest of the section to demonstrate the ideas.<p></p>

> Write a program to print "Hello world!" every three seconds,
and at the same time wait for input from the user.
Each line of user input will contain a single positive number n.
As soon as input is entered, calculate and output the Fibonacci number F(n)
and continue to wait for more input.
Note that there's a chance the periodic "Hello world!" is inserted
in the middle of user input, but we do not care about that.
http://sahandsaba.com/understanding-asyncio-node-js-python-3-4.html

# Multi-Threaded
One thread continues executing "hello world" every 3 seconds,
and the other thread is open to take input whenever it is given to execute fibonacci.

# Task-Specific Event Loop
Uses only the main thread. It will execute hello world, and be blocked(waiting) for fibonacci.
Knowledge of `selectors` module is required.

> The selectors module was introduced in Python 3.4
to enable easy access to low-level asynchronous I/O operations.
Basically, it allows you to open and read from many files by using I/O multiplexing.<br>
> _Mastering Python pg.175_

Note that this is our first most basic "asynchronous" function. It executes one function(print hello_world every 3 seconds)
and hands over control to fibonacci when a stdinput comes in **in a single thread**.

However, while we are waiting for the result from fibonacci, **hello_world is blocked.**

# Generalized Event Loop - Callbacks
While the above event only works for this specific problem, we could use the idea
to expand it so that
whatever problem that has a "timer", or **some sort of repeating function**
and a "fibonacci" or a **function that takes a long time** can work.

We basically separate the specifics of the problem and the structure of the process.

The structure is made into a EventLoop class and we put the required functions(fib, hello_world) inside main().

The main() function creates a loop and basically just executes a while loop(in run_forever()).

The reason why we say this is a EventLoop using "callbacks" is because
it "calls back" the function that needs to be executed when it is the "right time", i.e. when an event needs to be executed
(in this case, when a stdinput comes in or when 3 seconds has passed from the previous time).

# Generalized Event Loop - Coroutines
More information on coroutines can be found here:

> This means that we can write our asynchronous code as coroutines,
and simply yield when we need to wait on an asynchronous operation.
To do this, we simply yield the task or other coroutine whose value we will need to continue.
code will then look very sequential and similar to synchronous code.
http://sahandsaba.com/understanding-asyncio-node-js-python-3-4.html


