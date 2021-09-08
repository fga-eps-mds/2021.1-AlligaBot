FROM python:3.8-slim

RUN python -m pip install rasa

ADD ./bot /app

WORKDIR /app

USER 1001

ENTRYPOINT [ "rasa" ]

RUN chmod +x /app/start_services.sh

CMD /app/start_services.sh
