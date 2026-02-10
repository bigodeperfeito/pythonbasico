while True:
    try:
        valor = float (input("Digite um valor para sacar"))

        if 0 <= valor <=1000:
            break
        else:
            print("O valor deve ser entre 0 e 1000:")
    except ValueError:
        print("O valor deve ser inteiro:")

print("O saque foi de:", valor)
