
def inversao_string(string_entrada):
    string_invertida = []

    for indice in range(len(string_entrada) - 1, -1, -1):
        string_invertida.append(string_entrada[indice])

    return "".join(string_invertida)

def main():
    print(inversao_string('abc'))
    print(inversao_string('amanha'))
    print(inversao_string('abacaxi'))
    print(inversao_string('ananana'))

if __name__ == '__main__':
    main()
