n, m = map(int, input().split())

matriz = [list(map(str, input().split())) for _ in range(n)]

# Cria matriz_vuelva om as dimensões contrárias à matriz
matriz_vuelva = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
            matriz_vuelva[i][j] = matriz[n-j-1][i]
            # Se pone [n-j-1] para que no sea necesario crear un while con una variable x que variara de 1 a n

for linea in matriz_vuelva:
      print(' '.join(linea))
a
