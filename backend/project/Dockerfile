FROM python:3.9-slim-buster

# Установка необходимых системных пакетов
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    # Удаляем Supervisord, установленный через apt (на всякий случай)
    && apt-get purge --auto-remove supervisor \
    && apt-get install -y --no-install-recommends python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Создание пользователя с ограниченными правами
RUN groupadd -r appuser && useradd -r -g appuser -m -s /bin/bash appuser

# Рабочая директория
WORKDIR /app

# Создание директории для логов и установка прав
RUN mkdir -p /app/logs && chown -R appuser:appuser /app/logs

# Создание виртуального окружения
RUN python3 -m venv .venv

# Копирование зависимостей
COPY requirements.txt .

# Установка зависимостей в виртуальное окружение
RUN . .venv/bin/activate && pip install --no-cache-dir -r requirements.txt \
    && pip install supervisor # Устанавливаем supervisor через pip3

# Копирование приложения
COPY . .

# Настройка прав доступа
RUN chown -R appuser:appuser . \
    && chmod -R 755 /app/.venv \
    && chmod -R 755 /app/.venv/bin/gunicorn \
    && chmod -R 755 /app/.venv/bin/celery

# Копирование конфигурационного файла supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Установка прав на конфигурационный файл supervisord
RUN chown appuser:appuser /etc/supervisor/conf.d/supervisord.conf

# Переключение на пользователя appuser
USER appuser

# Настройка переменных окружения (замените на свои значения)
ENV DJANGO_SETTINGS_MODULE=config.settings
ENV DATABASE_URL=postgres://user:password@host:port/database_name
ENV REDIS_URL=redis://redis:6379/0
ENV RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672//

# Создание директорий для статических и медиа файлов
RUN mkdir -p staticfiles media

# Запуск supervisord с явным указанием Python 3 (на всякий случай)
ENTRYPOINT ["/app/.venv/bin/supervisord", "-n"] 

# Или, если supervisor установлен глобально для Python 3:
# ENTRYPOINT ["/usr/bin/supervisord", "-n"]
