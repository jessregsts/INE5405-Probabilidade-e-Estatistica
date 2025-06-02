import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Leitura dos dados
dados = pd.read_csv("br_inep_ideb_brasil.csv")

# Exibe as primeiras linhas para verificar como os dados foram lidos
print(dados.head())

# Filtrando os dados para as redes pública e privada
dados_publica = dados[dados['rede'] == 'publica']
dados_privada = dados[dados['rede'] == 'privada']

# Estatísticas descritivas
media_publica = dados_publica['ideb'].mean()
media_privada = dados_privada['ideb'].mean()
desvio_publica = dados_publica['ideb'].std()
desvio_privada = dados_privada['ideb'].std()

# Tamanhos das amostras
n_publica = len(dados_publica)
n_privada = len(dados_privada)

print("Estatísticas Descritivas:")
print(f"Média IDEB Pública: {media_publica:.2f}, Desvio Padrão: {desvio_publica:.2f}, Tamanho da amostra: {n_publica}")
print(f"Média IDEB Privada: {media_privada:.2f}, Desvio Padrão: {desvio_privada:.2f}, Tamanho da amostra: {n_privada}")

# Intervalos de confiança para 95% de confiança
ic_publica = stats.norm.interval(
    alpha=0.95,
    loc=media_publica,
    scale=desvio_publica / (n_publica**0.5)
)
ic_privada = stats.norm.interval(
    alpha=0.95,
    loc=media_privada,
    scale=desvio_privada / (n_privada**0.5)
)

print("\nIntervalos de Confiança (95%):")
print(f"Rede Pública: {ic_publica[0]:.2f} a {ic_publica[1]:.2f}")
print(f"Rede Privada: {ic_privada[0]:.2f} a {ic_privada[1]:.2f}")

# Verificar normalidade (Shapiro-Wilk)
shapiro_publica = stats.shapiro(dados_publica['ideb'])
shapiro_privada = stats.shapiro(dados_privada['ideb'])

print("\nTeste de Normalidade:")
print(f"Rede Pública: W={shapiro_publica.statistic:.4f}, p={shapiro_publica.pvalue:.4f}")
print(f"Rede Privada: W={shapiro_privada.statistic:.4f}, p={shapiro_privada.pvalue:.4f}")

# Verificar homogeneidade de variâncias (Levene)
levene_test = stats.levene(dados_publica['ideb'], dados_privada['ideb'])

print("\nTeste de Homogeneidade de Variâncias:")
print(f"Levene: F={levene_test.statistic:.4f}, p={levene_test.pvalue:.4f}")

# Teste t para diferença de médias
t_test = stats.ttest_ind(dados_publica['ideb'], dados_privada['ideb'], equal_var=True)

print("\nTeste t de Student:")
print(f"T-statistic={t_test.statistic:.4f}, p-value={t_test.pvalue:.4f}")

# Visualização das distribuições
sns.boxplot(data=[dados_publica['ideb'], dados_privada['ideb']])
plt.xticks([0, 1], ['Rede Pública', 'Rede Privada'])
plt.ylabel('Média do IDEB')
plt.title('Distribuição do IDEB por Rede de Ensino')
plt.show()

# Criar o gráfico de curvas normais
x_range = np.linspace(min(dados['ideb']) - 1, max(dados['ideb']) + 1, 1000)

# Curva normal para a rede pública
pdf_publica = stats.norm.pdf(x_range, loc=media_publica, scale=desvio_publica)

# Curva normal para a rede privada
pdf_privada = stats.norm.pdf(x_range, loc=media_privada, scale=desvio_privada)

# Plotando as curvas
plt.plot(x_range, pdf_publica, label='Rede Pública', color='blue')
plt.plot(x_range, pdf_privada, label='Rede Privada', color='red')

# Adicionar título e legendas
plt.title('Curvas Normais para as Médias do IDEB (Rede Pública e Rede Privada)')
plt.xlabel('Média do IDEB')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)

# Mostrar o gráfico
plt.show()
