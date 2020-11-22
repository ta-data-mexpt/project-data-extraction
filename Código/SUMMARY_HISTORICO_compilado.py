import glob
import pandas as pd

all_data = pd.DataFrame() 

segundo = []
for f in glob.glob("/Users/user/Documents/IRONHACK/PROYECTO_2/HISTORICOS/*.csv"): 
       primero = pd.read_csv(f) 
      
       segundo.append(primero) 
all_data = pd.concat(segundo, ignore_index=True)

all_data.to_csv("/Users/user/Documents/IRONHACK/PROYECTO_2/SUMMARY_HISTORICO/recoleccion1.csv",index=False)