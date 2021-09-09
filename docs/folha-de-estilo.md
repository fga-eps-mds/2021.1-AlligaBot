## Histórico de versões
|  Data | Versão |          Descrição         |  Autor(es)  |
|:-----:|:------:|:--------------------------:|:-----------:|
| 09/09 |   0.1  | Primeiras regras de estilo | Yudi Yamane |


# Folha de Estilo
Este documento explica o estilo de código Python usado no projeto. O estilo é 
baseado no [PEP 8](https://www.python.org/dev/peps/pep-0008/) com poucas 
modificações que serão explicadas abaixo juntamente com outros exemplos.

Para os curiosos, a ferramenta escolhida para verificar o estilo e formatação é
o [autopep8](https://pypi.org/project/autopep8/). Foi escolhida por ser 
flexível, popular e ter a opção de realizar a formatação automaticamente.

Antes de fazer push das suas alterações execute o linter (consulte o 
[`makefile`](/Makefile) para saber o comando).


## Exemplos
### Tabs ou espaços?
Use 2 espaços para cada nível de indentação. Configure o tab para 2 espaços no
seu editor de texto.

**Faça** assim:
```py
def my_func():
  if (result == IS_OK)
    return True
  return False
```

**Não** faça assim:
```py
def my_func():
    if (result == IS_OK)
        return True
    return False
```

### Espaços em branco em expressões
Evite espaços em branco desnecessários.

**Faça** assim:
```py
func(ham[1], {eggs: 2})
```

**Não** faça assim:
```py
func( ham [ 1 ], { eggs : 2 } )
```

Coloque espaços entre os operadores de menor prioridade.

**Faça** assim:
```py
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

**Não** faça assim:
```py
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

## Referências

- As referencias devem está em formato [ABNT](https://github.com/LamequeFernandes).
- [Introdução ao pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html)
- [Como usar arquivo de configuração para autopep8](https://github.com/hhatto/autopep8/issues/378)



