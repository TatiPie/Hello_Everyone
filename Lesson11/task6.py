# Даны два списка чисел. Посчитайте сколько чисел содержится одновременно как в первом
# списке, так и во втором
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 5, 8, 6]
set1 = set(list1)
set2 = set(list2)
intersection = set1.intersection(set2)
print(len(intersection))

