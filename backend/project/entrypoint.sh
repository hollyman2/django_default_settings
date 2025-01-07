#!/bin/bash

# Запуск миграций и сборка статических файлов
# mkdir -p static || (echo "Ошибка создания директории /app/static" && exit 1)
python3 manage.py makemigrations && \
python3 manage.py migrate && \
python3 manage.py collectstatic --noinput || (echo "Ошибка collectstatic" && exit 1)


# ... (другие команды, например, создание суперпользователя) ...

# Запуск сервера Django в фоне
gunicorn --bind 0.0.0.0:8000 config.wsgi:application &

celery -A config.celery beat -l info &

wait


