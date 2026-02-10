while True:
    nome= input ("Digite seu nome:")

    if nome=="":
        print("O nome não pode ser vazio.")
    else:
        break
    
print("Nome",nome)

while True:
        senha = input ("Digite sua senha: (max. 6 caracterers):")

        if len(senha)<=6:
            break
        else:
            print("A senha deve ter 6 caracters no máximo")

print("conta registrada", senha)
