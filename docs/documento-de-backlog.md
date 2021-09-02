# Backlog do Produto

Esse documento contêm os itens que deverão ser desenvolvidos pelos times de desenvolvimento, levando em conta os requisitos levantados. 

# Histórico de revisão
  |Data|Versão|Alteração|Autor|  
  |----|------|---------|-----|  
  |19/08/2021|0.1|Primeira definição de funcionalidades|Pedro Lucas|
  |24/08/2021|0.2|Alterações gerais|Ana Carolina, Pedro Lucas e Thaís Rebouças|
  |24/08/2021|0.2|Criação de épicos e features|Pedro Lucas e Thaís Rebouças|
  |29/08/2021|0.3|Criação de histórias de usuário|Pedro Lucas e Thaís Rebouças|
  |01/09/2021|0.4|Adição da definição do MoSCoW e pequenas correções na estrutura do documento|Thaís Rebouças|
  |01/09/2021|0.4|Adição de priorização levando em conta o time Capivaras|Thaís Rebouças|

# Referências

- Railsware Product Academy. MoSCoW prioritization for your product backlog. Youtube, 19 de Setembro de 2019. Disponível em: https://www.youtube.com/watch?v=DzruAbBhY0Q. Acesso em: 01 de Setembro de 2021.


# 1. Introdução

## 1.2 Abreviações e seus significados
|Abreviação|Significado|
|----------|-----------|
|EP|Epics|
|FT|Features|
|US|User Stories|

## 1.3 Termos importantes que serão utilizados nesse documento
|Termo|Definição|
|----------|-----------|
|Epics|Epics são descrições gerais do que se deseja no software|
|Features|Features é semelhante a Epics, porém é mais detalhada em relação ao que é sua função|
|User Stories|User Stories são exemplos de usuários que irão utilizar a função de uma feature em questão|

## 1.4 Priorização com MoSCoW

O MoSCoW é uma técnica utilizada para definir a prioridade dos requisitos presentes no projeto. As classificações são dadas por Must, Should, Could e Won't, que juntas formam o acrônimo MoSCoW. Essas classificações são dadas, para que se possa hierarquizar a necessidade dos requisitos ao projeto. Entendendo as regras de priorização, fizemos essa classificação para dar início à abertura desse documento.

- Must: Deve ter este requisito para atender às necessidades de negócios.
- Should: Deve ter este requisito, se possível, mas o sucesso do projeto não depende dele.
- Could: Pode ter este requisito se não afetar mais nada no projeto.
- Won't: Gostaria de ter esse requisito mais tarde, mas a entrega não será desta vez.

# 2. Backlog

## EP01: Sobre o bot
Será uma epic para ser uma informação inicial, onde o usuário terá o primeiro contato com o bot e terá uma breve explicação sobre suas funcionalidades.

### FT01: Cumprimento/Despedida

|ID|User Story|Prioridade|
|----------|-----------|---------|
|US01|Eu, como usuário, desejo receber cumprimento do bot para dar início a conversa |Must|
|US02|Eu, como usuário, desejo saber o que o bot é |Must|
|US03|Eu, como administrador do bot, desejo adicionar o tópico para que o bot seja capaz de manter uma conversa |Must|
|US04|Eu, como administrador do bot, desejo adicionar o tópico para que o bot entre em Fallback quando necessário |Must|
|US05|Eu, como usuário, desejo receber mensagem de despedida do bot para finalizar a conversa |Must|

### FT02: Apresentação de funcionalidades

|ID|User Story|Prioridade|
|----------|-----------|---------|
|US06|Eu, como usuário, desejo saber sobre as funcionalidades existentes no bot |Must|

## EP02: Informação sobre covid
Será uma epic para informar o usuário e tirar dúvidas gerais sobre a covid.

### FT03: Transmissão e prevenção

|ID|User Story|Prioridade|
|----------|-----------|---------|
|US07|Eu, como usuário, desejo saber sobre as variantes do covid|Must|
|US08|Eu, como usuário, desejo saber sobre as formas de transmissão|Must|
|US09|Eu, como usuário, desejo saber mais sobre o vírus|Must|
|US10|Eu, como usuário, desejo saber sobre as formas gerais de prevenção|Must|
|US11|Eu, como usuário, desejo saber sobre os sintomas da covid|Must|
|US13|Eu, como usuário, desejo saber qual a quantidade de infectados por covid na minha cidade/país|Should|

