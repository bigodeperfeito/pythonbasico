while True:
    nome= input ("Digite seu nome:")
    senha = input ("Digite sua senha:")

    if nome=="":
        print("O nome não pode ser vazio.")
    else:
        break
    
print("Nome",nome)

while true:
        senha = input ("Digite sua senha: (max. 0 caracterers):")

        if len(senha)<=0:
            break
        else:
            print("A senha deve ter 6 caracters no máximo")

print("conta registrada", senha)
