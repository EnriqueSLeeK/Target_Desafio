
dados = {
    'SP': 67836.43 ,
    'RJ': 36678.66 ,
    'MG': 29229.88 ,
    'ES': 27165.48 ,
    'Outros': 19849.53 ,
}

def main():
    valores = [dados[estado] for estado in dados]
    soma = sum(valores)
    porcentagens = [(valor * 100) / soma for valor in valores]
    tabela_porcentagem = {estado: porcentagem for estado, porcentagem in zip(dados, porcentagens)}
    return tabela_porcentagem


if __name__ == '__main__':
    tabela_porcentagem = main()
    for estado in tabela_porcentagem:
        print(f"{estado}: {tabela_porcentagem[estado]}")

