from flask import Flask, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Habilita o CORS para permitir acesso de qualquer origem (não recomendado para produção)

@app.route('/')
def listar_arquivos():
    pasta_arquivos = 'arquivos'  # Nome da pasta que você deseja listar
    arquivos = [arquivo for arquivo in os.listdir(pasta_arquivos)]
    caminho = arquivos

    return jsonify(arquivos)

@app.route('/arquivos/<nome_arquivo>')
def obter_arquivo(nome_arquivo):
    pasta_arquivos = 'arquivos'  # Nome da pasta que contém os arquivos
    caminho_arquivo = os.path.join(pasta_arquivos, nome_arquivo)

    return send_file(caminho_arquivo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
