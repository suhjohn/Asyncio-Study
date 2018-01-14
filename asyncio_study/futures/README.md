# Futures

> Futures are objects that represent the result of a task that may or may not have been executed. This result may be an exception.
https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e

> The asyncio_study.Future class is essentially a promise of a result; it returns the results
if they are available, and once it receives results,
it will pass them along to all the registered callbacks.
It maintains a state variable internally, which allows an outside party to mark a future as canceled.
_Mastering Python pg.172_

> Futures encapsulate pending operations so that they can be put in queues, their state of completion can be queried, and their results (or exceptions) can be retrieved when available.
_Fluent Python pg.511_


## Asyncio.futures vs concurrent.futures.Future

> There is also a .result() method, which works the same in both classes when the future is done:
it returns the result of the callable, or re-raises whatever exception might have been thrown when the callable was executed.
However, when the future is not done,
the behavior of the result method is very different between the two flavors of Future. <br>
In a concurrency.futures.Future instance, invoking f.result() will block the caller’s thread until the result is ready.
An optional timeout argument can be passed, and if the future is not done in the specified time, a TimeoutError exception is raised. <br>
In “asyncio_study.Future: Nonblocking by Design” on page 545,
we’ll see that the asyncio_study.Future.re sult method does not support timeout,
and the preferred way to get the result of futures in that library is to use yield from
which doesn’t work with concurrency.futures.Future instances. _Fluent Python pg.512_

Essentially, concurrent.futures.Future can be blocked(or "timed out") when the future is not done.

However, asyncio_study.Future isn't blocked. In addition, it is suggested to use yield from or **await** for Python 3.5 and above.