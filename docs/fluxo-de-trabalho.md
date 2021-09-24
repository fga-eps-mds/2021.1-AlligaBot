# Fluxo de Trabalho
Documento que descreve as etapas necessárias para uma implementação correta e eficiente das funcionalidades do Chatbot.

## Histórico de versões

| Data | Versão | Descrição | Autor |
| :--------: | :----: |:---------------: | :---------------: |
| 24/09/2021 | 0.1 | Criação do documento de fluxo de trabalho | [Douglas Monteles](https://github.com/DouglasMonteles)|

## Início
### Fluxo para implementar funcionalidades simples no Chatbot
É considerada uma funcionalidade simples aquela que possui uma resposta pronta, onde sabe-se que não haverá alteração ou atualização desta resposta com o passar do tempo.

<strong>Passo a passo:</strong>
  
`Desconsidere os comentários antecedidos por #`

  - Acesse o diretório `/bot` dentro do projeto
  - Precisamos criar uma `intent` dentro de `data/nlu.yml`
  - Adicione uma `intent` neste formato, abaixo das demais:
        
        # nlu.yml
        - intent: nome_da_intent
          examples: |
            - possível mensagem do usuário que represente esta intent
            - outra possível mensagem do usuário que represente esta intent

  - Depois, vá para `bot/domain.yml`, você precisa adicionar a intent recém criada na lista de `intents`

        # domain.yml
        intents:
          - start
          - despedida
          - covid
          - fora_do_escopo
          - formas_de_transmissao
          - mais_sobre_o_virus
          - bot_alligabot 
          - nome_da_intent
    
  - Ainda em `domain.yml`, precisamos adicionar as respostas que o usuário vai receber. Para isso, na parte de `responses:` adicione as respostas no seguinte padrão de nomeclatura: 

        # domain.yml
        responses:
          utter_nome_da_resposta:
          - text: Exemplo de resposta para a intent
          - text: "Exemplo de outra resposta que também manda uma imagem"
            image: "https://sitequalquer.com/imagem.png"

  - Em seguida, em `data/stories.yml`, precisamos adicionar o fluxo da conversa, ou seja, dada uma `intent`, precisamos adiconar uma `action`, <strong>que nesse caso</strong>, vai direcionar para as respostas criadas anteriormente.

        # stories.yml
        stories:

        - story: nome de sua escolha para identificar o storie
          steps:
          - intent: nome_da_intent
          - action: utter_nome_da_resposta

  - Por fim, treine o novo modelo e execute o shell para conversar com o bot:

        # Caso você esteja usando o docker
        make train
        make shell

        # Caso você esteja usando o Rasa instalado localmente
        rasa train
        rasa shell