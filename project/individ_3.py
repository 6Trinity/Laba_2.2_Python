import sys
import math

if __name__ == '__main__': day = int(input("Введите день: "))
s = float(10)
for i in range(day):
    s+= s + (s/100)
print("Суммарный путь на {0} день: {1} км".format(day, s))
