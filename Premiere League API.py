#!/usr/bin/env python
# coding: utf-8

# In[2]:


import http.client
import json
import csv
connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'b030eb58f80244309e009201e3e79dec' }
connection.request('GET', '/v2/competitions/PL/scorers?season=2019', None, headers )
response = json.loads(connection.getresponse().read().decode())
with open('premiere_league.csv', mode='w') as pl_file:
    pl_writer = csv.writer(pl_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    pl_writer.writerow(['name', 'nationality', 'numberOfGoals'])
    for player in response['scorers']:
        pl_writer.writerow([player['player']['name'], player['player']['nationality'], player['numberOfGoals']])


# In[ ]:




