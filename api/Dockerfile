FROM python:3.10-slim

WORKDIR /app

ENV FLASK_APP app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /app

CMD ["flask", "run"]
