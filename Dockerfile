FROM python:3.6-alpine3.10

WORKDIR /app

COPY elasticsearch-snap.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "-u", "snap.py" ]
