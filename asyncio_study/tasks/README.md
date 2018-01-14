# Tasks

> schedulers for coroutines.
https://medium.freecodecamp.org/a-guide-to-asynchronous-programming-in-python-with-asyncio-232e2afa44f6

> A task is responsible for executing a coroutine object in an event loop.
If the wrapped coroutine yields from a future,
the task suspends the execution of the wrapped coroutine and
waits for the completion of the future. When the future is done,
the execution of the wrapped coroutine restarts with the result or
the exception of the future.
https://docs.python.org/3/library/asyncio-task.html#coroutine
