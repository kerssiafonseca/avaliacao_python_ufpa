continuar = True
while continuar == True:
    salario = input("Digite o Salario do funcionario para obter o valor com reajuste: ")

    if str(salario).isnumeric():
        salario = float(salario)
        salario_com_reajuste = (salario * 0.25) + salario
        print("salário com reajuste de 25%: ",salario_com_reajuste)
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

