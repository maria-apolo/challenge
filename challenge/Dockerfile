FROM python:latest

RUN apt-get update && apt-get install -y python3-dev build-essential

RUN mkdir -p /usr/src/challenge
WORKDIR /usr/src/challenge

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENV PORT 1243

CMD exec uvicorn challenge.api:app --host 0.0.0.0 --port ${PORT} --workers 1