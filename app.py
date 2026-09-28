from flask import Flask, render_template, request

app = Flask(__name__)

ALIQUOTA_INSS = 0.08
LIMITE_IR = 2500.00
ALIQUOTA_IR = 0.15
VALOR_POR_DEPENDENTE = 200.00


def converter_salario(valor):
    return float(valor.strip().replace(",", "."))


@app.template_filter("moeda")
def formatar_moeda(valor):
    texto = f"{valor:,.2f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


def calcular_salario_liquido(salario_bruto, dependentes):
    if salario_bruto < 0:
        raise ValueError("O salario nao pode ser negativo.")

    if dependentes < 0:
        raise ValueError("O numero de dependentes nao pode ser negativo.")

    inss = salario_bruto * ALIQUOTA_INSS
    ir = salario_bruto * ALIQUOTA_IR if salario_bruto > LIMITE_IR else 0
    desconto_dependentes = dependentes * VALOR_POR_DEPENDENTE
    salario_liquido = salario_bruto - inss - ir + desconto_dependentes

    return {
        "salario_bruto": salario_bruto,
        "dependentes": dependentes,
        "inss": inss,
        "ir": ir,
        "desconto_dependentes": desconto_dependentes,
        "salario_liquido": salario_liquido,
    }


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    try:
        salario = converter_salario(request.form["salario"])
        dependentes = int(request.form["dependentes"])
        resultado_calculo = calcular_salario_liquido(salario, dependentes)
    except (ValueError, KeyError):
        return render_template(
            "form.html",
            erro="Erro: insira valores validos e nao negativos.",
        )

    return render_template("resultado.html", resultado=resultado_calculo)


if __name__ == "__main__":
    app.run(debug=True)
