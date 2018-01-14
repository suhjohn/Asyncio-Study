import asyncio

"""
Basic chaining of coroutines with the async syntax

print_sum() coroutine is added to the loop where print_sum is waiting for compute() coroutine. 
"""


async def compute(x, y):
    print(f'computing {x} + {y}...')
    await asyncio.sleep(1.0)
    print(f'compute complete!')
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print(f'{x} + {y} = result')

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()