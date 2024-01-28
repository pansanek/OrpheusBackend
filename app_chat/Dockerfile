FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_chat

# Установка зависимостей проекта
COPY ./requirements.txt /app_chat/
RUN pip install --no-cache-dir --upgrade -r /app_chat/requirements.txt

# Перенос проекта в образ
COPY ./app_chat/app /app_chat/app
COPY .env /app_chat

# Копирование файлов alembic
COPY ./app_chat/migration /app_chat/migration
COPY ./app_chat/alembic.ini /app_chat/alembic.ini

EXPOSE 82

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 82"]