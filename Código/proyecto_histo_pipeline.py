import json
import requests
import time
import pandas as pd
import urllib.request
from pandas.io.json import json_normalize
from datetime import datetime

def creacion_historico(links_completos, inicio, final):
    historico = []
    for item in list(links_completos.loc[inicio:final,'ligas']):
        pedido = requests.get(item)
        if len(pedido.json()) > 0:
            historico.append(pedido.json())  
    df = pd.DataFrame(historico)
    flat = pd.json_normalize(df[0])
    return flat   

def resumen (path, inicial, finalizacion):
    links_completos = pd.read_csv("/Users/user/Documents/IRONHACK/PROYECTO_2/LIGAS/ligas_historicos.csv")
    print('lectura archivo')
    
    flat = creacion_historico(links_completos, inicial, finalizacion)
    print('normalize a los archivos')
    
    flat.to_csv(path, index=False)
    return flat

archivo_historico = resumen("/Users/user/Documents/IRONHACK/PROYECTO_2/HISTORICOS/Historico21.csv",11000,12000)
archivo_historico