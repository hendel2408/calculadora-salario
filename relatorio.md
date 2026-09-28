# Calculadora de Salario Liquido com Flask

## Resultados testados

| Salario bruto | Dependentes | Resultado observado |
| --- | ---: | --- |
| 3000,00 | 2 | R$ 2710,00 |
| 2000,00 | 1 | R$ 2040,00 |
| 1000,00 | 0 | R$ 920,00 |
| -500,00 | 1 | Erro: insira valores validos e nao negativos. |
| abc | 2 | Erro: insira valores validos e nao negativos. |
| 2500 | -1 | Erro: insira valores validos e nao negativos. |

## Respostas

1. A validacao dos dados no backend e importante porque o usuario pode alterar ou burlar validacoes feitas apenas no navegador. Validando no servidor, a aplicacao evita calculos incorretos, entradas maliciosas e erros causados por valores negativos ou nao numericos.

2. Para facilitar futuras atualizacoes da regra de calculo, o ideal e deixar as regras em uma funcao separada e usar constantes para aliquotas, limite do IR e valor por dependente. Assim, se uma regra mudar, basta alterar esses valores ou a funcao de calculo, sem mexer na estrutura das rotas e dos templates.
