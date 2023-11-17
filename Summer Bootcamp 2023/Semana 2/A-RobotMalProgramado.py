inteiros = list(map(int, input().split()))

soma_acumulativa = [inteiros[0]]

for num in range(1, len(inteiros)):
    frequencia = soma_acumulativa[num - 1] + inteiros[num]
    soma_acumulativa.append(frequencia)
    num += 1

print(' '.join(map(str, soma_acumulativa)))
