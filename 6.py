#NUM 6
print("Введите год")
a = int(input())
if a % 400 == 0:
    print(a, ", год - високосный")
elif a % 100 == 0:
    print(a, ", год - не високосный")
elif a % 4 == 0:
    print(a, ", год - високосный")
else:
    print(a, ", год - не високосный")