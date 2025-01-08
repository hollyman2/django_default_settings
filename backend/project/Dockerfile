FROM python:3.9-slim-buster

RUN groupadd -r appuser && useradd -r -g appuser -m -s /bin/bash appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/staticfiles && chown -R appuser:appuser /app/staticfiles

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

USER appuser

ENV DJANGO_SETTINGS_MODULE=config.settings
ENV DATABASE_URL=postgres://postgres:Holly_2000@db:5432/todoapp

ENTRYPOINT ["/app/entrypoint.sh"]

