#!/usr/bin/env python3

"""
TCP/IP сервер, ожидающий входящее соединение от клиентов.
Отсылает обратно принятое сообщение с комментарием.
"""

import socket

HOST = "127.0.0.1"  # Локальный хост
PORT = 65432  # Произвольный номер порта

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Привязываем адрес и порт
    s.listen()  # Начинаем слушать входящее соединение
    conn, addr = s.accept()  # Ждем первого подключения
    with conn:
        print(f"Подключился клиент: {addr}")
        while True:
            data = conn.recv(1024)  # Читаем данные
            if not data:
                break  # Закрываем соединение, если ничего не получено

            # Формируем ответ, добавляем к сообщению префикс
            RESPONSE = f"Вы отправили: {data.decode('utf-8')}".encode("utf-8")

            # Отвечаем клиенту оригинальным сообщением с преамбулой
            conn.sendall(RESPONSE)
