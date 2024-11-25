lado = int(input())
espaço1 = input()

tostadaAntes = [list(map(str, input().strip())) for _ in range(lado)]

espaço2 = input()

tostadaDespues = [list(map(str, input().strip())) for _ in range(lado)]

if all(all(elemento != '#' for elemento in linea) for linea in tostadaAntes):
# Verifica em nenhuma das linhas de "tostadaAntes" tem mermelada
    print("NO LLEVABA MERMELADA")
elif tostadaAntes == tostadaDespues:
    print("HA HABIDO SUERTE")
else:
    print("TRAGEDIA")
a
