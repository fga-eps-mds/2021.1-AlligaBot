## Realizando o deploy do Alligabot no Heroku

### Pré-requisitos
- Criar uma conta no [heroku](https://dashboard.heroku.com/)
- Baixar o [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)
- Ter o [docker](https://docs.docker.com/get-docker/) e o [docker-compose](https://docs.docker.com/compose/) devidamente instalados

### Clonando o projeto

    git clone -b feature#141/rasa-deploy https://github.com/fga-eps-mds/2021-1-Bot.git

Entre no diretório `2021-1-Bot`:

    cd 2021-1-Bot

### Arquivos necessários
É necessário criar alguns arquivos na raiz do projeto para executar o Alligabot dentro de um container Docker no heroku, neste repositório, eles já estão criados, são eles:
- Um arquivo `Dockerfile`
- Um arquivo `start_services.sh`
- Um arquivo `heroku.yml`

### Realizando o deploy
Para enviar o projeto dentro de um container para o heroku, siga estes passos:

    heroku login

    heroku create informe_o_nome_do_projeto

    heroku container:login

    heroku container:push web

    heroku container:release web

### Conversando com o Alligabot
Este projeto já conta com a integração com o `Telegram`, entretando, é necessário informar ao `Heroku` as variáveis de ambiente com as credenciais de acesso, para isso:
- Acesse o seu [projeto no heroku](https://dashboard.heroku.com/apps)
- Clique no nome que você escolheu
- Depois vá em Settings (Configurações)
- Clique em `Reveal Config Vars` 
- Para os próximos passos, você precisa criar um bot no telegram, veja este [tutorial](https://github.com/fga-eps-mds/2021-1-Bot/blob/feature%23141%2Frasa-deploy/docs/tutoriais/Tutorial_Integracao_Rasa_com_Telegram.md)
- Adicione `BOT_ACCESS_TOKEN` e em valor cole o token de acesso informado pelo `BotFather` no telegram.
- Adicione `BOT_USER_NAME` e em valor cole o nome de usuário do Bot.
- Adicione `BOT_URL` e o valor será o domínio do seu app no heroku: `https://nome_do_seu_projeto_no_heroku.herokuapp.com`
- Converse com o Alligabot pelo Telegram 

### Verificando logs
Para visualizar os logs da aplicação, digite no terminal:

    heroku logs --tail

### Erros comuns
Alguns erros podem acontecer durante o deploy no heroku, o mais comum é:
- `R10 - Boot timeout`: <p align="justify">Basicamente este erro ocorre devido ao fato do Rasa precisar treinar um modelo, o que acaba levando mais tempo de o esperado, e o heroku espera, por padrão, `60s` para o app se vincular a uma porta, quando o app leva mais tempo a aplicação quebra e o processo é finalizado com erro. Para resolver isso é necessário informar ao heroku que já é esperado que o nosso app levará mais que `60s` para iniciar, para isso acessamos [este recurso](https://tools.heroku.support/limits/boot_timeout) que permitirá com que nós selecionamos o app que queremos e depois informar o `boot_timeout`, para o Rasa, é necessário selecionar `150s`.</p>
- Veja a lista de erros possíveis [aqui](https://devcenter.heroku.com/articles/error-codes)