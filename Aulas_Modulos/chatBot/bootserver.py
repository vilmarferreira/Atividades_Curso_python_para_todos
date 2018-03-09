import requests
import traceback
import json
from flask import Flask, request

token = "xxxxxxxx"
app = Flask(__name__)

@app.route ('/', methods= ['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        try:
            data = json.loads(request.data.decode())
            text = data['entry'][0]['messaging'][0]['message']['text']
            sender = data['entry'][0]['messaging'][0]['sender']['id']

            if text == "Olá":
                payload = {'recipient': {'id': sender}, 'message': {'text': "Olá, tudo bem com você?"}}
            elif text == "Bom dia":
                payload = {'recipient': {'id': sender}, 'message': {'text': "Bom dia!!!"}}
            elif text == "Olá mundo":
                payload = {'recipient': {'id': sender}, 'message': {'text': "Hello, word!!!"}}
            else:
                payload = {'recipient': {'id': sender}, 'message': {'text': "Não tenho a resposta."}}

            r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
        except Exception as e:
            print(traceback.format_exc())
    elif request.method == 'GET':
        if request.args.get('hub.verify_token') == 'teste@123':
            return request.args.get('hub.challenge')
        return "Token Inválido"
    return "Nada a retornar"
if __name__ == '__main__':
    app.run(debug=True)

