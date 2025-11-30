Цей проєкт запускається всередині контейнера Docker на базі "python:3.11-slim".  
Мета — швидко підняти середовище для запуску скрипта "run.py".

---

Як підняти за 3 хвилини
 1. Побудувати образ
bash
docker build -t stats-app .


 1. Запустити контейнер

docker run --rm stats-app

Контейнер автоматично виконає python run.py завдяки ENTRYPOINT

 Структура проєкту
- run.py — головний скрипт для запуску
- main.py — основна логіка
- StatsDB.py — модуль роботи з базою статистики
- DataLoader.py — завантаження даних
- StatUpdater.py — оновлення статистики
- fb_spend.json — дані витрат Facebook
- network_conv.json — дані конверсій мережі

Залежності
Встановлюються напряму при побудові образу:
- apscheduler
- pytest


Тестування
Запустити інтерактивний контейнер і виконати тести:

docker run -it --rm stats-app pytest





