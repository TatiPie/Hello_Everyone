a = input('введите строкку:')
b = input('введите символ:')
c = ''
for i in a:
    if i != b:
        c += i
print('Pезультат:',c)
