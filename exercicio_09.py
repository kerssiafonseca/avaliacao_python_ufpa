import datetime
import time

def exibir_hora_atual():
    while True:
        # Obter o objeto de hora atual
        hora_atual = datetime.datetime.now()
        
        # Definir o fuso horário da máquina
        fuso_horario_maquina = hora_atual.astimezone().tzinfo
        
        # Obter a hora atual no fuso horário da máquina
        hora_atual_fuso_horario_maquina = hora_atual.astimezone(fuso_horario_maquina)
        
        # Formatando a hora para exibição
        hora_formatada = hora_atual_fuso_horario_maquina.strftime("%H:%M:%S")
        
        # Limpar a tela para mostrar a hora atualizada
        print("\033c", end="")
        
        # Exibir a hora atual
        print(f"Hora atual: ({fuso_horario_maquina}): {hora_formatada}", end="", flush=True)
        
        # Aguardar um segundo antes de atualizar novamente
        time.sleep(1)

# Chamar a função para começar a exibir a hora atual
exibir_hora_atual()