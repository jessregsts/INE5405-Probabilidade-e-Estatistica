import pandas as pd

base = pd.read_csv(r'C:\Users\jessi\Downloads\br_inep_ideb_brasil_semtotal - br_inep_ideb_brasil.csv.csv')
base = base[base['rede'] != 'total']
temp = base.select_dtypes(include='number')  # Mantém apenas colunas numéricas

# Calculando a mediana
mediana = temp.median()
print(mediana)
print()

# Calculando a amplitude de todas as colunas numéricas
amplitude = temp.max() - temp.min()
print(amplitude)
#o decribe calcula a media, quartis, e desvio padrao direto
print(base.describe())