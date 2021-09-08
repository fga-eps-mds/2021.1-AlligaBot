FROM python:3.8-slim

ADD ./bot /app

RUN pip install --upgrade pip && \ 
    pip install --progress-bar off -r /app/requirements.txt

WORKDIR /app

RUN rasa train

USER 1001

ENTRYPOINT [ "rasa" ]

CMD [ "run", "--enable-api", "--port", "8080" ]
