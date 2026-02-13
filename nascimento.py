while True:
    try:
        nascimento = int (input("Digite seu ano de nascimento: "))
        
        if 1900 <= nascimento <= 2026:
            break
        else:
            print("O ano deve ser entre 1900 e 2026. ")
    except ValueError:
        print("Digite um ano de nascimento valido")

print ("Ano de nascimento registrado! ", nascimento)