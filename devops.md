# DevOps
Esse arquivo é temporário e serve como um mini diário
e manual de instruções do pessoal de DevOps. Futuramente
pode ser movido para o README.md principal. **Nada do que
está comitado nessa branch é permanente**.


## Começando
Certifique-se de que você tem 
[Docker](https://docs.docker.com/get-docker/) instalado em seu
computador. Se você usa Windows 10, será necessário habilitar
o [WSL](https://docs.microsoft.com/pt-br/windows/wsl/install-win10).
[Vídeo](https://www.youtube.com/watch?v=oQ08ZaOAiGU&ab_channel=CaravanaCloud)
para ter uma ideia visual de como é o processo de instalação dessas ferramentas.

Se você tiver seguidos todos os passos corretamente, você pode abrir
o temrinal e digitar:

    docker -v

Baixe esse repositório em seu computador (de preferência em ambiente Linux ou WSL):

    git clone https://github.com/fga-eps-mds/2021-1-Bot.git
    git checkout -b init-devops
    git pull origin init-devops

Ou clone apenas a branch `init-devops`:
    
    git clone -b init-devops https://github.com/fga-eps-mds/2021-1-Bot.git
    

### Rasa
Entre no repositório baixado

    cd 2021-1-Bot.git

Suba o ambiente de desenvolvimento rodando o seguinte comando:

    docker-compose up -d

`-d` indica que os containers devem rodar em background. Você deve ver algo assim no terminal:

    Starting actions ... done
    Starting rasa-bot ... done

Para conversar com o bot, execute o seguinte:

    docker exec -it rasa shell

Note a flag `it`. Ela indica que o container vai ser executado no modo
**iterativo** e com uma sessão de terminal ligada a ele. 

Depois que o prompt aparecer, em inglês, peça para ele te contar uma piada.

O  foi [servidor de ações](actions/actions.py) foi desenvolvido para 
consultar uma API de piadas.


## Algumas anotações e dúvidas
### 1 - Bot em um subdiretório
Como terão outros módulos além do bot, acho que faz sentido colocálo em um subdiretório.
Isso foi feito no projeto [Aix](https://github.com/fga-eps-mds/2019.1-Aix). Tentei fazer
isso com o seguinte comando:
    
    docker run --user 1000 -v $(pwd)/bot:/app rasa/rasa:2.8.2-full init --no-prompt

Note o conteúdo que vem depois da flag `-v`: `$(pwd)/bot:/bot`. `$(pwd)/bot`
indica o diretório `bot` dentro do diretório `$(pwd)`. Mas não funciona. Dá 
problemas de permissão. 

**Atualização**: rodar o comando anterior com ``--user 0`` dá certo.



### 2 - Por que essa parte da documentação usa `docker run` várias vezes?
`docker run` cria um container a cada execução. Por que não usar 
simplesmente `docker start` para o iniciar o container já criado 
lá no começo do tutorial?  Se rodar `docker start -i` ele usa o comando 
`shell` automaticamente. Como usar os comandos `init`, `shell` ou `train`
do Rasa?


### Permissão negada para editar um arquivo do bot
Dá uma olhada [aqui](https://github.com/microsoft/vscode-remote-release/issues/1008).

        sudo chown -R <seu-nome-de-usuario> <caminho/pra/pasta>


## VSCode não reconhece os módulos do rasa em venv
Você precisa dizer o path pro interpretador python do ambiente
virtual

Siga essas [instruções](https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code).

Mas não sei se isso é realmente necessário porque era pra estar pegando do container Docker.


## Quando o rasa reclamar de não ter permissão
[Olhe aqui](https://rasa.com/docs/rasa-x/installation-and-setup/install/docker-compose/#mounted-directories). Pra falar a verdade, eu não sei como isso funciona só rodei

        sudo chgrp -R root ./bot/* && sudo chmod -R 770 ./bot/*

e foi.
## Referências
- [Building a Rasa Assistant in Docker](https://rasa.com/docs/rasa/docker/building-in-docker/)
- [docker run](https://docs.docker.com/engine/reference/commandline/run/)
- [Deploying in docker compose](https://rasa.com/docs/rasa/docker/deploying-in-docker-compose/)


### Olhar depois
- https://github.com/airyhq/rasa-demo
- https://github.com/rgstephens/jokebot/blob/master/Dockerfile
- Esse me salvou: https://rasa.com/blog/custom-rasa-nlu-docker-container/
- https://rasa.com/blog/the-complete-guide-to-deploying-your-rasa-assistant/
