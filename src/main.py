# Script principal do motor de eventos
import os

print("Lista de comandos: ")
print("$LS: Lista os arquivos no diretório")
print("$MNT nome_do_arquivo.asm: Ativa o montador que converte o arquivo Assembly em hexadecimal")
print("$RUN nome_do_arquivo.hex: Roda o programa hexadecimal")
print("$EXT: Termina a execução do sistema\n")

while(True): # Loop Infinito
    input_text = input("> $") # Pega comando do usuário

    if input_text == "LS":
        dir = os.listdir('./user')
        print("  | Arquivo")
        print("--+---------")
        for i in range(0, len(dir)):
            print(str(i) + " | " + dir[i])

    if input_text == "EXT": 
        exit()