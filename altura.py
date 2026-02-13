while True:
    try:
        altura = float (input("Digite sua altura: "))
        
        if 0 <= altura:
            break
        else:
            print("A nota deve ser maior que 0. ")
    except ValueError:
        print("Digite uma altura vàlida")

print ("Altura registrada! ", altura)