test_cases = int(input())
results = []

for _ in range(test_cases):
    num_bombones, colorfavorito = map(int, input().split())

    coloresbombones = list(map(int, input().split()))

    hay = "NO"
    for color in coloresbombones:
        if colorfavorito == color:
            hay = "YES"
    results.append(hay)

for result in results:
    print(result)
a
