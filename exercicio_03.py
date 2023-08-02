from datetime import datetime

while True:
    data_usuario_str = input("Digite a data no formato dd/mm/yyyy: ")

    try:
        # Tenta converter a string para um objeto datetime
        data_usuario = datetime.strptime(data_usuario_str, '%d/%m/%Y')
        break  # Se a conversão foi bem sucedida, sai do loop
    except ValueError:
        print("Data inválida. Tente novamente.")

# Se chegou aqui, a data do usuário é válida e foi convertida para datetime
data_hora_atual = datetime.now()
diferenca = data_hora_atual - data_usuario

print("Diferença em anos:", diferenca.days // 365)
print("Diferença em meses:", diferenca.days//30)
print("Diferença em semanas: ",diferenca.days // 7)
print("Diferença em dias:", diferenca.days)
print("Diferença em horas:", diferenca.total_seconds() // 3600)
print("Diferença em minutos:", diferenca.total_seconds() // 60)
print("Diferença em segundos:", diferenca.total_seconds())


