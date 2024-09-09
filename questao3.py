import json

def ler_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        dados = json.load(file)
    return dados['faturamento']

def calcular_menor_maior_faturamento(faturamento):
    valores = [dado['valor'] for dado in faturamento if dado['valor'] > 0]
    menor = min(valores)
    maior = max(valores)
    return menor, maior

def calcular_media_mensal(faturamento):
    valores = [dado['valor'] for dado in faturamento if dado['valor'] > 0]
    if len(valores) > 0:
        media = sum(valores) / len(valores)
    else:
        media = 0
    return media

def contar_dias_acima_media(faturamento, media):
    return sum(1 for dado in faturamento if dado['valor'] > media)

def main():
    caminho_arquivo = 'faturamento.json'

    faturamento = ler_dados_json(caminho_arquivo)
    
    menor, maior = calcular_menor_maior_faturamento(faturamento)
    
    media_mensal = calcular_media_mensal(faturamento)
    
    dias_acima_media = contar_dias_acima_media(faturamento, media_mensal)
    
    print(f"Menor valor de faturamento: R$ {menor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

if __name__ == "__main__":
    main()