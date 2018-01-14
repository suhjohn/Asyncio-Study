import asyncio

async def factorial(number):
    result = 1
    for i in range(2, number+1):
        print(f"Task for {number}: Compute factorial: {i}")
        await asyncio.sleep(1)

        result *= i
    print(f'Task for {number} finished. Factorial({number}) = {result}')

loop = asyncio.get_event_loop()


'''
Method using async.gather in https://docs.python.org/3/library/asyncio-task.html#future

loop.run_until_complete(asyncio.gather(
    factorial(2),
    factorial(3),
    factorial(4),
))
loop.close()
'''

tasks = [loop.create_task(factorial(i)) for i in range(2, 5)]
wait_tasks = asyncio.wait(tasks)
loop.run_until_complete(wait_tasks)
loop.close()
