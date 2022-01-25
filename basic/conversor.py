money = float(input("Ingresa la cantidad en pesos mexicanos: "))
dollar_value = 20.18
converted = str(round(money / dollar_value, 2))
print(f"Los ${money} equivalen a ${converted} dólares")
