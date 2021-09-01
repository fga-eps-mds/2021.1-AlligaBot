
<p align="center">
  <img width="200" src="docs/img/logo.png">
</p>
<h1 align="center">AlligaBot</h1>

<!-- [badges] [badges] [badges] [badges]  -->


## 💻 Visão Geral
O AlligaBot propõe-se a ajudar a combater desinformação
no contexto da pandemia do COVID-19, facilitando a  divulgação 
de informações importantes através de um bot que responderá as duvidas
mais frequentes.
	

## 💡 Ideia e Incentivo
Com o decorrer da pandemia percebemos a preocupante e crescente desinformação da
população, e quando tal fato está relacionado a uma pandemia global é 
extremamtente perigoso. Por isso achamos necessária a divulgação de informações 
pertinenetes sobre a COVID-19 para informar a população e, de alguma forma, 
ajudar no combate mundial ao vírus.

<!-- ## ⚙️ Funcionalidades
- [x] Checkbox:
  - [x] Sub-Checkbox
    - Tópico 1
    - Tópico 2 -->

<!-- ## 📦 Releases 1 e 2
  Release 1 - 2 de setembro
  
  Release 2 - 26 de outubto -->

## 🚀 Como executar o projeto
### 🛠 Tecnologias e Pré-Requisitos
Esse projeto usa algumas ferramentas para o seu desenvolvimento:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [WSL](https://docs.microsoft.com/pt-br/windows/wsl/install-win10) para 
desenvolvimento em Windows 10

### ✔️ Instalando e executando
Baixe o repositório e entre nele

    git clone https://github.com/fga-eps-mds/2021-1-Bot.git
    cd 2021-1-Bot

Suba o ambiente de desenvolvimento rodando o seguinte comando:

    docker-compose up -d

`-d` indica que os containers devem rodar em background. Se esta é a su primeira
vez executando esse comando, isso pode levar alguns minutos. Para conversar com 
o bot, execute o seguinte:

    docker exec -it bot rasa shell

Note a flag `it`. Ela indica que o container vai ser executado no modo
**iterativo** e com uma sessão de terminal ligada a ele. 

Depois que o prompt aparecer, peça a ele, em inglês, para te contar uma piada.
O [servidor de ações](actions/actions.py) foi desenvolvido para 
consultar uma API de piadas.

Se você quiser adicionar novas falas ao bot você deve fazer alterações no arquivos 
`bot/domain.yml` e `bot/data/*`, e, em seguida, deve treiná-lo:

    docker exec -it -u root bot rasa train

`-u root` dá permissões de root para o container reescrever o modelo. Se o seu 
terminal reclamar de permissão negada para editar os arquivos dentro de 
`bot/`, execute:

    sudo chown -R $USER bot/

Não se esqueça de desligar os containers quando terminar sua sessão de
desenolvimento. Para desligar os containeres basta executar:

    docker-compose down

<!-- ## 🤝 Como contribuir para o projeto

Guia de Contribuição

Código de Conduta

Como rodar o projeto

Políticas de Contribuição

Template para criação de issues

Template para criação de pull requests -->

## 👨‍💻 Desenvolvedores
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Capivara :ox:</th>
    <th class="tg-0pky">PlusUltra :fleur_de_lis:</th>
    <th class="tg-0pky">Slowbrows :pig2:</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Desenvolvedor</td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/36899389?v=4&s=45" width="45"> 
      <br><a href="https://github.com/MegahNevel"> Eduardo Levenhagem</a></td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/54580766?v=4&amp;s=45" alt="[Douglas Monteles]"> 
      <br><a href="https://github.com/DouglasMonteles">Douglas Monteles</a></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Desenvolvedor</td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/79016306?v=4&s=45" alt="Lameque"> 
      <br><a href="https://github.com/LamequeFernandes">Lameque Fernandes </a></td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/48847770?v=4&amp;s=45" alt="Erick Levy>"> 
      <br><a href="https://github.com/Ericklevy">Erick Levy</a></td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/39713656?v=4&s=45" alt="Kayro César>"> 
      <br><a href="https://github.com/kayrocesar">Kayro César</a></td>
  </tr>
  <tr>
    <td class="tg-0pky">DevOps</td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/35047444?v=4&s=45" alt="Thaos Rebouças"> 
      <br><a href="https://github.com/Thais-ra">Thais Rebouças</a></td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/37981839?s=45&amp;v=4" alt="Yudi Yamane"> 
      <br><a href="https://github.com/yudi-azvd">Yudi Yamane</a></td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/44177946?v=4&s=45" alt="Luiz Petengill"> 
      <br><a href="https://github.com/LuizPettengill">Luiz Petengill</a></td>
  </tr>
  <tr>
    <td class="tg-0pky">Arquiteto</td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/52364259?v=4&s=45" alt="Kathlyn Lara"> 
      <br><a href="https://github.com/klmurussi"> Kathlyn Lara</a></td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/78758172?v=4&amp;s=45" alt="Victor Eduardo"> 
      <br><a href="https://github.com/victorear05">Victor Eduardo</a></td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/53947083?v=4&s=45" alt="Matheus Rapahel"> 
      <br><a href="https://github.com/matheusrazor">Matheus Rapahel</a></td>
  </tr>
  <tr>
    <td class="tg-0pky">Product Owner</td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/49570180?v=4&s=45" alt="Ana Carolina">
      <br><a href="https://github.com/AnaCarolinaRodriguesLeite"> Ana Carolina </a></td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/85000470?v=4&amp;s=45" alt="Pedro Lucas"> 
      <br><a href="https://github.com/PedroLSF">Pedro Lucas</a></td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/73257118?v=4&s=45" alt="Matheus Akio"> 
      <br><a href="https://github.com/matheusakio">Matheus Akio</a></td>
  </tr>
  <tr>
    <td class="tg-0pky">Scrum Master</td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/54778783?v=4&s=45" alt="Matheus Sousa"> 
      <br><a href="https://github.com/gatotabaco">Matheus Sousa</a></td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/44625056?v=4&amp;s=45" alt="Amanda Nobre"> 
      <br><a href="https://github.com/AmandaNbr">Amanda Nobre</a></td>
    <td class="tg-0pky" style="text-align: center;"> 
      <img src="https://avatars.githubusercontent.com/u/78568172?v=4&s=45" alt="Henrique Hida"> 
      <br><a href="https://github.com/HenriqueHida">Henrique Hida</a></td>
  </tr>
</tbody>
</table>

<small>Feito com <a href="https://www.tablesgenerator.com/html_tables">
  Tables Generator</a>.
</small>

## 📝 Licença
Este projeto está licenciado sob os termos da licença 
[GNU GPL v3.0](https://github.com/fga-eps-mds/2021-1-Bot/blob/improvement(%2398)/melhorar-readme/LICENSE).
