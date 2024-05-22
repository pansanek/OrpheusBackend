FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_location

# Установка зависимостей проекта
COPY ./requirements.txt /app_location/
RUN pip install --no-cache-dir --upgrade -r /app_location/requirements.txt

# Перенос проекта в образ
COPY ./app_location/app /app_location/app
COPY .env /app_location

EXPOSE 83

CMD ["/bin/sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 83"]