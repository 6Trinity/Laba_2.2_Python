import math
import sys

if __name__ == '__main__': n = float(input("Введите день недели: "))
if n <  0 and n > 7: print("Illegal value of a", file=sys.stderr), exit(1)
if n == 1 : print("Понедельник")
elif n == 2 : print("Вторник")
elif n == 3: print("Среда")
elif n == 4 : print("Четверг")
elif n == 5 : print("Пятница")
elif n == 6 : print("Суббота")
elif n == 7 : print("Воскресенье")
else: print("Ошибка!", file=sys.stderr), exit(1)