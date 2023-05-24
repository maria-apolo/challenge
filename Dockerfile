FROM python:latest

RUN apt-get update && apt-get install -y python3-dev build-essential

RUN mkdir -p /usr/src/challenge
WORKDIR /usr/src/challenge

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY challenge/ .

EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "challenge.api:app"]