current_dir := $(shell pwd)

stop:
	sudo docker-compose stop

run-shell:
	sudo docker run -it -v $(current_dir)/bot:/app -p 5005:5005 --net my-project rasa/rasa:2.8.2-full shell

# train:
	# mkdir -p bot/models
	# sudo docker run -v $(current_dir):/bot rasa/rasa:2.8.3-full train --domain domain.yml --data data --out models
