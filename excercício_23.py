# -*- coding: utf-8 -*-
"""Excercício 23

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e1qfpENv0omMLvWe03GtXJIu1va_rf3O

Exercício 23
"""

nome = str(input('Informe o nome:'))
sexo = str(input('Informe o sexo. F para feminino e M para masculino:'))
altura = float(input('Informe a altura:')) #faltou a altura
s = sexo.upper() #faltou usar o método upper()

if (s == 'M'):
  peso_ideal = (72.7 * altura) - 58
else:
  peso_ideal = (62.1 * altura) - 44.7

print ('O peso ideal é:', '%.1f' %peso_ideal)