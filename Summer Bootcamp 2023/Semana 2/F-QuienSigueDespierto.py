p, v = map(int, input().split())
despierto = 0

for _ in range(p):
    luz = list(input().split())

    viviendas = list(zip(luz[0::2], luz[1::2]))

    for par in viviendas:
        if '#' in par:
            despierto += 1

print(despierto)
