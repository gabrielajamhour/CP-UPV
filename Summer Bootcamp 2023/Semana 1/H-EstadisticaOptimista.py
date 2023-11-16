num_notas = int(input())
notas = list(map(float, input().split()))

notas_lista = [nota for nota in notas if nota >= 5]

soma = 0
for nota in notas_lista:
        soma += nota

media = soma / len(notas_lista)

print(f'{media:.2f}')
