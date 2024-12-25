# -*- coding: utf-8 -*-
"лаба 1"
import math

x = float(input("Введите x: "))
y = float(input("Введите y: "))

fx = math.pow(x, 2)
ch = x - y
def switch(ch):
    if ch == 0:
        return math.pow(fx, 2) + math.pow(y, 2) + math.sin(y)
    elif ch > 0:
        return math.pow((fx - y), 2) + math.cos(y)
    elif ch < 0:
        return math.pow(y - fx, 2) + math.tan(y)

# Вызов функции и сохранение результата в c
c = switch(ch)

print(c)

