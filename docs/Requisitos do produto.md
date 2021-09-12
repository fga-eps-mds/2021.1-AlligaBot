# Requisitos do produto

Este documento esta com a elicitação dos requisitos gerados no início do projeto. 

## Histórico de versões

| Data | Versão | Descrição | Autor(es) |
| :--: | :----: | :-------: | :-------: |
| 02/09/2021  | 0.1 |  Criação da estrutura do documento  | Ana Carolina  |
| 02/09/2021  | 0.2 |  Criação da primeira versão |  Ana Carolina  |
| 11/09/2021  | 0.3 |  Correção de bugs da extensão e alteração de localidade para a pasta docs; Alteração do nome bot para chatbot e correção ortográfica  |  Ana Carolina  |

## Categoria de prioridades

| Tipo           | Descrição                             |
| :------------- | :------------------------------------- |
| Alta           | Requisitos indispensáveis para o funcionamento do chatbot  |
| Intermediária  | Requisitos importantes para o sistema, mas caso não sejam implementados não resultará em um mau funcionamento do chatbot     |
| Útil           | Requisitos que não são usados com tanta frequência e não são tão significativos na satisfação que o usuário tem sobre o chatbot                     |


## Lista de requisitos

| Identificador                 | Requisito                                                            | Dependente de | Prioridade |
| :---------------------------- | :------------------------------------------------------------------- | :------------ |  :-------- |
| RF01                          | Permitir que o usuário diga olá, para começar a conversa. | --- | Alta  |
| RF02                          | Mostrar a lista funcionalidades dos três temas logo depois da primeira interação.  | RF01  |  Alta  |
| RF03                          | Permitir ao usuário solucionar dúvidas gerais sobre a COVID-19.                     | RF02  | Alta  |
| RF04                          | Permitir que o usuário saiba informações sobre as vacinas que estão disponíveis.  | RF01,RF02 | Alta  |
| RF05                          | Permitir que o usuário saiba sobre a prevenção no sentido geral.(comum) | RF01  | Alta  |
| RF06                          | Permitir que o usuário saiba sobre prevenção em locais fechados e abertos.  | RF01,RF05 | Alta  |
| RF07                          | Permitir que o usuário visualize o número de infectados.  | RF01,RF02 | Baixa |
| RF08                          | Permitir que o usuário receba notificação sobre a data da próxima vacina. | RF04  | Alta  |
| RF00                          | Habilitar comunicação entre as normas de políticas públicas em conjunto com vacinação e prevenção.  | --- | Alta  |
| RF10                          | Permite ao usuário saber mais sobre o CoronaVírus.  | RF03  | Alta  |
| RF11                          | Suportar o grande número de informações atualizadas sobre a COVID-19 no banco de dados.  | --- | Intermediária  |
| RF12                          | Assegurar a qualidade e transparência da informação com o usuário.  | --- | Alta  |
| RF13                          | Permitir ao usuário saber dos sintomas quando infectado.  | RF03  | Alta  |
| RF14                          | Permitir que ele saiba os lugares de testes.  | RF14  | Alta  |
| RF15                          | Permitir que o usuário dê tchau ao chatbot sabendo que a conversa acabou. | RF01  | Útil  |
