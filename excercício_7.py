# -*- coding: utf-8 -*-
"""Excercício 7

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e1qfpENv0omMLvWe03GtXJIu1va_rf3O

Exercício 7
"""

quantDiasAno = 365
quantDiasMes = 30

print ("Informe sua idade atual em anos, meses e dias.")

anos = int (input('Quantidade de anos: '))
meses = int (input('Quantidade de meses: '))
dias = int (input('quantidade de dias: '))

diasEmMeses = quantDiasMes * meses
diasEmAnos = quantDiasAno * anos

print ('Você viveu: ',dias+diasEmMeses+diasEmAnos, 'dias.')