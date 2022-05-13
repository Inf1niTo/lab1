#NUM 5
print("Введите буквенную координату")
p = str(input())
bykvi = ['o', 'a', 'b', 'c', 'd', 'i', 'f', 'g', 'h']
z = (bykvi.index(p))
print("Введите числовую координату")
num = int(input())
if (z+num) % 2 == 0:
    print("Клетка черная")
else:
    print("Клетка белая")
