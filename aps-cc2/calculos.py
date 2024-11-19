# calculos.py

from fatores_emissao import fatores_emissao, projetos_reducao

def calcular_emissoes(dados):
    total_emissoes = 0
    
    # Calcula o total de emissões com base nos dados recebidos
    for tipo, quantidade in dados.items():
        if tipo in fatores_emissao:
            emissao = quantidade * fatores_emissao[tipo]
            total_emissoes += emissao

    # Converte kg CO2 para toneladas
    total_emissoes_toneladas = total_emissoes / 1000

    # Calcula o custo para compensar as emissões em cada projeto de redução
    custos_compensacao = {
        projeto: total_emissoes_toneladas * preco
        for projeto, preco in projetos_reducao.items()
    }

    # Retorna as emissões totais e os custos de compensação
    return total_emissoes, custos_compensacao
