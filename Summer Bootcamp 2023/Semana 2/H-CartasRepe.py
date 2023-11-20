def cartas_iguales(amigo1, amigo2):
    amigo1.sort()
    amigo2.sort()
    
    # Método de dos punteros (2 pointer technique)
    puntero1 = 0
    puntero2 = 0

    cartas_iguales = []

    while puntero1 < len(amigo1) and puntero2 < len(amigo2):
        if amigo1[puntero1] == amigo2[puntero2]:
            # Si las cartas son iguales, adiciona a la lista de cartas iguales
            cartas_iguales.append(amigo1[puntero1])
            puntero1 += 1
            puntero2 += 1
        elif amigo1[puntero1] < amigo2[puntero2]:
            puntero1 += 1
        else:
            puntero2 += 1

    return cartas_iguales

a, b = map(int, input().split())
cartas_amigo1 = list(map(int, input().split()))
cartas_amigo2 = list(map(int, input().split()))

resultado = cartas_iguales(cartas_amigo1, cartas_amigo2)
resultado = [str(i) for i in resultado]
print(' '.join(resultado))
