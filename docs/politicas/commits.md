# Política de Commits

Padronização dos commits no projeto. 

## Histórico de Versões


| Data       | Versão | Descrição                      | Autor             |
| :--------: | :----: | :----------:                   | :---------------: |
| 09/08/2021 |    1   | Criação da política de commits | Lameque Fernandes |

## Semântica do Commit

Os commits devem seguir o seguinte padrão:

### Princípios:

#### Commits atômicos
Sempre dividir em pequenos e significativos commits, fazendo com que cada commit tenha apenas uma funcionalidade.

#### Commits em Inglês
Para que o projeto seja mais acessível ao público global, o idioma padrão adotado tanto no código quanto para tudo o que se relaciona diretamente ao mesmo é o inglês.

### Formato:
```
<tipo>(#número da issue): assunto
```

#### Tipos:
- ```feat```: nova funcionalidade
- ```style```: formatação geral no código
- ```refact```: refatoração de código
- ```test```: adicionar/refatorar testes
- ```fix```: correções
- ```docs```: relacionado a documentação

#### Assunto:
- Deve possuir no máximo 50 caracteres
- Devem estar em letras minúsculas

*Exemplo de commit:*
```
git commit -m "refactor(#02): change login method to oauth"
```

## Referências

DARTORA, João. Tudo o que você precisa saber sobre commits semânticos. *Ilegra*. Disponível em: <https://ilegra.com/blog/tudo-o-que-voce-precisa-saber-sobre-commits-semanticos/>. Acesso em: 09 de ago. de 2021.

Políticas de Commit. Disponível em: <https://fga-eps-mds.github.io/2020.1-Grupo6/policies/commits/>. Acesso em: 09 de ago. de 2021