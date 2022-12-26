import sys
import math

if __name__ == '__main__': a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
for i in (a,b,c):
    if abs(i) >= 4:
        print(i)
