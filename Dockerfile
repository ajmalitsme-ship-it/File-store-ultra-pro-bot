FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["bash", "-c", "python bot.py & gunicorn wsgi:app --bind 0.0.0.0:$PORT"]
