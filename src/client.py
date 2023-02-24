# Запуск имитации клиента.
import socket
import re
import time

HOST = "localhost"  # Имя хоста
PORT = 50013  # Порт связи с сервером
IS_RECONNECT_ENABLED = False

if __name__ == "__main__":
    is_started = False
    while IS_RECONNECT_ENABLED or not is_started:
        is_started = True
        print()
        print("Create client")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:  # создание сокета
            sock.connect((HOST, PORT))  # подключение к серверу
            print("Client connected")
            while True:
                bufer = 4098  # размер буфера на приём в байтах
                # Input
                time.sleep(0.5)  # Что вывод был последователен при подключении из main.py.
                data = input("Type the message to send:")
                if data == "exit":
                    print("Close by client")
                    break
                # Отправка данных на сервер.
                data_bytes = data.encode()
                sock.sendall(data_bytes)
                # Приём данных
                data_bytes = sock.recv(bufer)
                data = data_bytes.decode()
                # определение размера данных
                size_buffer = re.search(r'\d+', data).group(0)
                # дискретный приём данных
                for i in range((int(size_buffer) // bufer)):
                    data_bytes = sock.recv(bufer)
                    data += data_bytes.decode()
                # удаление строки длины из данных
                data = re.sub(r'\d+', '', data, 1)
                # запись в файл. В реале заменить на открытие через браузер.
                with open('result_html.html', 'w') as file:
                    file.write(data)
                print('Look for data in a file: "result_html.html"')
                if not data:
                    print("Closed by server")
                    break
            # Закрыть сокет при дисконекте.
            sock.close()
            print("Client disconnected")
