FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /code

# Установка зависимостей проекта
COPY ./requirements.txt /app_user/
RUN pip install --no-cache-dir --upgrade -r /app_user/requirements.txt

# Перенос проекта в образ
COPY ./app_user/app /app_user/app
COPY ../.env /app_user

# Копирование файлов alembic
COPY ./app_user/migration /app_user/migration
COPY ./app_user/alembic.ini /app_user/alembic.ini

EXPOSE 88

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 88"]