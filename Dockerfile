# Використовуємо офіційний Python образ
FROM python:3.11-slim

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо файли проекту
COPY run.py .
COPY main.py .
COPY StatsDB.py .
COPY DataLoader.py .
COPY StatUpdater.py .
COPY fb_spend.json .
COPY network_conv.json .

# Встановлюємо потрібні залежності напряму
RUN pip install --no-cache-dir apscheduler pytest

# За замовчуванням запускаємо скрипт
ENTRYPOINT ["python", "run.py"]