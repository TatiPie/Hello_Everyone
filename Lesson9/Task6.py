#Оперрация del - удаление элемента из словаря
#Исходный словарь
Salary = {'Director': 120,
          'Secretary': 100,
          'Cleaner': 50}
print(Salary)
#Удалить элемент по ключу Secretary
# del Salary ['Secretary']
# print(Salary)

#Удалить элемент по ключу 'Secretary' с проверкой
key = 'Secretary'
if key in Salary:
    del Salary['Secretary']
    print(Salary)
    