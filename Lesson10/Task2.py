string_set = {"Nicholas", "Michelle", "John", "Mercy"}
print(string_set)

mixed_set = {2.0, "Nicholas", (1,2,3)}
print(mixed_set)

num_set = set([1, 2, 5, 3, 4, 4, 5, 6])
print(num_set)

x = {}
print(type(x))

x = set()
print(type(x))

month = set(["Jan", "Feb", "March", "Apr"])
for n in month:
    print(n)

month = set(["Jan", "Feb", "March", "Apr", "May"])
print('May' in month)

month = set(["Jan", "Feb", "March", "Apr", "May"])
month.add("June")
print(month)

num_set = {1, 2, 3, 4, 5, 6}
num_set.discard(3) #здесь если удалить элемент которого нет например 10, не выдаст ошибку
print(num_set)

num_set = {1, 2, 3, 4, 5, 6}
num_set.remove(3) #здесь если удалить элемент которого нет например 7, то выдаст ошибку
print(num_set)

num_set = {1, 2, 3, 4, 5, 6}
print(num_set.pop()) #метод pop() во множестве удаляет случайный элемент
print(num_set)

num_set = {1, 2, 3, 4, 5, 6}
num_set.clear() #этот метод помогает удалить все элементы во множестве
print(num_set)

month_a = set(["Jan", "Feb", "March", "Apr", "May"])
month_b = set(["June", "July", "Aug", "Sep", "Oct"])
all_month = month_a.union(month_b) #этот метод объединяет множество путем добавления в первое
# множество второе множество, также может объединять неограниченное количество множеств
print(all_month)

month_a = set(["Jan", "Feb", "March", "Apr", "May"])
month_b = set(["June", "July", "Aug", "Sep", "Oct"])
print(month_a | month_b)

x = {1, 2, 3}
y = {4, 3, 6}
print(x & y) #Оператор & and

A = {1, 2, 3}
B = {4, 3, 6}
print(A - B) #выводим все элементы множества А которые не содержатся во множестве В
print(B - A) #выводим все элементы множества В которые не содержатся во множестве А


