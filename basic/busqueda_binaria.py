# funciona solamente cuando el conjunto está ordenado
objetivo = int(input('Escoge número para sacar su raíz cuadrada: '))
epsilon = 0.001
bajo = 0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo)/2
    
print(f'La raíz cuadrada de {objetivo} es {respuesta}')
