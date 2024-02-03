from flask import Flask

app = Flask(__name__)


# criando rotas
@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/about")
def about():
    return "Página sobre"


if __name__ == "__main__":
    app.run(debug=True) # <- só para desinvolvimento manual 
