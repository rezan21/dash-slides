FROM python:3.8-slim-buster

# ENV PYTHONUNBUFFERED True

RUN apt-get update 
RUN pip install --upgrade pip

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--worker-class", "gevent", "--workers", "2", "--worker-connections=500", "app:server", "-b", "0.0.0.0:8080"]

