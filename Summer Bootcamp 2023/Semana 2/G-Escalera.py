alturas = list(map(int, input().split()))

analisis = ''
for a in range(1, len(alturas)):
    if alturas[a - 1] < alturas[a]:
        analisis += 'S'
    elif alturas[a - 1] == alturas[a]:
        analisis += 'I'
    else:
        analisis += 'B'

print(analisis)
