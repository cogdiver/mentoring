# Explorar modulos
import time
import datetime
import re


def sumar2(valor):
  return valor + 2

def winner(user_option, computer_option):
  return 0, 1

print(sumar2(4))
print(sumar2(7))
print(winner(1,2))

mi_lista = []
for i in range(10):
    value = i + 1
    if value % 2 == 0:
        mi_lista.append(value)

mi_lista_2 = [i for i in range(1, 11) if i % 2 == 0]

print(mi_lista)
print(mi_lista_2)
