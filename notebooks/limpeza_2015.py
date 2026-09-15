import pandas as pd

colunas = [
    "NU_ANO",
    "CO_MUNICIPIO_ESC",
    "NO_MUNICIPIO_ESC",
    "CO_UF_ESC",
    "SG_UF_ESC",
    "TP_DEPENDENCIA_ADM_ESC",
    "NU_NOTA_CN",
    "NU_NOTA_CH",
    "NU_NOTA_LC",
    "NU_NOTA_MT",
    "NU_NOTA_REDACAO",
    "Q006"
]

df = pd.read_csv(
    "C:/Users/toravi21/Desktop/ciencia de dados final/dados/bruto/MICRODADOS_ENEM_2015.csv",
    encoding="latin1",
    sep=";",
    low_memory=False,
    usecols=colunas
)

nomes = {
    "NU_ANO": "ANO",
    "CO_MUNICIPIO_ESC": "COD_MUNICIPIO",
    "NO_MUNICIPIO_ESC": "MUNICIPIO",
    "CO_UF_ESC": "COD_UF",
    "SG_UF_ESC": "UF",
    "TP_DEPENDENCIA_ADM_ESC": "DEPENDENCIA_ADM",
    "NU_NOTA_CN": "NOTA_CIENCIAS_NATUREZA",
    "NU_NOTA_CH": "NOTA_CIENCIAS_HUMANAS",
    "NU_NOTA_LC": "NOTA_LINGUAGENS",
    "NU_NOTA_MT": "NOTA_MATEMATICA",
    "NU_NOTA_REDACAO": "NOTA_REDACAO",
    "Q006": "RENDA",
}

df = df.rename(columns=nomes)

df.to_csv(
    "C:/Users/toravi21/Desktop/ciencia de dados final/dados/limpo/2015_selecionado.csv",
    encoding="utf-8",
    sep=";",
    index=False
)