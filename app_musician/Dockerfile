FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_musician

# Установка зависимостей проекта
COPY ./requirements.txt /app_musician/
RUN pip install --no-cache-dir --upgrade -r /app_musician/requirements.txt

# Перенос проекта в образ
COPY ./app_musician/app /app_musician/app
COPY ../.env /app_musician

# Копирование файлов alembic
COPY ./app_musician/migration /app_musician/migration
COPY ./app_musician/alembic.ini /app_musician/alembic.ini

EXPOSE 86

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 86"]