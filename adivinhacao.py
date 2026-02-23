print ('***********************')
print('****Jogo adivinhação****')
print('************************')

numero_secreto = 39

chute_str = input("Digite o seu numero:")

print("Seu numero é:", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print("Você Acertou!!")

else:
    print("Você errou :(")