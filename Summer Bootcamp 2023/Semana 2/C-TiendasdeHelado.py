numSabores = int(input())

heladeria1 = list(map(int, input().split()))
heladeria2 = list(map(int, input().split()))

sumaSabores = [sabor_hel1 + sabor_hel2 for sabor_hel1, sabor_hel2 in zip(heladeria1, heladeria2)]

print(' '.join(map(str, sumaSabores)))
