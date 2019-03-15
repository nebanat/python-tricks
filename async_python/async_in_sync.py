import asyncio

# from helpers import async_to_sync
from helpers_class import async_to_sync


async def get_chat_id(name):
    await asyncio.sleep(3)
    return "chat-%s" % name


def main():
    result = async_to_sync(get_chat_id)("django")
    print(result)


if __name__ == '__main__':
    main()
