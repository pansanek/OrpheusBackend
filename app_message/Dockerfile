FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_message

# Установка зависимостей проекта
COPY ./requirements.txt /app_message/
RUN pip install --no-cache-dir --upgrade -r /app_message/requirements.txt

# Перенос проекта в образ
COPY ./app_message/app /app_message/app
COPY .env /app_message

EXPOSE 84

CMD ["/bin/sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 84"]