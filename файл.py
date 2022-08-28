f = open('example.txt', 'r') #открыть файл из рабочей директории в режиме чтения
#fp = open('C:/xyz.txt', 'r') #открыть файл из любого каталога
# try:
#     print(*f) #выводим содержимое файла
#     print(f) #выводим объект
# finally:
#     f.close()
#
# with open('example.txt') as f:
#     print(*f) #работа с файлом

print(f.read(7)) #чтение 7 символов из example.txt
print(f.read(7))
print(f.read())
f.close()






