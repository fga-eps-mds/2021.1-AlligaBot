cd app/

# Treina o bot 
rasa train

# Incia o servidor do Rasa
rasa run --model models --enable-api --cors “*” --debug -p $PORT