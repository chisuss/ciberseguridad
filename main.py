from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return "<h1>Hola Mundo</h1>"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/clave/<miclave>")
def clave(miclave):
    if miclave == "12345":
        return "Clave correcta"
    return "Clave incorrecta"

app.run(host="0.0.0.0", port=5000)
