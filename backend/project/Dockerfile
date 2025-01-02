FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN groupadd -r appuser && useradd -r -g appuser -m -s /bin/bash appuser

USER appuser

ENV DJANGO_SETTINGS_MODULE=config.settings
ENV DATABASE_URL=sqlite:///db.sqlite3

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
