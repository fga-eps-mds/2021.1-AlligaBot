# Política de Branches

Padronização das branches no projeto. 

## Histórico de Versões


| Data       | Versão | Descrição                      | Autor             |
| :--------: | :----: | :----------:                   | :---------------: |
| 10/08/2021 |    1   | Criação da política de branch | [Lameque Fernandes](https://github.com/LamequeFernandes)|

## Padronização das Branches

### Prefixos:
- ```feature/```
- ```hotfix/```
- ```documentation/```
- ```improvement/```

### Branches:

- **Branch master:** Branch que contém o código em nível de produção, será o código mais consolidado existente na aplicação. Nenhum integrante dos times é autorizado a fazer commits diretamente na *master.*

- **Branches feature:** Como o nome já diz, são branches na qual são desenvolvidos novos recursos ao projeto. São criadas começando com o prefixo **feature/**.
Exemplo: ```feature/new-layout```

- **Branchs hotfix:** Branches no qual são realizadas correções de bugs São criadas começando com o prefixo **hotfix/**.
Exemplo: ```hotfix/button-correction```

- **Branches documentation:** Branches na qual são desenvolvidos os documentos do projeto. São ciradas começando com o prefixo **documentation/**
Exemplo: ```documentation/template-document```

- **Branches improvement:** Branche para melhoria de algum componente e afins, seja de performance, de escrita de layout, etc. Exemplo: ```improvement/layout-optimization```

### Princípios:
- Branches em Inglês: Para que o projeto seja mais acessível ao público global, o idioma padrão adotado tanto no código quanto para tudo o que se relaciona diretamente ao mesmo é o inglês.

## Referências

DULCETTI, Bruno. Padrões e nomenclaturas no Git. *BrunoDulcetti*. Disponível em: <https://www.brunodulcetti.com/padroes-e-nomenclaturas-no-git/>. Acesso em: 10 de ago. de 2021.

Políticas de Branches. Disponível em: <https://fga-eps-mds.github.io/2018.2-ComexStat/docs/politicaBranches>. Acesso em: 10 de ago. de 2021