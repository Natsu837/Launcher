// app.js
document.addEventListener("DOMContentLoaded", () => {
  // Кэшируем элементы DOM для повышения производительности
  const form = document.getElementById("myForm");
  const outputDiv = document.getElementById("output");
  const msgInput = document.getElementById("msgInput"); // Кэшируем также поле ввода

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    // Получаем и обрезаем значение ввода
    const inputValue = msgInput.value.trim();

    // Проверяем, не пустое ли значение
    if (!inputValue) {
      outputDiv.innerText = "Пожалуйста, введите сообщение."; // Отображаем сообщение об ошибке
      return;
    }

    try {
      // Выполняем запрос к серверу
      const response = await fetch(`http://127.0.0.1:65432`, {
        method: "POST",
        headers: {
          "Content-Type": "text/plain",
        },
        body: inputValue,
      });

      // Проверяем, успешен ли ответ
      if (!response.ok) {
        throw new Error(`Ошибка: ${response.statusText}`);
      }

      // Получаем текст ответа и отображаем его
      const textResponse = await response.text();
      outputDiv.innerText = textResponse;
    } catch (err) {
      // Отображаем ошибку в outputDiv вместо alert
      outputDiv.innerText = `Произошла ошибка: ${err.message}`;
    }
  });
});