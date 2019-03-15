import asyncio
import time
# from helpers import sync_to_async
from helpers_class import sync_to_async

loop = asyncio.get_event_loop()


# synchronous function
def get_chat_id(name):
    time.sleep(3)
    print("running " + name)


# asynchronous function
async def run_another_func(name):
    print("running " + name)


async def main():
    await asyncio.wait([
        sync_to_async(get_chat_id)('Django synchronous'),
        run_another_func('tornado asynchronous')
    ])

if __name__ == '__main__':
    print("started at %s" % time.strftime('%X'))
    loop.run_until_complete(main())
    loop.close()
    print("finished at %s" % time.strftime('%X'))
