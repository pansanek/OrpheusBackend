FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_attachment

# Установка зависимостей проекта
COPY ./requirements.txt /app_attachment/
RUN pip install --no-cache-dir --upgrade -r /app_attachment/requirements.txt

# Перенос проекта в образ
COPY ./app_attachment/app /app_attachment/app
COPY ../.env /app_attachment

# Копирование файлов alembic
COPY ./app_attachment/migration /app_attachment/migration
COPY ./app_attachment/alembic.ini /app_attachment/alembic.ini

EXPOSE 82

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 82"]