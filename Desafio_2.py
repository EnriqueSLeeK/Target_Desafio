
def fib(fator):

    if fator < 0:
        return 0

    if fator == 0:
        return 0
    elif fator == 1:
        return 1

    return fib(fator - 1) + fib(fator - 2)

def verifica_numero_sequencia(numero):

    fator = 0
    numero_na_sequencia = 0
    while numero >= numero_na_sequencia:
        if numero == numero_na_sequencia:
            return f"Pertence a sequencia: {numero}"
        fator += 1
        numero_na_sequencia = fib(fator)

    return f"Nao pertence a sequencia: {numero}"


def main():
    print(verifica_numero_sequencia(21))
    print(verifica_numero_sequencia(3))
    print(verifica_numero_sequencia(2))
    print(verifica_numero_sequencia(99))
    print(verifica_numero_sequencia(-6))
    print(verifica_numero_sequencia(111))

if __name__ == "__main__":
    main()

    
