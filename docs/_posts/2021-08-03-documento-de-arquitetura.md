---
layout: post
date: 2021-08-03 00:00:00 -0300
categories: docs
excerpt: ""
---

<!-- ## Histórico de revisão
|Data|Versão|Alteração|Autor|  
|----|------|---------|-----|  
|10/08/2021|0.1|Abertura do documento de Arquitetura|Victor Eduardo|  
|21/08/2021|0.2|Definição de tecnologias, e diagrama arquitetural|Victor Eduardo, Matheus Raphael|
|08/09/2021|0.3|Correção de pequenos erros presentes no documento|Victor Eduardo| -->
  
# 1. Introdução
## 1.1 Finalidade
Este documento tem como finalidade apresentar a arquitetura do projeto ChatBot, de forma que fique de fácil entedimento a estrututra arquitetural do projeto, e sejam mostradas todas as decisões relacionadas a ela.
  
## 1.2 Escopo
Essa documentação engloba as funções visadas pelo projeto, além das tecnologias usadas, seu diagrama de relações e casos de uso. Engloba também algumas outras informações técnicas como características de desempenho e qualidade. O projeto vem sendo desenvolvido por alunos da UNB-FGA, na disciplina MDS.
  
## 1.3 Definições, acrônimos e abreviações

| Abreviação | Significado |
|:---:|:---:|
| API | Application Programming Interface |
| FGA | Faculdade do Gama |
| MDS | Métodos de Desenvolvimento de Software |
| NLU | Natural-language understanding |
| UNB | Universidade de Brasília |

## 1.4 Referências
- Chat Bot. Disponível em https://github.com/fga-eps-mds/2021-1-Bot. Acesso em 10/08/2021.
- Como documentar a Arquitetura de Software. Disponível em http://www.linhadecodigo.com.br/artigo/3343/como-documentar-a-arquitetura-de-software.aspx. Acesso em 10/08/2021.
- Documento de Arquitetua GloriaBot. Disponível em: https://github.com/fga-eps-mds/2019.2-GloriaBot/blob/master/docs/DocumentoDeArquitetura.md. Acesso em 10/08/2021.
- Documento de Arquitetura Tino. Disponível em: https://github.com/fga-eps-mds/2019.1-Tino/blob/master/docs/documento-de-arquitetura.md. Acesso em 10/08/2021.
- Documento de Arquitetura Vamos Cuidar. Disponível em: https://fga-eps-mds.github.io/2020.1-VC_Usuario/#/docs/Documento_de_Arquitetura. Acesso em 10/08/2021.
  
## 1.5 Visão Geral
Este documento está dividído em 6 grandes tópicos, com subdivisões, com o objetivo final de detalhar as características arquiteturais do projeto, bem como seus requisitos e motivações:

|  | Tópico | Descrição |
|---|---|---|
| 1 | Introdução | Fornece ao leitor uma visão geral do conteúdo abordado no documento |
| 2 | Representação Arquitetural | Detalha a arquitetura utilizada no projeto e como ela está organizada |
| 3 | Metas e Restrições da Arquitetura | Descreve os objetivos do projeto, bem como suas restrições, do ponto de vista arquitetural |
| 4 | Visão dos Casos de Uso | Descreve as partes significativas do ponto de vista da arquitetura do modelo de casos de uso |
| 5 | Visão Lógica | Descreve as partes significativas do ponto de vista da arquitetura do modelo de design |
| 6 | Tamanho e Desempenho | Descreve as características de desempenho do Software, bem como as restrições estabelecidas e possíveis falhas |

