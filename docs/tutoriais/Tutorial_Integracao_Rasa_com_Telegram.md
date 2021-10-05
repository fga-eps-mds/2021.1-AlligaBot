<h1 align="center">Treinamento com Rasa</h1>

### Esse projeto pretende mostrar uma visão geral do Rasa e sua aplicação prática para criar um ChatBot no Telegram.
<br/>

### Video Explicativo
Para ajudar no tutorial, eu criei este [vídeo](https://www.youtube.com/watch?v=8TPbLPuCgCI&ab_channel=douglassilva) onde sigo este passa-a-passo abaixo para integrar o Telegram com Rasa

## Sobre o Projeto
Nesse projeto vamos criar uma assistente virtual com Rasa e integra-lo ao Telegram para que o usuário tenha um ambiente mais amigável para interagir.

## Pré-requisitos
  - Instalar o Rasa localmente
    - Veja como [Instalar o Rasa no Windows](https://www.youtube.com/watch?v=GlR60CvTh8A&ab_channel=Rasa)
    - Veja como [Instalar o Rasa no Linux](https://www.youtube.com/watch?v=tXiYJM2vGJk&ab_channel=Rasa)
  - Instalar o [NgRok](https://dashboard.ngrok.com/get-started/setup)
    - Para acessar a página de instalação, você precisa fazer um cadastro na página. Dica: Use o login com o Google.
    - Vaja este [vídeo](https://www.youtube.com/watch?v=nv7Q39NehDA&ab_channel=douglassilva) que eu criei sobre a instalação do NgRok

## Clonando o Projeto
Para clonar o projeto Rasa, execute o comando abaixo:

    git clone https://github.com/fga-eps-mds/2021-1-Bot.git
    git checkout -b rasa-training
    git pull origin rasa-training

Você pode optar por baixar somente a branch `rasa-training`:
    
    git clone -b rasa-training https://github.com/fga-eps-mds/2021-1-Bot.git

Agora, entre no diretório abaixo:

    cd 2021-1-Bot/rasa-assistente

## Criando o Bot no Telegram
Precesamos de um bot no Telegram para podermos integra-lo ao nosso projeto, para isso, acesse o Telegram e siga os passos abaixo:
  - Pesquise por: `BotFather`
  - Crie um novo bot com: `/newbot`
  - Dê um nome para o bot
  - Dê um nome de usuário (precisa terminar com bot Ex: botinho_bot)
  - Observe que ele gera um token para acessar a API, ele será necessário para o próximo passo

## Liberanado o localhost para o mundo
Para que o Telegram consiga se comunicar com o nosso projeto Rasa, ele precisa acessar o serviço que estara rodando localmente no endereco: `http://localhost:5005`, no entanto, este serviço é acessível somente de forma local. Para liberar o serviço para acesso externo, vamos utilizar o `NgRok`. O comando abaixo libera o serviço que está randando localmente na porta 5005 para o mundo.

    ./ngrok http 5005

Copie a URL gerada com protocolo HTTPS e siga para o próximo passo.

## Alterando as Credenciais
Antes de executar o projeto, precisamos alterar as credenciais do Rasa para podermos conecta-lo ao bot do Telegram
  - No projeto, acesse o arquivo na raiz do projeto: `credentials.yml`

No Arquivo, altere a parte sobre o Telegram:

    telegram:
      access_token: "COLE_AQUI_SEU_TOKEN_DO_TELEGRAM"
      verify: "COLE_AQUI_SEU_NOME_DE_USUARIO"
      webhook_url: "COLE-SOMENTE_AQUI_SUA_URL_GERADA_PELO_NGHOK/webhooks/telegram/webhook"


## Execultando o Projeto
O comando abaixo executa o projeto Rasa, habilitando o recurso de API e liberando o CORS.

    rasa train
    rasa run --enable-api --cors "*"


## Conversando pelo Telegram
Se tudo ocorrer bem, você poderá conversar com seu bot pelo Telegram, exerimente começar com `/start`.

<img src="assets/conversa_pelo_telegram.jpeg">
