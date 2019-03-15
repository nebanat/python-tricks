import asyncio
from concurrent.futures import ThreadPoolExecutor
# from functools import wraps


async def sync_to_async(func, param):
    """
    This function helps to run a synchronous function in an asynchronous context(manner)
    by spinning up a new thread and new event loop and returning control to the
    main event loop which listens and returns when it is finished

    :param func: synchronous function
    :param param: function parameter(s)
    :return:
    """
    executor = ThreadPoolExecutor(max_workers=1)
    event_loop = asyncio.get_event_loop()
    result = await event_loop.run_in_executor(executor, func, param)
    return result


def async_to_sync(func, param):
    """
    This function helps to run an asynchronous function in a synchronous context(manner)
    by spinning up an event loop and running to complete then returning the result
    of the function

    :param func: asynchronous function
    :param param: function parameter(s)
    :return:
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(func(param))
    return result

# writing in the form of a decorator
# async def sync_to_async_decorator(func):
#     @wraps(func)
#     async def sync_call(*args, **kwargs):
#         try:
#             executor = futures.ThreadPoolExecutor(max_workers=3)
#             event_loop = asyncio.get_event_loop()
#             result = await event_loop.run_in_executor(executor, func, *args)
#             return result
#         finally:
#             pass
#     return sync_call
