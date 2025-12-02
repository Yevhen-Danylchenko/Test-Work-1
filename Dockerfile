FROM python:3.11-slim

WORKDIR /app

COPY run.py .
COPY main.py .
COPY StatsDB.py .
COPY DataLoader.py .
COPY StatUpdater.py .
COPY test_stats.py .
COPY fb_spend.json .
COPY network_conv.json .

RUN pip install --no-cache-dir apscheduler pytest

ENTRYPOINT ["python", "run.py"]