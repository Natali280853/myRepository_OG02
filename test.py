oper_add = '+'
oper_sub = '-'
oper_mult = '*'
oper_div = '/'

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

oper_usr = input("Введите операцию (" + oper_add + ", " + oper_sub + ", " + oper_mult + ", " + oper_div + "): ")

if oper_usr == oper_add:
    print(num1 + num2)

elif oper_usr == oper_sub:
    print(num1 - num2)

elif oper_usr == oper_mult:
    print(num1 * num2)

elif oper_usr == oper_div:
    print(num1 / num2)
else:
    print("Ошибка: Неизвестная операция!")
