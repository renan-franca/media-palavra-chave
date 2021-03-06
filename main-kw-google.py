# -*- coding: utf-8 -*-
"""Como analisar KW no Google Trends.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lwM78mbmqLiqHc1BCfrTBadvjPl5b1dp

**Contexto 📋 :** eu preciso descobrir boas oportunidades de palavras-chave que são muito buscadas e se mantêm estáveis ao longo do tempo. 

**Problema 👤:** encontrar uma ferramenta que permita comparar mais de 5 buscas de palavras-chave ao longo do tempo.

**Obetivo 👨🏽‍💻:** criar um programa que me permita buscar a média de buscas de cada palavra-chave e não fique restrito a apenas a 5 buscas.
"""

!pip install pytrends

import csv
from pytrends.request import TrendReq
pytrends = TrendReq(hl='pt-BR')

all_keywords = ['Javascript', 'Python', 'Java', 'PHP', 'CSS', 'HTML', 'C#', 'Golang']

timeframes = ['today 5-y', 'today 12-m', 'today 3-m', 'today 1-m']
cat = '0' 
geo = 'BR' 
gprop ='' 

def check_trends(searched_keyword):
  pytrends.build_payload(searched_keyword,
                         cat, 
                         timeframes[1], 
                         geo, 
                         gprop,)

  data = pytrends.interest_over_time() 
  return round(data.mean(),2) 

csv_data = [] 

for kw in all_keywords: 
  mean = check_trends([kw])
  print('O interesse médio por ' + kw + ' é: ' + str(mean[kw])) 
  csv_data.append({'keyword': kw, 'search value': str(mean[kw])})

with open('trends.csv', mode='w') as csv_file:  
    fieldnames = ['keyword', 'search value']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames) 
    writer.writeheader()
    writer.writerows(csv_data)