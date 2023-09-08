import pandas as pd
import requests
from io import StringIO

url= "https://zenodo.org/record/4670969/files/terremotos_centro_sur_america.csv"

response = requests.get(url)

if response.status_code == 200:
    
    df = pd.read_csv(StringIO(response.text))
    
    df.to_csv('dataset_2076326.csv', index=False)  
    
    print("El conjunto de datos se ha descargado '")
else:
    print("Error")

    