# -*- coding: utf-8 -*-
"""Excercício 30

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e1qfpENv0omMLvWe03GtXJIu1va_rf3O

Exercício 30
"""

valor1 = int(input('Informe um valor:'))
valor2 = int(input('Informe um valor:'))
valor3 = int(input('Informe um valor:'))

if (valor1 < valor2) and (valor2 < valor3):
  print (valor1,'-',valor2,'-',valor3)
elif (valor3 < valor2) and (valor2 < valor1):
  print (valor3,'-',valor2,'-',valor1)
elif (valor1 > valor2) and (valor3 > valor2) and (valor3 < valor1):
  print (valor2,'-',valor3,'-', valor1)
elif (valor3 > valor1) and (valor3 > valor2) and (valor1 > valor2):
  print (valor2,'-',valor1,'-',valor3)
elif (valor2 > valor1) and (valor2 > valor3) and (valor1 > valor3):
  print (valor3,'-',valor1,'-',valor2)
else:
  print (valor1,'-',valor3,'-', valor2)