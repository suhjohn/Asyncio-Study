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

