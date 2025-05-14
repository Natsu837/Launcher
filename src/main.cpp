#include <webview/webview.h>
#include <iostream>
#include <fstream>
#include <string>

std::string title = "Launcher";

int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrevInst, LPSTR lpCmdLine, int nCmdShow)
{
    system("resources/node/node.exe resources/server.js");
    webview::webview wview(false, nullptr);
    wview.set_title(title); // Используем переменную title
    wview.set_size(1280, 720, WEBVIEW_HINT_FIXED);
    wview.navigate("localhost:3000"); // Подключение к frontend
    wview.run(); // Запускаем веб-просмотр
}