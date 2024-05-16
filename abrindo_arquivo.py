# -*- coding: utf-8 -*-
"""
Vornei
"""
# Junior:
arquivo = open('nome_arquivo.txt')
print(arquivo.read())
arquivo.close()

# Senior:
with open('nome_arquivo.txt') as arquivo:
    print(arquivo.read())