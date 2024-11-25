n = int(input())
print('+---+' + '---+' * (n-1))

for _ in range(n):
    for _ in range(3):
        print('|   |' + '   |' * (n-1))
        
    print('+---+' + '---+' * (n-1))
