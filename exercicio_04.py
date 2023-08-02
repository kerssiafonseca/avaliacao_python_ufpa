peso_saco_racao = float(input("Digite o peso do saco de ração: "))
qtd_gramas_racao = float(input("Digite a quantidade de gramas para a alimentação dos gatos: "))
contador = 0

peso_saco_gramas = (peso_saco_racao * 1000)
while contador < 5:
    peso_saco_gramas -= (qtd_gramas_racao * 2)
    contador += 1

if peso_saco_gramas<0:
    print("A ração acabou")

print(peso_saco_gramas)


