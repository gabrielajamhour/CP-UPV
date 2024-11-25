longitud = int(input())

array1 = list(map(str, input().split()))
array2 = list(map(str, input().split()))

array1_out = []
array2_out = []

for i in range(longitud):
    if i % 2 == 0:
        array1_out.append(array1[i])
        array2_out.append(array2[i])
    else:
        array1_out.append(array2[i])
        array2_out.append(array1[i])

print(' '.join(array1_out))
print(' '.join(array2_out))
a
