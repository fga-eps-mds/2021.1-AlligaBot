
<p align="center">
  <img width="300" src="docs/assets/img/logo.png">
</p>
<h1 align="center">AlligaBot</h1>

 ![GitHub issues](https://img.shields.io/github/issues/fga-eps-mds/2021.1-AlligaBot?color=red)
 ![GitHub closed issues](https://img.shields.io/github/issues-closed/fga-eps-mds/2021.1-AlligaBot?color=green)
 ![GitHub pull requests](https://img.shields.io/github/issues-pr/fga-eps-mds/2021.1-AlligaBot?color=orange)
 ![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/fga-eps-mds/2021.1-AlligaBot?color=brightgreen)
 ![GitHub branches](https://badgen.net/github/branches/fga-eps-mds/2021.1-AlligaBot/)
 ![GitHub repo size](https://img.shields.io/github/repo-size/fga-eps-mds/2021.1-AlligaBot?color=purple)
 ![GitHub contributors](https://img.shields.io/github/contributors/fga-eps-mds/2021.1-AlligaBot?color=ff69b4)
 ![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)
<!-- ![GitHub commits count](https://badgen.net/github/commits/fga-eps-mds/2021.1-AlligaBot/)
<!-- [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/fga-eps-mds/2021.1-AlligaBot/blob/main/LICENSE) -->

## 💻 Visão Geral
O AlligaBot propõe-se a ajudar a combater desinformação
no contexto da pandemia do COVID-19, facilitando a  divulgação 
de informações importantes através de um chat bot que responderá as dúvidas
mais frequentes.
	

## 💡 Ideia e Incentivo
Com o decorrer da pandemia percebemos a preocupante e crescente desinformação da
população, e quando tal fato está relacionado a uma pandemia global é 
extremamente perigoso. Por isso achamos necessária a divulgação de informações 
pertinentes sobre a COVID-19 para informar a população e, de alguma forma, 
ajudar no combate mundial ao vírus.

<!-- ## ⚙️ Funcionalidades
- [x] Checkbox:
  - [x] Sub-Checkbox
    - Tópico 1
    - Tópico 2 -->

 ## 📦 Releases
  Release 1 - 14 de setembro
  - [Apresentação Geral](https://youtu.be/S_MtOdIb13s)
  - [Apresentação Equipe Capivaras](https://www.youtube.com/watch?v=TWQMUeZd9EY)
  - [Apresentação Equipe Plus Ultra](https://www.youtube.com/watch?v=5FDRdg9cj_k)
  - [Apresentação Equipe Slowbros](https://www.youtube.com/watch?v=mxh4G5HwLlE)
  
  Release 2 - 28 de outubto
  - [Apresentação Geral](https://www.youtube.com/watch?v=obGYts5OgUw)
  - [Apresentação Equipe Capivaras](https://www.youtube.com/watch?v=NFjVpS1ztDw)
  - [Apresentação Equipe Plus Ultra](https://www.youtube.com/watch?v=7I6uinQSSJY)
  - [Apresentação Equipe Slowbros](https://www.youtube.com/watch?v=j0dtt2ndL2k)

## 🚀 Como executar o projeto
### 🛠 Tecnologias e Pré-Requisitos
Esse projeto usa algumas ferramentas para o seu desenvolvimento:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [WSL](https://docs.microsoft.com/pt-br/windows/wsl/install-win10) para 
desenvolvimento em Windows 10
- [Make](https://www.gnu.org/software/make/)

Você pode assistir esse [vídeo](https://www.youtube.com/watch?v=oQ08ZaOAiGU)
para instalar as ferramentas do Docker e o WSL no Windows 10. Além disso, note
que Docker Compose é um programa diferente do Docker e deve ser instalado 
separadamente.

### ✔️ Instalando e executando
Baixe o repositório e entre nele

    git clone https://github.com/fga-eps-mds/2021.1-AlligaBot.git
    cd 2021.1-AlligaBot

Crie um arquivo para as variáveis ambiente e o preencha com as
informações que faltam.

    cp .example.env .env

Para preencher essas variáveis, dê uma olhada na seção da 
[FAQ "Onde conseguir os tokens e as variáveis de ambiente?"](docs/_posts/2021-09-16-faq.md).
Faça build das imagens rodando o seguinte comando:

    make build 

Se esta é a sua primeira vez executando esse comando, isso pode levar 
alguns minutos. Em seguida suba os contêineres com

    make run

Então, treine o bot executando:

    make train


Para conversar com o chatBot, execute o seguinte:

    make shell

Para sair do shell, digite `/stop` ou faça <kbd>Ctrl</kbd>+<kbd>C</kbd>.
Não se esqueça de desligar os containers quando terminar sua sessão de
desenvolvimento. Para desligar os contêineres basta executar:

    make stop

Se você quiser adicionar novos diálogos ao AlligaBot você deve fazer alterações 
no arquivos `bot/domain.yml` e `bot/data/*.yml`, e, em seguida, deve treiná-lo
novamente:

    make train


## 🤝 Como contribuir para o projeto

[Guia de Contribuição](docs/_posts/2021-08-16-como-contribuir.md)

[Código de Conduta](docs/_posts/2021-08-21-code_of_conduct.md)

[Política de Branches](docs/_posts/2021-08-19-branches.md)

[Políticas de Commits](docs/_posts/2021-08-18-commits.md)

[Template para criação de issues](.github/ISSUE_TEMPLATE/custom.md)

[Template para criação de pull requests](.github/pull_request_template.md)

## 👨‍💻 Desenvolvedores

### Capivaras 🐗

<table>
	<tr>
		<td align="center"><a href="https://github.com/AnaCarolinaRodriguesLeite"><img src="https://avatars.githubusercontent.com/u/49570180?v=4" width="100px;" alt=""/><br /><sub><b>Ana Carolina</b></sub></a><br /><a href="https://github.com/AnaCarolinaRodriguesLeite"></a></td>
		<td align="center"><a href="https://github.com/klmurussi"><img src="https://avatars.githubusercontent.com/u/52364259?v=4" width="100px;" alt=""/><br /><sub><b>Kathlyn Lara</b></sub></a><br /><a href="https://github.com/klmurussi"></a></td>
		<td align="center"><a href="https://github.com/LamequeFernandes"><img src="https://avatars.githubusercontent.com/u/79016306?v=4" width="100px;" alt=""/><br /><sub><b>Lameque Fernandes</b></sub></a><br /><a href="https://github.com/LamequeFernandes"></a></td>
		<td align="center"><a href="https://github.com/gatotabaco"><img src="https://user-images.githubusercontent.com/44625056/138941035-32cb39e4-06e2-44fc-9108-219fbe232373.png" width="100px;" alt=""/><br /><sub><b>Matheus Sousa</b></sub></a><br /><a href="https://github.com/gatotabaco"></a></td>
		<td align="center"><a href="https://github.com/Thais-ra"><img src="https://avatars.githubusercontent.com/u/35047444?v=4" width="100px;" alt=""/><br /><sub><b>Thais Rebouças</b></sub></a><br /><a href="https://github.com/Thais-ra"></a></td>
	</tr>
</table>

### Plus Ultra 🔋

<table>
	<tr>
		<td align="center"><a href="https://github.com/AmandaNbr"><img src="https://avatars.githubusercontent.com/u/44625056?v=4" width="100px;" alt=""/><br /><sub><b>Amanda Nobre</b></sub></a><br /><a href="https://github.com/AmandaNbr"></a></td>
		<td align="center"><a href="https://github.com/Ericklevy"><img src="https://avatars.githubusercontent.com/u/48847770?v=4" width="100px;" alt=""/><br /><sub><b>Erick Levy</b></sub></a><br /><a href="https://github.com/Ericklevy"></a></td>
		<td align="center"><a href="https://github.com/DouglasMonteles"><img src="https://avatars.githubusercontent.com/u/54580766?v=4" width="100px;" alt=""/><br /><sub><b>Douglas Monteles</b></sub></a><br /><a href="https://github.com/DouglasMonteles"></a></td>
		<td align="center"><a href="https://github.com/victorear05"><img src="https://avatars.githubusercontent.com/u/78758172?v=4" width="100px;" alt=""/><br /><sub><b>Victor Eduardo</b></sub></a><br /><a href="https://github.com/victorear05"></a></td>
		<td align="center"><a href="https://github.com/PedroLSF"><img src="https://avatars.githubusercontent.com/u/85000470?v=4" width="100px;" alt=""/><br /><sub><b>Pedro Lucas</b></sub></a><br /><a href="https://github.com/PedroLSF"></a></td>
    <td align="center"><a href="https://github.com/yudi-azvd"><img src="https://avatars.githubusercontent.com/u/37981839?v=4" width="100px;" alt=""/><br /><sub><b>Yudi Yamane</b></sub></a><br /><a href="https://github.com/yudi-azvd"></a></td>
	</tr>
</table>

### Slowbrows 🐌


<table>
	<tr>
		<td align="center"><a href="https://github.com/HenriqueHida"><img src="https://user-images.githubusercontent.com/44625056/138940949-85ce3584-3998-4b02-b078-71e490d2e8dd.png" width="100px;" alt=""/><br /><sub><b>Henrique Hida</b></sub></a><br /><a href="https://github.com/HenriqueHida"></a></td>
		<td align="center"><a href="https://github.com/kayrocesar"><img src="https://user-images.githubusercontent.com/44625056/138947080-2c18ad1b-8e2b-4c47-a317-92b46b68c00b.png" width="100px;" alt=""/><br /><sub><b>Kayro Cesar</b></sub></a><br /><a href="https://github.com/kayrocesar"></a></td>
	</tr>
</table>

## 📝 Licença
Este projeto está licenciado sob os termos da licença 
[GNU GPL v3.0](./LICENSE).

