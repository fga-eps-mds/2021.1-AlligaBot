# Como testar as entradas do bot e respostas

Este e um tutorial que visa a ferramente do proprio rasa para testar as entradas do usuarios com as resposta do bot.

### Preparando

Certifique-se que voce esta na pasta de `bot/tests/` e ir no arquivo `test_stories.yml` .

Neste `test_stories.yml` crie sua historia e coloque a intenção do usuario `user` insira a frase do usuario e insira as intenções(`intent`) do usuario e as ações(`action`) do bot.

    stories:
    - story: inicio conversa
      steps:
      - user: |
          oi
        intent: start
      - action: utter_cumprimentar

### Posteriormente faça o teste

Usando o comando o rasa testara as entradas e saidas e vera se estão de acordo com uma matriz em diagonal.

    make test


Com isso o make test gerara a pasta `bot/results` nesta pasta gerara 3 pngs importantes para ver se todos os testes bateram.


Se estiver tudo certo com a imagens ela gerara umas matriz em diagonal sem outros numeros fora da diagonal.

Se não aparecera algum quadrado fora da diagonal

<h1 align="center">Matrix de confusão certa</h1>
<p align="center">
    <img width="500" src="../img/intent_confusion_matrix.png">
</p>



<h1 align="center">Matrix de confusão errada</h1>
<p align="center">
    <img width="500" src="../img/intent_confusion_matrix_example.png">
</p>

<h1 align="center">Histograma do bot certo</h1>
<p align="center">
    <img width="500" src="../img/intent_histogram.png">
</p>

<h1 align="center">Histograma do bot errado</h1>
<p align="center">
    <img width="500" src="../img/intent_histogram_example.png">
</p>


<h1 align="center">Histórias do bot</h1>
<p align="center">
    <img width="700" src="../img/story_confusion_matrix.png">
</p>






