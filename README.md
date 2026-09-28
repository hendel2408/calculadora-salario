# Calculadora de Salario Liquido com Flask

Aplicacao web desenvolvida em Flask para calcular o salario liquido a partir do salario bruto e do numero de dependentes.

## Regras do calculo

- INSS: 8% do salario bruto.
- IR: 15% do salario bruto quando o valor for superior a R$ 2.500,00.
- Dependentes: acrescimo de R$ 200,00 por dependente.
- Entradas invalidas e valores negativos sao tratados pelo formulario.

## Como executar

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Depois, acesse `http://127.0.0.1:5000` no navegador.

O relatorio da atividade, com os resultados dos testes e as respostas propostas, esta em [relatorio.md](relatorio.md).
