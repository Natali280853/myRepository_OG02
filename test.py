op_add = '+'
op_sub = '-'
op_mult = '*'
op_div = '/'

try:
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    oper_usr = input("Введите операцию (" + op_add + ", " + op_sub + ", " + op_mult + ", " + op_div + "): ")

    if oper_usr == op_add:
        print(num1 + num2)

    elif oper_usr == op_sub:
        print(num1 - num2)

    elif oper_usr == op_mult:
        print(num1 * num2)

    elif oper_usr == op_div:
        if num2 == 0:
            print("Ошибка: деление на ноль!")
        else:
            print(num1 / num2)
    else:
        print("Ошибка: Неизвестная операция!")

except ValueError:
    print("Ошибка: Некорректный ввод числа!")
except Exception as e:
    print(f"Необработанное исключение: {e}")
