import random

# Cores no Terminal PY
VERMELHO = "\033[31m"
VERDE    = "\033[32m"
AMARELO  = "\033[33m"
AZUL     = "\033[34m"
RESET    = "\033[0m"

def jogar():
    print(f"{AZUL}**************************")
    print("*****Jogo adivinhação*****")
    print(f"**************************{RESET}")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0

    print("\nQual dificuldade você gostaria de jogar?")
    print(f"{VERDE}(1) Fácil{RESET} | {AMARELO}(2) Médio{RESET} | {VERMELHO}(3) Difícil{RESET}")

    # Seleção de dificuldade com validação
    while True:
        try:
            dificuldade = int(input("Defina a dificuldade (1-2-3): "))
            if dificuldade == 1:
                total_tentativas = 10
                break
            elif dificuldade == 2:
                total_tentativas = 5
                break
            elif dificuldade == 3:
                total_tentativas = 3
                break
            else:
                print(f"{AMARELO}Opção inválida! Digite 1, 2 ou 3.{RESET}")
        except ValueError:
            print(f"{VERMELHO}Por favor, digite um número inteiro.{RESET}")

    print(f"\nVocê terá {total_tentativas} tentativas.")

    # Loop principal das rodadas
    for rodada in range(1, total_tentativas + 1):
        print(f"\n{AMARELO}Tentativa {rodada} de {total_tentativas}{RESET}")
        
        try:
            chute_str = input(f"{AZUL}Digite o seu numero (1-100): {RESET}")
            chute = int(chute_str)

            if chute < 1 or chute > 100:
                print(f"{AMARELO}O número deve ser entre 1 e 100!{RESET}")
                continue

            acertou = chute == numero_secreto
            maior   = chute > numero_secreto

            if acertou:
                print(f"{VERDE}É isso meno você é foda!{RESET}")
                break
            else:
                if maior:
                    print(f"{VERMELHO}Diminuiii!{RESET}")
                else:
                    print(f"{VERMELHO}Aumenta o bagulho!{RESET}")
        
        except ValueError:
            print(f"{VERMELHO}Meno, digita um número válido!{RESET}")

    # Finalização
    print(f"\n{AZUL}O número secreto era: {numero_secreto}{RESET}")
    print(f"{AZUL}Boa meno tenta de novo se tu é bem home{RESET}")

if __name__ == "__main__":
    jogar()