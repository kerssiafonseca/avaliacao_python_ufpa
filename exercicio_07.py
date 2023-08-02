posicoes_fibonacci = int(input(
    "Digite quantos numeros da sequencia de fibonacci você deseja visualizar: "
))

contador = 2 
sequencia_fibonacci = [1,1]

while contador < posicoes_fibonacci:
    elemento_fibonacci = sequencia_fibonacci[contador - 1] + sequencia_fibonacci[contador - 2]
    sequencia_fibonacci.append(elemento_fibonacci)
    contador += 1

print(sequencia_fibonacci)

if posicoes_fibonacci in sequencia_fibonacci:
    indice_valor = sequencia_fibonacci.index(posicoes_fibonacci)
    print("O numero que você digitou faz parte da sequencia de fibonacci, ele se encontra na posição: ", indice_valor+1)
else:
    print("O numero que você digitou não faz parte da sequencia de fibonacci exibida")
