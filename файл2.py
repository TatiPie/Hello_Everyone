# x = open('text.txt', 'r')

# print(x.readline()) #прочитать первую строку
# print(x.readline()) #прочитать вторую строку
# x.close()
#
# x = open('text.txt', 'r')
#
# print(x.readlines()) #прочитать все строки
# x.close()

# f = open('xyz.txt', 'w') #откытие в режиме записи
# f.write('Hello \nWorld') #запись Hello World в файл
# f.close() #закрые файла

import os
# os.rename("xyz.txt", "abc.txt") #переименование xyz.txt в abc.txt
print("Текущая деректория:", os.getcwd()) #вывести текущую деректорию
# os.mkdir("folder") #создать пустой каталог (папку)
#изменение текущего каталога на 'folder'
# os.chdir("folder")
#вывод текущей папки
print("Текущая директория изменилась на folder:", os.getcwd())
#os.chdir("..") #вернуть в предыдущую директорию
print("Текущая директория изменилась:", os.getcwd())
# os.makedirs("nested1/nested2/nested3")  #сделать несколько вложенных папок

#удалить этот файл
# os.remove("abc.txt")

#удалить папку
# os.rmdir("folder")

#удалить вложенные папки
os.removedirs("nested1/nested2/nested3")

