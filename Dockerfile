FROM python:3.11-slim AS builder

WORKDIR /app

# Копируем requirements.txt
COPY src/requirements.txt ./

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Финальная стадия (минимизированный образ)
FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости из билд-стадии
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Копируем код приложения
COPY src/ ./src/
COPY ./alembic.ini ./

# Переменные окружения
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app:$PYTHONPATH

# Запуск приложения
CMD ["bash", "/app/src/start.sh"]
