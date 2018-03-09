from flask import  Flask

app = Flask(__name__) #Criando uma instância da classe Flask chamada app

@app.route("/") #Definindo a URL que executará a função abaixo

def hello_word(): #Função que retorna uma frase exibida no navegador.
    return "Hello, World"