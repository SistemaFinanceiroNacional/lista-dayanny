# -*- coding: utf-8 -*-
"""Excercício 26

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e1qfpENv0omMLvWe03GtXJIu1va_rf3O

Exercício 26
"""

nome = str(input('Nome do produto:'))
quantEstoque = int(input('Quantidade atual em estoque:'))
quantMaxima = int(input('Quantidade máxima no estoque:'))
quantMinima = int(input('Quantidade mínima no estoque:'))

quantMedia = (quantMaxima + quantMinima)/2

if (quantEstoque >= quantMedia):
  print ('Não efetuar compra.')
else:
  print ('Efetuar compra.')