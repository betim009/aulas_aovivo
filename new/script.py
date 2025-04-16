import requests
import pandas as pd

end_point = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
response = requests.get(end_point)

if response.status_code == 200:
    data = response.json()
    data_frame = pd.DataFrame(data)
    data_frame.to_csv("ibge.csv")
    