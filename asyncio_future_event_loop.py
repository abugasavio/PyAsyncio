import asyncio


def mark_done(future, result):
    print(f"setting future result to {result}")
    future.set_result(result)


event_loop = asyncio.get_event_loop()

try:
    all_done = event_loop.create_future()
    print('scheduling event loop')
    event_loop.call_soon(mark_done, all_done, 'the result')
    print('entering event loop')
    result = event_loop.run_until_complete(all_done)
    print(f'returned result {result}')
finally:
    event_loop.close()

print(f'future result {all_done.result()}')
