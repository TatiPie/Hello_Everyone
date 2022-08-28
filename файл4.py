f = open('word.txt')
b = [] #список со словами
n = [] #список с числами
s = f.readlines()
print(s)
for i in s:
    i = i[:-1]
    if i.isalpha(): #определяет является ли элемент буквами
        i = str(i)
        b.append(i)
    elif i.isdigit(): #определяет является ли элемент числом, цифрами
        i = int(i)
        n.append(i)
print(b)
print(n)
n.sort()
b.sort()
mas = n + b
print(mas)
