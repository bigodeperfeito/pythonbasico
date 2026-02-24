import random

print ('***********************')
print('****Jogo adivinhação****')
print('************************')

numero_secreto = random.randint(1, 100)
total_tentativas = 5



for rodada in range(1, total_tentativas + 1):
    
    chute_str = input("Digite o seu numero de 1 a 100: ")
    
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("O número deve ser entre 1 e 100")
        continue

    print("Tentativa {} de {}".format(rodada, total_tentativas))
    print("Seu numero é:", chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você Acertou!!")
        break

    else:
        if(maior):
            print("O seu chute foi maior que o numero secreto")
        elif (menor):
            print("O seu chute foi menor que o numero secreto")
    rodada = rodada +1

print(numero_secreto)
print("Fim de jogo!")