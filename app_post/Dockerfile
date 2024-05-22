FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_post

# Установка зависимостей проекта
COPY ./requirements.txt /app_post/
RUN pip install --no-cache-dir --upgrade -r /app_post/requirements.txt

# Перенос проекта в образ
COPY ./app_post/app /app_post/app
COPY .env /app_post

EXPOSE 87

CMD ["/bin/sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 87"]