### FT04: Regras para lugares específicos

|ID|User Story|Prioridade|
|----------|-----------|---------|
|US15|Eu, como usuário, desejo saber os cuidados que devo ter em locais abertos|Must|
|US16|Eu, como usuário, desejo saber os cuidados que devo ter em locais fechados|Must|
|US17|Eu, como usuário, desejo saber qual a diferença de contaminação entre locais abertos e fechados|Must|
|US18|Eu, como cliente, desejo saber os cuidados que devo ter em restaurantes|Should|
|US19|Eu, como cliente, desejo saber os cuidados que devo ter na academia|Should|
|US20|Eu, como cliente, desejo saber os cuidados que devo ter no dentista|Should|
|US21|Eu, como cliente, desejo saber os cuidados que devo ter em barbearia/cabelereiro|Should|

### FT05: Como continuar trabalhando de maneira segura

|ID|User Story|Prioridade|
|----------|-----------|---------|
|US22|Eu, como funcionário, desejo saber os cuidados que devo tomar no escritório|Must|
|US23|Eu, como funcionário, desejo saber os cuidados que devo ter no atendimento aos clientes|Must|

### FT06: Preciso pegar transporte público

|ID|User Story|Prioridade|
|----------|-----------|---------|
|US24|Eu, como usuário, desejo saber como me cuidar no transporte público |Must|

### FT07: Home office e saúde mental

|ID|User Story|Prioridade|
|----------|-----------|---------|
|US25|Eu, como usuário, desejo saber como lidar com o home office |Should|
|US26|Eu, como usuário, desejo saber como posso me exercitar em casa |Should|
|US27|Eu, como usuário, desejo saber como cuidar da minha saúde mental na pandemia |Must|

### FT08: Vacinação

|ID|User Story|Prioridade|
|----------|-----------|---------|
|US28|Eu, como usuário, desejo saber qual a quantidade de vacinados na minha cidade/país|Could|
|US279|Eu, como usuário, desejo saber quando posso me vacinar|Must|
|US30|Eu, como usuário, desejo saber se as vacinas são seguras|Must|
|US31|Eu, como usuário, desejo saber se eu preciso me vacinar|Must|
|US32|Eu, como usuário, desejo saber como as vacinas aprovadas pela anvisa agem no organismo|Should|
|US33|Eu, como usuário, desejo saber quantas doses da vacina preciso tomar|Must|
|US34|Eu, como usuário, desejo saber qual a eficácia de cada vacina aprovada pela anvisa|Must|

### FT09: Detecção

|ID|User Story|Prioridade|
|----------|-----------|---------|
|US35|Eu, como usuário com suspeita de covid, desejo saber oque fazer|Must|
|US36|Eu, como usuário com suspeita de covid, desejo saber aonde me testar|Should|
|US37|Eu, como usuário com suspeita de covid, desejo saber qual tipo de exame devo fazer e porque|Must|
|US38|Eu, como usuário, testei positivo para covid e quero saber oque fazer|Must|

## EP03: Lembrete programado
Será uma epic para criar lembretes programados.

### FT10: Lembrete de vacinação

|ID|User Story|Prioridade|
|----------|-----------|---------|
|US39|Eu, como usuário, desejo cadastrar a data da próxima dose da vacina|Must|
|US40|Eu, como usuário, desejo ser lembrado da próxima dose da vacina|Must|

### FT11: Avisos e cuidados

|ID|User Story|Prioridade|
|----------|-----------|---------|
|US41|Eu, como usuário, desejo cadastrar interesse em receber mensagens sobre as principais descobertas sobre a covid|Could|
|US42|Eu, como usuário, desejo ser notificado sobre as principais descobertas sobre a covid|Could|
|US43|Eu, como usuário, desejo cadastrar interesse em receber mensagens sobre dicas de home office|Could|
|US44|Eu, como usuário, desejo receber dicas de home office|Could|
|US45|Eu, como usuário, desejo cadastrar interesse em receber mensagens sobre dicas de saúde mental|Should|
|US46|Eu, como usuário, desejo receber dicas de saúde mental|Should|