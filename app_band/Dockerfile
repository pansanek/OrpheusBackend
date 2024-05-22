FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_band

# Установка зависимостей проекта
COPY ./requirements.txt /app_band/
RUN pip install --no-cache-dir --upgrade -r /app_band/requirements.txt

# Перенос проекта в образ
COPY ./app_band/app /app_band/app
COPY .env /app_band


EXPOSE 80

CMD ["/bin/sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 80"]