# Asyncio

> This module provides infrastructure for writing single-threaded concurrent code using coroutines,
multiplexing I/O access over sockets and other resources,
running network clients and servers, and other related primitives.
https://docs.python.org/3/library/asyncio.html

> asyncio_study is the new concurrency module introduced in Python 3.4. It’s designed to use coroutines and futures to simplify asynchronous code and make it almost as readable as synchronous code simply because there are no callbacks.
https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e

> Async - A style of concurrent programming in which tasks release the CPU during waiting periods,
so that other tasks can use it.
_Miguel Grinberg Asynchronous Python for the Complete Beginner PyCon 2017_,
 https://www.youtube.com/watch?v=iG6fr81xHKA&t=1177s

# Key Concepts
0. Coroutines / Generators
1. Event Loop
2. Futures
3. Tasks


# 0. Coroutines / Generators
Fundamental idea behind Asyncio.

## Coroutines
https://github.com/suhjohn/Asyncio-Study/tree/master/asyncio_study/coroutines-generators/coroutines

# 0.5 Thread
Understanding of threads is required to grasp what an event loop is.

> Think of a thread as a single sequence of instructions and the CPU's current state in executing them (CPU state refers to e.g. register values, in particular the next instruction register).
_http://sahandsaba.com/understanding-asyncio-node-js-python-3-4.html'_

# 1. Event Loop
https://github.com/suhjohn/Asyncio-Study/tree/master/asyncio_study/event_loop

# 2. Futures
https://github.com/suhjohn/Asyncio-Study/tree/master/asyncio_study/futures

# 3. Tasks
https://github.com/suhjohn/Asyncio-Study/tree/master/asyncio_study/tasks

# Use Cases
Courtesy of _Practical Python Async for Dummies_, https://www.youtube.com/watch?v=5_K8GwZ_268

- Results At End
    - run an independent function multiple times
    - order doesn't matter
    - can be run simultaneously
    - "pure" functions are the best
    - you can wait till all the calls complete before looking at the results
- Results as we go
