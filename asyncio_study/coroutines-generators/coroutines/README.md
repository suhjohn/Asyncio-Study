# Coroutines

> Coroutines are subroutines that offer non-pre-emptive multitasking through multiple entry points.
_Mastering Python pg.154_

> A coroutine is syntactically like a generator: just a function with the yield keyword in its body.
However, in a coroutine, yield usually appears on the right side of an expression
(e.g., datum = yield), and it may or may not produce a value —
if there is no expression after the yield keyword, the generator yields None.
The coroutine may receive data from the caller, which uses .send(datum) instead
of next(...) to feed the coroutine. Usually, the caller pushes values into the coroutine.
_Fluent Python pg.463_

> A coroutine is a function that can "return" while still remembering the state in which it is returning (value of local variables, and what the next instruction should be). This will then allow the coroutine to be called again, which results in it continuing from where it left off.
_http://sahandsaba.com/understanding-asyncio-node-js-python-3-4.html_

> generator that consumes data, but doesn’t generate it.
https://medium.freecodecamp.org/a-guide-to-asynchronous-programming-in-python-with-asyncio-232e2afa44f6

## In the context of asyncio

> Coroutines used with asyncio may be implemented using the async def statement, or by using generators. The async def type of coroutine was added in Python 3.5, and is recommended if there is no need to support older Python versions.
https://docs.python.org/3/library/asyncio-task.html#coroutine

Coroutines can do the following:

- `result = await future` or `result = yield from future` – suspends the coroutine until the future is done, then returns the future’s result, or raises an exception, which will be propagated. (If the future is cancelled, it will raise a CancelledError exception.) Note that tasks are futures, and everything said about futures also applies to tasks.
- `result = await coroutine` or `result = yield from coroutine` – wait for another coroutine to produce a result (or raise an exception, which will be propagated). The coroutine expression must be a call to another coroutine.
- `return expression` – produce a result to the coroutine that is waiting for this one using await or yield from.
- `raise exception` – raise an exception in the coroutine that is waiting for this one using await or yield from.

