import random

print ("**********************")
print ("***jogo adivinhação***")
print ("**********************")

numero_secreto = random.randrange(1,101)
total_tentativas = 15
rodada = 1
dificuldade = (1, 2, 3)


print("Qual nível você escolhe?")
print("(1) Fácil (2) Médio (3) Difícil")

dificuldade = int(input("Defina o nível: "))

if(dificuldade == 1):
    total_tentativas = 15
if(dificuldade == 2):
    total_tentativas = 10
elif(dificuldade == 3):
    total_tentativas = 5

print("Suas tentativas: ", total_tentativas)


for rodada in range (1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))


    chute_str = input("Digite o seu numero: ")
    chute = int(chute_str)

    if(chute <1 or chute > 100):
        print("O número deve ser entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou")
        break
    else:
        if(maior):
            print("abaixa")
        elif(menor):
            print("Aumenta")

print(numero_secreto)
print("fim de jogo!")