# 2. Representação da Arquitetura
![Captura de tela de 2021-08-21 16-03-24](https://user-images.githubusercontent.com/78758172/130332389-f7fb3872-bf5c-4b54-adc6-ebb5a9a08312.png)

A representação arquitetural do ciclo de funcionamento está explicitada na imagem acima. O ciclo começa quando o usuário envia uma mensagem para o AlligaBot, após isso a mensagem é repassada ao bot onde primeiro a mensagem passa pelo Rasa NLU que processa a mensagem, após isso, no Rasa Core, é feita a etapa de identificar a intenção do usuário. Por último o Rasa escolherá a resposta mais adequada através do Rasa Actions, e retornará tal resposta ao usuário via Telegram.
Por se tratar de um ChatBot, o projeto conta apenas com a parte de Back-end, realizada através do Rasa, uma vez que o Front-end seria exatamente a interface do app Telegram que é responsável pela interação com o usuário, ou seja receber a mensagem do usuário e passá-la ao bot, e de mostrar ao usuário o retorno dado pelo bot.
  
## 2.1 Tecnologias
### 2.1.1 Rasa
![Captura de tela de 2021-08-21 16-00-44](https://user-images.githubusercontent.com/78758172/130332385-f1e97e13-94c1-4916-990e-3d1daf4d87ee.png)

Para a construção do sistema usaremos o Rasa, um framework utilizado para construção de bot's de conversação. O framework conta com 3 principais componentes, o Rasa NLU que é responsável por processar a mensagem enviada pelo usuário, o Rasa Core que é responsável por identificar a intenção do usuário e o Rasa Actions, que dada a intenção do usuário, este escolhe a resposta mais adequada a se retornar ao usuário.
O Rasa aprende de acordo com que for sendo treinado, através de seu machine learning, e através do NLU consegue-se fazer também um bot "mais humano".
  
### 2.1.2 Telegram
![telegram](https://user-images.githubusercontent.com/78758172/130331794-8b17a2c5-3cf8-42ba-a22f-9257b47d5bd3.png)

O local o qual o usuário poderá interagir com o bot será no Telegram sendo ele um app de troca de mensagens. A implementação de bot's à plataforma é gratuita e disponibilizada pelo próprio app.
  
### 2.1.3 Python
![python](https://user-images.githubusercontent.com/78758172/130331804-81e4fc0b-1138-40c5-8b85-1755a9c3eab3.png)

A linguagem de programação a ser utilizada no bot será o Python, já que o Rasa também a utiliza.
  
# 3. Metas e restrições de Arquitetura
## 3.1 Metas
O projeto aqui apresentado trata-se de um Chat Bot integrado a plataforma Telegram e tem como função informar o usuário acerca de conteúdos sobre o COVID-19 com informações fornecidas, dentro outros, pelo site [Corona Cidades](coronacidades.org), sobre como prevenir o contágio, gestão pública, e informações relacionadas à vacinação na região do usuário.
  
## 3.2 Restrições
- Possuir conexão com a internet
- Dispositivo com acesso ao Telegram
- O sistema entenderá apenas mensagens em Português - BR

  
## 3.3 Requisitos não funcionais
- O sistema deve possuir integração com a plataforma Telegram
- O sistema deve conversar com o usuário em linguagem natural
- O sistema deve ser capaz de receber a localização do usuário, quando necessário
- O bot deve ser treinado a fim de conseguir atender ao máximo de usuários possíveis
  
# 4. Visão dos Casos de Uso
## 4.1 Atores de Casos de Uso

|Ator|Descrição|
|----|---------|
|Usuário | O usuário poderá interagir com o bot através do chat da plataforma Telegram, utilizando linguagem natural|
  
## 4.2 Descrições de Casos de Uso

|Épico|Caso de uso|Descrição|
|-----|-----------|---------|
|E1|Sobre o bot|Será uma epic para ser uma informação inicial, onde o usuário terá o primeiro contato com o bot e terá uma breve explicação sobre suas funcionalidades|
|E2|Informações sobre covid|Será uma epic para informar o usuário e tirar dúvidas gerais sobre a covid|
|E3|Lembrete programado|Será uma epic para criar lembretes programados|
  
# 5. Visão Lógica
## 5.1 Diagrama de Pacotes
- O pacote 2021-1-Bot é o pacote principal do do projeto, contém todos os outros sub-pacotes e documentos disponíveis no documento
- Toda a documentação do projeto pode ser encontrada na pasta docs

# 6. Tamanho e desempenho
Este bot atuará primeiramente no Telegram, seu tamanho e desempenho serão comuns com aplicações semelhantes de ChatBots que utilizam a tecnologia Rasa.
O desempenho poderá ser afetado devido a serviços externos, como consultas de dados sobre vacinações ou instabilidades de sistemas.
