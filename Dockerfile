FROM python:3.11-alpine
WORKDIR /easyquest
COPY app app
COPY gunicorn.conf.py gunicorn.conf.py
COPY easyquest.supervisor.ini easyquest.supervisor.ini
COPY requirements.txt requirements.txt
COPY supervisord.conf supervisord.conf
COPY requirements.txt requirements.txt

RUN mkdir /easyquest/uploads/

RUN apk add --update --no-cache gcc musl-dev linux-headers git supervisor
RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt

ENTRYPOINT ["supervisord", "-c", "/easyquest/supervisord.conf"]