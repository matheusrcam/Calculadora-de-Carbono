# routes.py

from flask import Blueprint, request, jsonify, render_template
from calculos import calcular_emissoes
from fatores_emissao import projetos_reducao

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/calcular', methods=['POST'])
def calcular():
    dados = request.json
    total_emissoes, custos_compensacao = calcular_emissoes(dados)
    # Enviando também a quantidade de créditos necessários
    return jsonify({
        'total_emissoes': total_emissoes,
        'creditos': total_emissoes / 1000,  # Convertendo para toneladas de CO2
        'custos_compensacao': custos_compensacao
    })

@routes.route('/custo', methods=['POST'])
def calcular_custo():
    data = request.json
    creditos = data.get('creditos')
    projeto = data.get('projeto')
    
    if projeto in projetos_reducao:
        custo = creditos * projetos_reducao[projeto]
        return jsonify({'custo': custo})
    else:
        return jsonify({'erro': 'Projeto de compensação não encontrado'}), 400
