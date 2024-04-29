from controller import controller
from flask import Flask, request,jsonify
from flask_cors import CORS
import traducao
import json

servidor = Flask(__name__)

CORS(servidor)

@servidor.route('/traduzir', methods=['POST'])

def traduzir_mensagem():
    
    dados = request.json
    frase =str(dados.get('frase'))
    idioma =str(dados.get('idioma'))    
    
    traducao_resultado = traducao.traduzir_frase(frase, idioma.lower())
    
    return jsonify({"traducao": traducao_resultado})
  

if __name__ == '__main__':
    servidor.run(debug=True)
    