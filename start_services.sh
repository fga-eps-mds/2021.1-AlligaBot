cd app/

# Treinando o modelo do Rasa
#rasa train

# Iniciando o servidor do Rasa
rasa run --model models --enable-api --cors "*" --debug --p $PORT