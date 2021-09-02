FROM rasa/rasa-sdk:latest

ADD ./actions /app/actions

CMD [ "start", "--actions", "actions" ]