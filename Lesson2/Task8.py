import math
a = int(input("Введите сторону треугольника"))
b = int(input("Введите сторону треугольника"))
c = int(input("Введите сторону треугольника"))
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print ("Треугольник не существует")
    elif a == b and a == c:
        print("Равносторонний")
    elif a == b or a == c or b == c:
        print("Равнобедренный")
    else:
        print("Разносторонний")



