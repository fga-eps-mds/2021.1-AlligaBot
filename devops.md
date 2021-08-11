# DevOps
Esse arquivo é temporário e serve como um mini diário
e manual de instruções do pessoal de DevOps. Futuramente
deve ser movido para o README.md principal. Nada do que
está comitado nessa branch é permanente.


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


### Rasa
Baixe a imagem do rasa executando o seguinte comando no terminal:

    docker run --user 1000 -v $(pwd):/app rasa/rasa:2.8.2-full init --no-prompt

Algumas explicações sobre o comando anterior:

- `--user 1000` dá permissões de root para o container.
- ``-v $(pwd):/app`` especifica que os conteúdos do diretório atual
vão estar visíveis para o container no diretório ``app``. As mudanças 
que ocorrem no container vão ser sincronizadas com o seu computador.
- ``rasa/rasa:2.8.2-full`` é o nome da imagem que docker vai baixar e executar.
- ``init --no-prompt`` é o comando do próprio rasa. 

Se essa é a sua primeira vez rodando esse comando, o Docker vai baixar a imagem 
do Rasa, o que pode levar alguns minutos. Logo em seguida ele vai executar 
o container. 


### Conversando com o bot
Para interagir com o bot, execute:

    docker run -it -v $(pwd):/app rasa/rasa:2.8.2-full shell

Note a flag ``it``. Ela indica que o container vai ser executado no modo
**iterativo** e com uma sessão de terminal ligada a ele. 

Depois que o prompt aparecer, experimente dizer "hi" e dizer que está triste.


## Algumas anotações e dúvidas
### 1 - Bot em um subdiretório
como foi feito no projeto [Aix](https://github.com/fga-eps-mds/2019.1-Aix). 
Tentei o seguinte comando:
    
    docker run --user 1000 -v $(pwd)/bot:/app rasa/rasa:2.8.2-full init --no-prompt

Mas não funciona. Dá problemas de permissão. 


### 2 - Por que essa parte da documentação usa ``docker run`` várias vezes?
``docker run`` cria um container a cada execução. Por que não usar 
simplesmente ``docker start`` para o iniciar o container já criado 
lá no começo do tutorial?


## Referências
- [Building a Rasa Assistant in Docker](https://rasa.com/docs/rasa/docker/building-in-docker/)
- [docker run](https://docs.docker.com/engine/reference/commandline/run/)
- [Deploying in docker compose](https://rasa.com/docs/rasa/docker/deploying-in-docker-compose/)