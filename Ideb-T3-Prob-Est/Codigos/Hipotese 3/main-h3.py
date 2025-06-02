import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("br_inep_ideb_brasil.csv")

# Filtrar os dados para obter as médias do IDEB ao longo dos anos para a rede "total"
df_ideb_total = df[df['rede'] == 'total'][['ano', 'ideb']]

# Remover valores nulos
df_ideb_total.dropna(subset=['ideb'], inplace=True)

# Adicionar uma constante para o modelo de regressão (intercepto)
X = sm.add_constant(df_ideb_total['ano'])

# Definir a variável dependente (IDEB)
y = df_ideb_total['ideb']

# Ajustar o modelo de regressão linear
modelo = sm.OLS(y, X).fit()

# Exibir o resumo do modelo
print(modelo.summary())

# Visualizar a relação entre ano e IDEB
plt.figure(figsize=(8, 6))
plt.scatter(df_ideb_total['ano'], df_ideb_total['ideb'], color='blue', label='Dados Observados')
plt.plot(df_ideb_total['ano'], modelo.fittedvalues, color='red', label='Regressão Linear')
plt.xlabel('Ano')
plt.ylabel('Ideb')
plt.title('Relação entre o Ideb total e os anos')
plt.legend()
plt.show()

# Teste da hipótese
# H₀: β = 0 (não há tendência significativa)
# H₁: β ≠ 0 (há uma tendência significativa)
# O valor-p do coeficiente 'ano' será comparado com o nível de significância (alpha)

valor_p = modelo.pvalues['ano']
alpha = 0.05

# Decisão
if valor_p < alpha:
    print(f"Rejeita-se a hipótese nula (H₀): o Ideb apresenta uma tendência significativa de crescimento.")
else:
    print(f"Não rejeita-se a hipótese nula (H₀): o Ideb não apresenta uma tendência significativa de crescimento.")
