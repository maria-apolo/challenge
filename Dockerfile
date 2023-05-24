FROM python:3.9-slim@sha256:980b778550c0d938574f1b556362b27601ea5c620130a572feb63ac1df03eda5 

RUN mkdir -p /usr/src/challenge
WORKDIR /usr/src/challenge

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENV PORT 1243

CMD exec uvicorn challenge.api:app --host 0.0.0.0 --port ${PORT} --workers 1