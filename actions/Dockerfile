FROM python:3.8-slim

RUN python -m pip install rasa==2.8.3

ADD requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && \ 
    pip install pandas \
    pip install patool \
    pip install --progress-bar off --no-cache-dir -r /tmp/requirements.txt

ADD . /app/actions

WORKDIR /app/actions

USER root

ENTRYPOINT [  ]

RUN chmod +x /app/actions/start_services.sh

CMD /app/actions/start_services.sh