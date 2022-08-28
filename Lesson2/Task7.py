year = int(input("введите год"))
if year % 4 != 0:
    print("Год не высокосный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Год высокосный")
    else:
        print("Год не высокосный")
else:
    print("Год высокосный")


