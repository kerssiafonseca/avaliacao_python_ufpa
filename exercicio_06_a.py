def calcularReajuste(salario_atual):
    salario_com_reajuste = 0
    if salario_atual <= 1500:
        salario_com_reajuste = (salario_atual * 0.25) + salario_atual
    elif salario_atual <=3000:
        salario_com_reajuste = (salario_atual * 0.20) + salario_atual
    elif salario_atual <=6000:
        salario_com_reajuste = (salario_atual * 0.15) + salario_atual
    else:
        salario_com_reajuste = (salario_atual * 0.10) + salario_atual
    return salario_com_reajuste

continuar = True

while continuar == True:
    nome_funcionario = input("Digite o nome do funcionario: ")
    salario_atual = input("Digite o Salario do funcionario para obter o valor com reajuste: ")

    if str(salario_atual).isnumeric():
        salario_atual = float(salario_atual)

        salario_com_reajuste = calcularReajuste(salario_atual)

        print("O salario com reajuste do funcionário "+ nome_funcionario + " é: "+ str(salario_com_reajuste))

        resposta = input("Deseja continuar? (S/N): ")
        if resposta.upper() == "S":
            continuar = True
        elif resposta.upper() == "N":
            print("programa finalizado!")
            continuar = False
        else:
            print("Opção inválida. Digite S para Sim ou N para Não.")
    else:
        print('por favor digite um valor numérico')



