# Histórico de revisão
  |Data|Versão|Alteração|Autor|  
  |----|------|---------|-----|  
  |10/08/2021|0.1|Abertura do documento de Arquitetura|Victor Eduardo|  

# 1. Introdução
## 1.1 Finalidade
Este documento tem como finalidade apresentar a arquitetura do projeto ChatBot, para que o leitor consiga identificar sua estrutura arquitetural, e possa assim saber como o projeto foi desenvolvido, e como esse funciona.

## 1.2 Escopo
Essa documentação engloba as funções visadas pelo projeto, além das tecnologias usadas, seu diagrama de relações, e casos de uso. Engloba também algumas outras informações técnicas como características de desempenho e qualidade. O projeto vem sendo desenvolvido por alunos da UNB-FGA, na disciplina MDS. 

## 1.3 Definições, acrônimos e abreviações
|Abreviação|Significado|
|----------|-----------|
|FGA|Faculdade do Gama|
|MDS|Métodos de Desenvolvimento de Software|
|UNB|Universidade de Brasília|

## 1.4 Referências
- Chat Bot. Disponível em https://github.com/fga-eps-mds/2021-1-Bot. Acesso em 10/08/2021.
- Como documentar a Arquitetura de Software. Disponível em http://www.linhadecodigo.com.br/artigo/3343/como-documentar-a-arquitetura-de-software.aspx. Acesso em 10/08/2021.
- Documento de Arquitetua GloriaBot. Disponível em: https://github.com/fga-eps-mds/2019.2-GloriaBot/blob/master/docs/DocumentoDeArquitetura.md. Acesso em 10/08/2021.
- Documento de Arquitetura Tino. Disponível em: https://github.com/fga-eps-mds/2019.1-Tino/blob/master/docs/documento-de-arquitetura.md. Acesso em 10/08/2021.
- Documento de Arquitetura Vamos Cuidar. Disponível em: https://fga-eps-mds.github.io/2020.1-VC_Usuario/#/docs/Documento_de_Arquitetura. Acesso em 10/08/2021.

## 1.5 Visão Geral
Este documento está dividído em 7 grandes tópicos, com subdivisões, com o objetivo final de detalhar as características arquiteturais do projeto, bem como seus requisitos e motivações. Está dividido nos seguintes grandes tópicos:
| |Tópico|Descrição|
|-|------|---------|
|1|Introdução|Fornece ao leitor uma visão geral do conteúdo abordado no documento|
|2|Representação Arquitetural|Detalha a arquitetura utilizada no projeto e como ela está organizada|
|3|Metas e Restrições da Arquitetura|Descreve os objetivos do projeto, bem como suas restrições, do ponto de vista arquitetural|
|4|Visão dos Casos de Uso|Descreve as partes significativas do ponto de vista da arquitetura do modelo de casos de uso|
|5|Visão Lógica|Descreve as partes significativas do ponto de vista da arquitetura do modelo de design|
|6|Tamanho e Desempenho|Descreve as características de desempenho do Software, bem como as restrições estabelecidas e possíveis falhas|
|7|Qualidade|Descreve como a arquitetura contribui para que o Software final possua um maior nível de qualidade|

# 2. Representação da Arquitetura
![Captura de tela de 2021-08-21 13-52-58](https://user-images.githubusercontent.com/78758172/130329524-98ee4023-ffc3-4753-8e57-2e16f721a651.png)


A representação arquitetural do ciclo de funcionamento está explicitada na imagem acima. O ciclo começa quando o usuário envia uma mensagem para o bot, após isso a API recebe a mensagem e repassa para o processamento de linguagem natural (PLN), que por usa vez repassa para o bot que processa a informação com a intenção de identificar o que está sendo requerido pelo usuário. Após o processamento, o bot busca no site [Corona cidades](https://coronacidades.org/) a melhor resposta e a repassa para a API, que dá o retorno ao usuário.
Por se tratar de um ChatBot, o projeto conta apenas com a parte de Back-end, uma vez que a parte Front-end seria exatamente o app Telegram que é responsável por receber a mensagem do usuário e passá-la ao bot através da API, e de dar o devido retorno através da mesma.

## 2.1 Tecnologias

# 3. Metas e restrições de Arquitetura 
## 3.1 Metas
O projeto aqui apresentado, trata-se de um Chat Bot integrado a plataforma Telegram, um app de troca de mensagens, e tem a função de informar o usuário acerca de conteúdos sobre o COVID-19 com informações fornecidas pelo site [Corona Cidades](coronacidades.org), sobre como prevenir o contágio, sobre gestão pública, e informações relacionadas à vacinação na região do usuário.

## 3.2 Restrições

## 3.3 Requisitos não funcionais
- O sistema deve possui integração com a plataforma Telegram.
- O sistema deve conversar com o usuário em linguagem natural.
- O sistema deve ser capaz de receber a localização do usuário, caso necessário.
- O sistema deve ser capaz de interpretar áudios enviados pelo usuário.

# 4. Visão dos Casos de Uso
  
## 4.1 Diagrama de Casos de Uso
![](https://user-images.githubusercontent.com/78758172/128819731-a98ac913-94b5-4764-b76e-11a85ae1f8ad.png)
## 4.2 Atores de Casos de Uso
|Ator|Descrição|
|----|---------|
|Usuário|O usuário poderá interagir com o bot através do chat da plataforma Telegram, utilizando linguagem natural|

## 4.3 Descrições de Casos de Uso
|Épico|Caso de uso|Descrição|
|-----|-----------|---------|
|E1|Solicitação de informações a respeito da Gestão Pública|Buscar e dar o retorno sobre Gestão Pública|
|E2|Solicitação de informações a respeito da vacinação na região|Obter a localização do usuário, buscar e dar o retorno sobre a vacinação em tal região|
|E3|Solicitação de informações a respeito da prevenção|Buscar e dar o retorno sobre prevenção no(s) lugar(es), solicitado(s) pelo usuário|
# 5. Visão Lógica
## 5.1 Diagrama de Pacotes

# 6. Tamanho e desempenho

# 7. Qualidade
  
