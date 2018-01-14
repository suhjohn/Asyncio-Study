import asyncio

import datetime


async def display_date(loop, time):
    end_time = loop.time() + time
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1) >= end_time:
            break
        await asyncio.sleep(1)

if __name__=="__main__":
    sec = int(input("Input the amount of seconds you want the time to be printed: "))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(display_date(loop, sec))
    loop.close()
