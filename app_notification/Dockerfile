FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_notification

# Установка зависимостей проекта
COPY ./requirements.txt /app_notification/
RUN pip install --no-cache-dir --upgrade -r /app_notification/requirements.txt

# Перенос проекта в образ
COPY ./app_notification/app /app_notification/app
COPY .env /app_notification

# Копирование файлов alembic
COPY ./app_notification/migration /app_notification/migration
COPY ./app_notification/alembic.ini /app_notification/alembic.ini

EXPOSE 88

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 88"]