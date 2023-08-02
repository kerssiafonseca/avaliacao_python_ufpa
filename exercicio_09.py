import datetime
import time

def exibir_hora_atual():
    while True:
        # Obter a hora atual
        hora_atual = datetime.datetime.now()
        
        # Formatando a hora para exibição
        hora_formatada = hora_atual.strftime("%H:%M:%S")
        
        # Limpar a tela para mostrar a hora atualizada
        print("\033c", end="")
        
        # Exibir a hora atual
        print(f"Hora atual: {hora_formatada}", end="", flush=True)
        
        # Aguardar um segundo antes de atualizar novamente
        time.sleep(1)

# Chamar a função para começar a exibir a hora atual
exibir_hora_atual()