FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_user

# Установка зависимостей проекта
COPY ./requirements.txt /app_user/
RUN pip install --no-cache-dir --upgrade -r /app_user/requirements.txt

# Перенос проекта в образ
COPY ./app_user/app /app_user/app
COPY .env /app_user

EXPOSE 88

CMD ["/bin/sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 88"]



