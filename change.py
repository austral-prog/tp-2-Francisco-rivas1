def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("Vuelto")
    pesos= money - int(expense) - 1
    centavos= 1 - (expense%1)
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
change()
