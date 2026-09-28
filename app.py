from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    try:
        salario = float(request.form["salario"])
        dependentes = int(request.form["dependentes"])
    except ValueError:
        return "Erro: Insira valores válidos."

    if salario < 0:
        return "Erro: O salário não pode ser negativo."

    if dependentes < 0:
        return "Erro: O número de dependentes não pode ser negativo."

    inss = salario * 0.08

    if salario > 2500:
        ir = salario * 0.15
    else:
        ir = 0

    resultado = salario - inss - ir + (dependentes * 200)

    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Resultado</title>
        <style>
            body {{
                min-height: 100vh;
                margin: 0;
                display: grid;
                place-items: center;
                font-family: Arial, sans-serif;
                color: #222222;
                background-color: #f5f5f5;
            }}

            p {{
                margin: 20px;
                font-size: 28px;
                font-weight: bold;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <p>Salário líquido: R$ {resultado:.2f}</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
