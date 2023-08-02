continuar = True
while continuar == True:
    salario = input("Digite o Salario do funcionario para obter o valor com reajuste: ")
    percentual = input("Digite o percentual de acrescimo do funcionario para obter o valor com reajuste: ")

    if str(salario).isnumeric() and str(percentual).isnumeric:
        salario = float(salario)
        percentual = float(percentual)
        salario_com_reajuste = (salario * (percentual/100)) + salario
        print("salário com reajuste de ", percentual,"% ",salario_com_reajuste)
        resposta = input("Deseja continuar? (S/N): ")
        if resposta.upper() == "S":
            continuar = True
        elif resposta.upper() == "N":
            print("programa finalizado!")
            continuar = False
        else:
            print("Opção inválida. Digite S para Sim ou N para Não.")
    else:
        print('por favor digite apenas um valores numéricos')

