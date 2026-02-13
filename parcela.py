while True:
    try:
        parcela = int (input("Digite um numero de parcelas: "))
        
        if 1 <= parcela <= 12:
            break
        else:
            print("As parcelas devem ser entre 1 e 12. ")
    except ValueError:
        print("Digite apenas números")

print ("parcelas registrada! ", parcela)