#NUM 4
print("Введите название месяца с заглавной буквы")
mes = str(input())
max = ['Январь','Март','Май','Июль','Август','Октябрь','Декабрь']
iskl = str('Февраль')
if mes in max:
    print("В месяце", mes, "31 день")
if mes not in max and mes != iskl:
    print("В месяце", mes, "30 дней")
if mes == iskl:
    print ("В месяце", mes, "может быть 28 или 29 дней")
