FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_comment

# Установка зависимостей проекта
COPY ./requirements.txt /app_comment/
RUN pip install --no-cache-dir --upgrade -r /app_comment/requirements.txt

# Перенос проекта в образ
COPY ./app_comment/app /app_comment/app
COPY .env /app_comment


EXPOSE 82

CMD ["/bin/sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 82"]