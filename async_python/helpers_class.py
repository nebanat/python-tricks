import asyncio
import functools
import threading
from concurrent.futures import Future, ThreadPoolExecutor

try:
    import contextvars  # python 3.7+ only
except ImportError:
    contextvars = None


class AsyncToSync:
    def __init__(self, awaitable):
        self.awaitable = awaitable
        try:
            self.main_event_loop = asyncio.get_event_loop()
        except RuntimeError:
            self.main_event_loop = getattr(
                SyncToAsync.threadlocal, "main_event_loop", None
            )

    def __call__(self, *args, **kwargs):
        try:
            event_loop = asyncio.get_event_loop()
        except RuntimeError:
            pass
        else:
            if event_loop.is_running():
                raise RuntimeError(
                    "You cannot use AsyncToSync in the same thread as an async event loop - "
                    "Just await the async function directly"
                )
        call_result = Future()
        if not (self.main_event_loop and self.main_event_loop.is_running()):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                loop.run_until_complete(self.main_wrap(args, kwargs, call_result))
            finally:
                try:
                    if hasattr(loop, "shutdown_asyncgens"):
                        loop.run_until_complete(loop.shutdown_asyncgens())
                finally:
                    loop.close()
                    asyncio.set_event_loop(loop)
        else:
            self.main_event_loop.call_soon_threadsafe(
                self.main_event_loop.create_task,
                self.main_wrap(args, kwargs, call_result)
            )
        return call_result.result()

    def __get__(self, parent, objtype):
        return functools.partial(self.__call__, parent)

    async def main_wrap(self, args, kwargs, call_result):
        try:
            result = await self.awaitable(*args, **kwargs)
        except Exception as e:
            call_result.set_exception(e)
        else:
            call_result.set_result(result)


class SyncToAsync:
    """
        Utility class which turns a synchronous callable into an awaitable that
        runs in a threadpool. It also sets a threadlocal inside the thread so
        calls to AsyncToSync can escape it.
    """
    loop = asyncio.get_event_loop()
    loop.set_default_executor(
        ThreadPoolExecutor(max_workers=1)
    )

    threadlocal = threading.local()

    def __init__(self, func):
        self.func = func

    async def __call__(self, *args, **kwargs):
        loop = asyncio.get_event_loop()

        if contextvars is not None:
            context = contextvars.copy_context()
            child = functools.partial(self.func, *args, **kwargs)
            func = context.run
            args = (child,)
            kwargs = {}
        else:
            func = self.func

        future = loop.run_in_executor(
            None, functools.partial(self.thread_handler, loop, func, *args, **kwargs)
        )

        return await asyncio.wait_for(future, timeout=None)

    def __get__(self, parent, objtype):
        return functools.partial(self.__call__, parent)

    def thread_handler(self, loop, func, *args, **kwargs):
        self.threadlocal.main_event_loop = loop
        return func(*args, **kwargs)


sync_to_async = SyncToAsync
async_to_sync = AsyncToSync
