# -*- coding: utf-8 -*-
"""Excercício 29

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e1qfpENv0omMLvWe03GtXJIu1va_rf3O

Exercício 29
"""

print ('Informe valores diferentes!')
valor1 = int(input('Informe um valor:'))
valor2 = int(input('Informe um valor:'))

if (valor2> valor1):
  X = valor1
  valor1 = valor2
  valor2 = X

valor3 = int(input('Informe um valor:'))

if (valor3> valor2):
  X = valor2
  valor2 = valor3
  valor3 = X

print ('A soma dos maiores valores é:', valor1+valor24)