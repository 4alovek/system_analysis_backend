FROM python:3.12-slim

WORKDIR /app

ENV PYTHONPATH=/app/src

# Установка необходимых системных пакетов
RUN apt-get update && apt-get install -y

COPY ./pyproject.toml ./poetry.lock* ./

# Установка Poetry
RUN pip install --upgrade pip \
    && pip install setuptools poetry \
    && poetry config virtualenvs.create false \
    && poetry config virtualenvs.in-project false

# Установка зависимостей
RUN poetry install --no-root

# Копирование исходного кода
COPY ./src ./src

# Копирование и настройка entrypoint скрипта
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Запуск через entrypoint скрипт
ENTRYPOINT ["/entrypoint.sh"]