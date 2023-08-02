def calcular_pagamento_emprestimo(P, A, i):
    saldo_devedor = P
    juros_acumulados = 0
    meses = 0

    while saldo_devedor >= A:
        juros = saldo_devedor * (i / 100)
        abatimento = A - juros
        saldo_devedor -= abatimento
        juros_acumulados += juros
        meses += 1

        print(f"Mês {meses}:")
        print(f"Valor em dinheiro dos juros pagos: R$ {juros:.2f}")
        print(f"Valor em dinheiro aplicado no pagamento da dívida: R$ {abatimento:.2f}")
        print(f"Valor acumulado de juros já pagos: R$ {juros_acumulados:.2f}")
        print(f"Valor ainda por pagar do empréstimo: R$ {saldo_devedor:.2f}")
        print()

    saldo_residual = saldo_devedor
    print("Resultado final:")
    print(f"Número de meses necessários para pagar o empréstimo: {meses}")
    print(f"Valor da última prestação (saldo residual): R$ {saldo_residual:.2f}")

# Exemplo de uso
calcular_pagamento_emprestimo(1000, 150, 1.5)

