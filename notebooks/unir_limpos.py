import pandas as pd
import glob
import os

pasta = "C:/Users/toravi21/Desktop/ciencia de dados final/dados/limpo"

arquivos = glob.glob(os.path.join(pasta, "*.csv"))

lista_dfs = [pd.read_csv(a, sep=";", encoding="utf-8", low_memory=False) for a in arquivos]

df_final = pd.concat(lista_dfs, ignore_index=True)


df_final.to_csv(
    os.path.join(pasta, "enem_completo.csv"),
    encoding="utf-8",
    sep=";",
    index=False
)