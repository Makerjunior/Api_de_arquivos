from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Habilita o CORS para permitir acesso de qualquer origem (não recomendado para produção)

@app.route('/')
def listar_arquivos():
    pasta_arquivos = 'arquivos'  # Nome da pasta que você deseja listar
    caminhos = [os.path.abspath(os.path.join(pasta_arquivos, arquivo)) for arquivo in os.listdir(pasta_arquivos)]
    return jsonify(caminhos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
