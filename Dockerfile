FROM python:3.6-alpine3.10

WORKDIR /app

COPY src .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "-u", "elasticsearch-take-snap.py" ]
