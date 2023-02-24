import asyncio
import sys
import time

SCRIPTS = [
    'server.py',
    'client.py'
]


async def waiter(sc, p):
    # Функция которая вернет имя скрипта после ожидания
    await p.wait()
    return sc, p


async def main():
    waiters = []

    # Запуск
    for sc in SCRIPTS:
        p = await asyncio.create_subprocess_exec(sys.executable, sc)
        time.sleep(0.5)  # для последовательного вывода в консоли
        waiters.append(asyncio.create_task(waiter(sc, p)))

    # Ожидание
    while waiters:
        done, waiters = await asyncio.wait(waiters, return_when=asyncio.FIRST_COMPLETED)
        for w in done:
            sc, p = await w
            print('Done', sc)


if __name__ == "__main__":
    asyncio.run(main())
