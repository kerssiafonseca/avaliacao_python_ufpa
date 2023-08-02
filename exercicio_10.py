def calcularQtdParImpar(valores):
    contador_impares = 0
    contador_pares = 0
    for valor in valores:
        if valor % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
    print("a quantidade de numeros pares digitada é: "+ str(contador_pares) + " e a quantidade de numeros impares é: "+ str(contador_impares))

def calcularMedia(valores):
    soma = sum(valores)
    media = soma/len(valores)
    print("A média aritmética dos valores digitados é igual a :"+ str(media))

def calcularMediaPares(valores):
    valores_pares = []
    for valor in valores:
        if valor % 2 == 0:
            valores_pares.append(valor)
    media_pares = sum(valores_pares)/len(valores_pares)

    print("O resultado da média aritmética dos valores pares é igual a: "+ str(media_pares))

continuar = True
valores = []

while continuar == True:

    valor = float(input("Digite um valor: "))

    if valor >= 0:
        valores.append(int(valor))
    else:
        print("Digite apenas valores numéricos positivos")

    resposta = input("Deseja adicionar mais um valor? (S/N): ")

    if resposta.upper() == "S":
        continuar = True
    elif resposta.upper() == "N":
        print("programa finalizado!")
        continuar = False
    else:
        print("Opção inválida. Digite S para Sim ou N para Não.")


calcularQtdParImpar(valores)
calcularMediaPares(valores)
calcularMedia(valores)

