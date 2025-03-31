def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    pesos= money - int(expense) - 1
    centavos= int((1- (expense%1))*100)
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
change()
