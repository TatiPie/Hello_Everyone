#Создайте словарь из строки 'hellomynameis" следующим образом
#в качестве ключей возьмите буквы строки, а значениями пусть будут числа
#соответствующие количеству вложений данной буквы в строку
str = 'hellomynameis'
dictionary_1 = {key: str.count(key) for key in str}
print(dictionary_1)



