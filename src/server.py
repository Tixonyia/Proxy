import asyncio
from src import proxy_data


async def handle_connection(reader, writer):
    addr = writer.get_extra_info("peername")
    print("\nConnected by", addr)
    while True:
        # Receive
        try:
            data = await reader.read(4086)  # буффер обмена при чтении от клиента
        except ConnectionError:
            # при дисконекте
            print(f"\nClient suddenly closed while receiving from {addr}")
            break
        print(f"Received {data} from: {addr}")
        if not data:
            break

        if data == b"close":
            break
        data = proxy_data.driver_chrom_respons_after_load(data)  # работа с html

        try:
            writer.write(data)  # Ответ клиенту

        except ConnectionError:
            print(f"\nClient suddenly closed, cannot send")
            break
    writer.close()
    print("\n Disconnected by", addr)


async def main(host, port):
    # Запуск сервера
    server = await asyncio.start_server(handle_connection, host, port)
    print(f"Start server...")
    async with server:
        await server.serve_forever()

HOST = ""  # Имя хоста
PORT = 50013  # Порт связи с сервером

if __name__ == "__main__":

    asyncio.run(main(HOST, PORT))
