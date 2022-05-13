#NUM 2
print("Введите возраст собаки")
a = float(input())
if a > 0 and a <= 2:
    a = a * 10.5
    print("Возраст собаки:", a)
else:
    a = a * 4
    print("Возраст собаки:", a)
