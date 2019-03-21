import asyncio

loop = asyncio.get_event_loop()


async def update_spreadsheet():
    print('Hello I am in the spreadsheet')
    # requester_email = await sync_to_async(HotDeskRequest.query_().filter_by)(
    #     hot_desk_ref_no=hot_desk_ref_no).first().email
    await asyncio.sleep(2)

    # requester_name = await sync_to_async(User.query_().filter_by)(email=requester_email).first().name
    await asyncio.sleep(2)

    print('Hello I am out of the spreadsheet')


async def get_response():
    print('hello I am in the response')
    print(dict(text='Hello response'))


async def update_spreadsheet_handler():
    await asyncio.wait([
        update_spreadsheet(),
        get_response()
    ])


def run_update():
    loop.run_until_complete(update_spreadsheet_handler())
    loop.close()


if __name__ == '__main__':
    run_update()

