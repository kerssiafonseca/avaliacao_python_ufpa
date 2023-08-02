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
funcionarios = []
soma_salarios_funcionarios = 0

while continuar == True:
    nome_funcionario = input("Digite o nome do funcionario: ")
    salario_atual = input("Digite o Salario do funcionario para obter o valor com reajuste: ")

    if str(salario_atual).isnumeric():
        funcionario = {
            "nome": nome_funcionario,
            "salario": float(salario_atual)
        }

        funcionarios.append(funcionario)

    else:
        print('por favor digite um valor numérico')

    resposta = input("Deseja adicionar mais um funcionario? (S/N): ")

    if resposta.upper() == "S":
        continuar = True
    elif resposta.upper() == "N":
        print("programa finalizado!")
        continuar = False
    else:
        print("Opção inválida. Digite S para Sim ou N para Não.")


for funcionario in funcionarios:
    salario_com_reajuste = calcularReajuste(funcionario["salario"])
    soma_salarios_funcionarios += salario_com_reajuste
    print("O salario com reajuste do funcionário "+ funcionario["nome"] + " é: "+ str(salario_com_reajuste))

print("O total de todos os salarios dos funcionarios com reajuste é: ", soma_salarios_funcionarios)


