import random

print ('***********************')
print('****Jogo adivinhação****')
print('************************')

numero_secreto = random.randint(1, 100)
total_tentativas = 5
rodada = 1

while(rodada <= total_tentativas):
    chute_str = input("Digite o seu numero de 1 a 100: ")
    print("Seu numero é:", chute_str)

    chute = int(chute_str)

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