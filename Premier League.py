#!/usr/bin/env python
# coding: utf-8

# In[65]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
from lxml import html
from lxml.html import fromstring
import lxml.html as lh
import urllib.request
from urllib.request import urlopen
import random
import re
import scrapy
import csv


# In[4]:


url = 'https://www.transfermarkt.es/premier-league/startseite/wettbewerb/GB1/saison_id/2019'


# In[6]:


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
pageTree = requests.get(url, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')


# In[56]:


array_team = []
pl_teams = pageSoup.find_all('td',{'class':'hauptlink no-border-links show-for-small show-for-pad'},'a')
for i in pl_teams:
    array_team.append(i.text)


# In[45]:


#indexage = 0
#pl_ageav = pageSoup.find_all('td',{'class':'zentriert hide-for-small hide-for-pad'})
#for i in pl_ageav:
 #   indexage += 1
    #if indexage%2 != 0 and indexage !=1:
      #  print(i.text)


# In[50]:


array_values = []
indexv = 0
pl_value = pageSoup.find_all('td',{'class':'rechts hide-for-small hide-for-pad'},"a")
for i in pl_value:
    indexv += 1
    if indexv%2 != 0 and indexv != 1:
        array_values.append(i.text)


# In[51]:


array_values_prom = []
indexv2 = 0
pl_value2 = pageSoup.find_all('td',{'class':'rechts hide-for-small hide-for-pad'},"a")
for i in pl_value2:
    indexv2 += 1
    if indexv2%2 == 0 and indexv2 != 2:
        array_values_prom.append(i.text)


# In[67]:


with open('premiere_league_transfer.csv', mode='w') as pl_file:
    pl_writer = csv.writer(pl_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    pl_writer.writerow(['Team', 'Total Value', 'Mean Value'])
    for i in range(len(array_team)):
    #print (array_team[i]+'|'+array_values[i]+'|'+array_values_prom[i])    
            pl_writer.writerow([array_team[i], array_values[i], array_values_prom[i]])

