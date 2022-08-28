#Исключения

#Конструкция try - except для обработки исключения
try:
   k = 1 / 0
except ZeroDivisionError:
   k = 0
print(k)

my_dict = {"a": 1, "b": 2, "c": 3}
try:
   value = my_dict["d"]
except IndexError:
   print("Такого индекса не существует")
except KeyError:
   print("Этого ключа нет в словаре")
except:
   print("Произошла другая оибка")

my_dict = {"a": 1, "b": 2, "c": 3}
try:
   value = my_dict["d"]
except (IndexError, KeyError):
   print("Произошла ошибка IndexError или KeyError!")
finally:
   print("Оператор finally выполнен!")
   




