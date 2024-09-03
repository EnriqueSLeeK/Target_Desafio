
import json
from statistics import mean

# Foi usado o json
# So foi considerado os dias uteis onde o 'valor' nao e 0

def extracao_de_dados(arquivo: str) -> dict:
    with open('dados.json', 'r') as f:
        return json.loads(f.read())

def procura_menor_faturamento(faturamentos: list) -> float:
    return min(faturamentos)

def procura_maior_faturamento(faturamentos: list) -> float:
    return max(faturamentos)

def conta_dias_faturamento_media(faturamentos, media):
    contador = 0
    for faturamento in faturamentos:
        if faturamento > media:
            contador += 1
    return contador

def main():
    dados = extracao_de_dados('dados.json')

    faturamentos = [dado['valor'] for dado in dados if dado['valor'] != 0]
    menor_faturamento = procura_menor_faturamento(faturamentos)
    maior_faturamento = procura_maior_faturamento(faturamentos)
    media = mean(faturamentos)

    dias_acima_media_faturamento = conta_dias_faturamento_media(faturamentos, media)

    return (menor_faturamento, maior_faturamento, dias_acima_media_faturamento)


if __name__ == "__main__":
    menor_f, maior_f, acima_media = main()
    print(f"Menor Faturamento: {menor_f}")
    print(f"Maior Faturamento: {maior_f}")
    print(f"Quant dias acima da media Faturamento: {acima_media}")
