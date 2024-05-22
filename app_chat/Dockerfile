FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_chat

# Установка зависимостей проекта
COPY ./requirements.txt /app_chat/
RUN pip install --no-cache-dir --upgrade -r /app_chat/requirements.txt

# Перенос проекта в образ
COPY ./app_chat/app /app_chat/app
COPY .env /app_chat


EXPOSE 81

CMD ["/bin/sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 81"]