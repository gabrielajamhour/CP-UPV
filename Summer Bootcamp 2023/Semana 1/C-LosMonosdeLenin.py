n1 = int(input())
inteiros = list(map(int, input().split()))
n2 = int(input())
alfabeto = list(map(str, input().split()))
n3 = int(input())
string = input()

inteiros_new = []
for num in inteiros:
    num_final = num * 2
    inteiros_new.append(num_final)
inteiros_final = [str(num) for num in inteiros_new]
print(" ".join(inteiros_final))

alfabeto_final = []
for char in alfabeto:
    maiusculas = char.upper()
    alfabeto_final.append(maiusculas)
print(" ".join(alfabeto_final))

string_final = ''
for letra in string:
    if letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or letra == "I" or letra == "o" or letra == "O" or letra == "u" or letra == "U":
        string_final += '0'
    else:
        string_final += letra
print(string_final)
a
