FROM python:3.8-slim

RUN python -m pip install rasa

ADD ./bot /app

WORKDIR /app

RUN rasa train nlu

USER 1001

ENTRYPOINT [ "rasa" ]

CMD [ "run", "--enable-api", "--port", "8080" ]
