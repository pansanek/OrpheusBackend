FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_message

# Установка зависимостей проекта
COPY ./requirements.txt /app_message/
RUN pip install --no-cache-dir --upgrade -r /app_message/requirements.txt

# Перенос проекта в образ
COPY ./app_message/app /app_message/app
COPY .env /app_message

# Копирование файлов alembic
COPY ./app_message/migration /app_message/migration
COPY ./app_message/alembic.ini /app_message/alembic.ini

EXPOSE 81

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 81"]