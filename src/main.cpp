#include <webview/webview.h>
#include <iostream>
#include <fstream>
#include <string>

std::string title = "Launcher";

// Функция для чтения содержимого файла index.html
std::string readIndex()
{
    std::ifstream in("resources/index.html");
    // Проверяем, удалось ли открыть файл
    if (!in) {
        std::cerr << "Ошибка: не удалось открыть файл resources/index.html" << std::endl;
        return ""; // Возвращаем пустую строку в случае ошибки
    }

    // Резервируем память для строки, чтобы избежать многократного выделения
    std::string content;
    content.reserve(1024 * 1024); // Предполагаем, что файл не превышает 1 МБ

    std::string line;
    // Читаем файл построчно и добавляем в строку
    while (std::getline(in, line)) {
        content += line; // Конкатенация строк
    }

    return content; // Возвращаем содержимое файла
}

int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrevInst, LPSTR lpCmdLine, int nCmdShow)
{
    webview::webview wview(false, nullptr);
    wview.set_title(title); // Используем переменную title
    wview.set_size(1280, 720, WEBVIEW_HINT_FIXED);
    wview.set_html(readIndex()); // Устанавливаем HTML содержимое
    wview.run(); // Запускаем веб-просмотр
}