# monta o container
build:
	@echo "Buildando Containers Docker."
	sudo docker-compose build

# roda o container em segundo plano
run:
	sudo docker-compose up -d
	@echo "Containers Docker estão rodando em segundo plano."

# monta e roda o container em segundo plano
run-build:
	@echo "Buildando Containers Docker."
	sudo docker-compose build
	sudo docker-compose up -d
	@echo "Containers Docker estão rodando em segundo plano."

# para o container
stop:
	sudo docker-compose down
	@echo "Containers Docker foram parados."

# abre o shell para comunicação com o bot
shell:
	@echo "Iniciando shell iterativo."
	sudo docker exec -it bot rasa shell

# treina o bot
train:
	@echo "Iniciando treino."
	sudo docker exec -it bot rasa train


lint-format-actions:
	@echo "Aplicando correções de estilo e formatação dos arquivos do servidor de ações"
	@docker exec -it actions python -m autopep8 /app/actions


docs-build:
	docker run -v $$PWD/docs:/srv/jekyll --name docs -p 4000:4000 -it jekyll/jekyll:3.8 jekyll serve --livereload

docs-start:
	docker start -i docs

docs-stop:
	docker stop docs