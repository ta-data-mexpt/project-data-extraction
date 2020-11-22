import json
import requests
import time
import pandas as pd
import urllib.request
from pandas.io.json import json_normalize
from datetime import datetime

def summary_diario (path):
    paises = 'https://api.covid19api.com/summary'
    resultado = requests.get(paises)
    #resultado
    resultado_1 = resultado.json()
    resultado_1
    country = resultado_1['Countries']
    country
    df = pd.DataFrame(country).iloc[:,:-1]
    #df
    df.to_csv(path,index=False)
    return df

info_diario = summary_diario (f"/Users/user/Documents/IRONHACK/PROYECTO_2/DATACOVID_{datetime.today().isoformat()}.csv")

info_diario