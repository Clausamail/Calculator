from math import *
i = 0
def f():
    a = int(input("Введите первое число: "))
    b = input("Введите оператор(+, -, /, *): ")
    c = int(input("Введите второе число: "))
    if b == '+':
        print(a+c)
    elif b == '-':
        print(a-c)
    elif b == '*':
        print(a * c)
    elif b == '/':
        if c == 0:
            print("Делить на 0 нельзя!")
        else:
            print("%.2f" % (a / c))
    else:
        global i
        if i > 2:
            print("Ты совсем тупой???")
        else:
            print("Попробуй снова.")
        i+=1
        f()
f()
while True:
    f()