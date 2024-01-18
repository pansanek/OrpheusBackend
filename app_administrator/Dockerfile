FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_administrator

# Установка зависимостей проекта
COPY ./requirements.txt /app_administrator/
RUN pip install --no-cache-dir --upgrade -r /app_administrator/requirements.txt

# Перенос проекта в образ
COPY ./app_administrator/app /app_administrator/app
COPY .env /app_administrator

# Копирование файлов alembic
COPY ./app_administrator/migration /app_administrator/migration
COPY ./app_administrator/alembic.ini /app_administrator/alembic.ini

EXPOSE 80

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 80"]