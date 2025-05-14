#!/usr/bin/env python3

"""Модуль для запуска веб-приложения с использованием библиотеки WebView."""

import os
import webview

TITLE = "Launcher"


# --------------------------------------------------
def read_index():
    """Функция для чтения содержимого файла index.html"""
    file_path = os.path.join(os.getcwd(), "resources", "index.html")
    try:
        with open("resources/index.html", "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Ошибка: не удалось открыть файл '{file_path}'")
        return ""  # Возвращаем пустую строку в случае ошибки


# --------------------------------------------------
def main():
    """Основная функция для запуска веб-просмотра"""
    # Создаем окно веб-лаунчера
    webview.create_window(TITLE, html=read_index(), width=1280, height=720)
    webview.start()  # Запускаем веб-лаунчера


# --------------------------------------------------
if __name__ == "__main__":
    main()
