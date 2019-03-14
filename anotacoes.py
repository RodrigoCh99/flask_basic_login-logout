"""
        ----------------------------------    //    ---------------------------------------------
ANOTAÇÃO:

    O código asseguir faz uma das funções "/teste" ou a outra dependendo da condicional:
     usuario interagiu com a URL ?

@app.route("/test")
@app.route("/test/<name>")
def test(name=None):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá! Pessoa que não informou nome"

        ----------------------------------    //    ---------------------------------------------

# Um modo equivalente ao informado é:

        ----------------------------------    //    ---------------------------------------------
@app.route("/test", defaults={'name': None})
@app.route("/test/<name>")
def test(name):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá! Pessoa que não informou nome"


      ----------------------------------    //    ---------------------------------------------

"""