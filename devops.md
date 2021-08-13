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

Baixe a imagem do rasa executando o seguinte comando no terminal:

    docker run --user 0 -v $(pwd):/app rasa/rasa:2.8.2-full init --no-prompt

Se você estiver em Linux, pode ser que você aprecisa rodar o comando anterior
com `sudo`. Algumas explicações sobre o comando anterior:

- `--user 0` dá permissões de root para o container.
- `-v $(pwd)/bot:/app` especifica que os conteúdos do subdiretório bot
vão estar visíveis para o container no diretório `app`. As mudanças 
que ocorrem no container vão ser sincronizadas com o seu computador.
- `rasa/rasa:2.8.2-full` é o nome da imagem que docker vai baixar e executar.
- `init --no-prompt` é o comando do próprio rasa. 

Se essa é a sua primeira vez rodando esse comando, o Docker vai baixar a imagem 
do Rasa, o que pode levar alguns minutos. Logo em seguida ele vai executar 
o container. 


### Conversando com o bot
Se você quiser mais ações para bot, vamos criar e ligar o servidor de ações:

    docker network create my-project

    docker run --user 0 -v $(pwd)/bot:/app --net my-project --name action-server rasa/rasa-sdk:2.8.1

    docker run --user 0 -d -v $(pwd)/bot/actions:/app/actions --net my-project --name action-server rasa/rasa-sdk:2.8.1

Para interagir com o bot (usando o servidor de ações), execute:

    docker run -it -v $(pwd)/bot:/app -p 5005:5005 --net my-project rasa/rasa:2.8.2-full shell

Se você preferiu não ligar o servidor de ações, apenas execute:

    docker run -it -v $(pwd)/bot:/app rasa/rasa:2.8.2-full shell


Note a flag `it`. Ela indica que o container vai ser executado no modo
**iterativo** e com uma sessão de terminal ligada a ele. 

Depois que o prompt aparecer, experimente dizer "hi" e dizer que está triste.
Tente pedir para ele contar uma piada também.


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


## Referências
- [Building a Rasa Assistant in Docker](https://rasa.com/docs/rasa/docker/building-in-docker/)
- [docker run](https://docs.docker.com/engine/reference/commandline/run/)
- [Deploying in docker compose](https://rasa.com/docs/rasa/docker/deploying-in-docker-compose/)