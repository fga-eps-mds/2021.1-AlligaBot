FROM rasa/rasa-sdk:latest

USER root

ADD actions/requirements.txt /tmp/

RUN pip install --upgrade pip && \ 
    pip install --progress-bar off --no-cache-dir -r /tmp/requirements.txt

ADD ./actions /app/actions

CMD [ "start", "--actions", "actions" ]