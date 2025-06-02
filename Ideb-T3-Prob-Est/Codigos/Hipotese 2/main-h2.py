import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Carregar o banco de dados (aqui assumimos que o arquivo é CSV)
df = pd.read_csv("br_inep_ideb_brasil.csv")

# Filtrar os dados para a rede pública e privada
# Aqui vamos considerar que a coluna 'rede' tem os valores 'publica' e 'privada'
rede_publica = df[df['rede'] == 'publica']
rede_privada = df[df['rede'] == 'privada']

# Contar o número de escolas com nota acima de 250 no SAEB de Matemática
# Vamos considerar a coluna 'nota_saeb_matematica'
nota_limite = 250

# Proporções de escolas com nota acima de 250 para cada rede
publicas_acima_250 = rede_publica[rede_publica['nota_saeb_matematica'] > nota_limite]
privadas_acima_250 = rede_privada[rede_privada['nota_saeb_matematica'] > nota_limite]

p_publica = len(publicas_acima_250) / len(rede_publica)
p_privada = len(privadas_acima_250) / len(rede_privada)

# Número de escolas nas duas redes
n_publica = len(rede_publica)
n_privada = len(rede_privada)

# Calcular o erro padrão
SE = ( (p_publica * (1 - p_publica)) / n_publica + (p_privada * (1 - p_privada)) / n_privada ) ** 0.5

# Calcular a estatística de teste z
z = (p_publica - p_privada) / SE

# Determinar o valor-p usando a distribuição normal padrão (teste bilateral)
p_value = 2 * (1 - stats.norm.cdf(abs(z)))

# Imprimir resultados
print(f"Número de escolas públicas: {n_publica}")
print(f"Número de escolas privadas: {n_privada}")
print(f"Número de escolas públicas com nota acima de 250: {len(publicas_acima_250)}")
print(f"Número de escolas privadas com nota acima de 250: {len(privadas_acima_250)}")
print(f"Proporção de escolas públicas com nota acima de 250: {p_publica:.4f}")
print(f"Proporção de escolas privadas com nota acima de 250: {p_privada:.4f}")
print(f"Valor z: {z:.4f}")
print(f"Valor p: {p_value:.4f}")

# Decisão
alpha = 0.05
if p_value < alpha:
    print("Rejeita-se a hipótese nula (H₀): as proporções são significativamente diferentes.")
else:
    print("Não se rejeita a hipótese nula (H₀): as proporções não são significativamente diferentes.")

# Visualização - Gráfico de barras das proporções em porcentagem
redes = ['Pública', 'Privada']
proporcoes = [p_publica * 100, p_privada * 100]  # Multiplicando por 100 para exibir em porcentagem

# Plotando o gráfico de barras com as barras mais finas (largura ajustada com o parâmetro width)
plt.figure(figsize=(8, 6))
plt.bar(redes, proporcoes, color=['blue', 'orange'])  # width ajustado para barras mais finas

# Ajustando o limite do eixo y para que as barras fiquem menos altas
plt.ylim(0, 100)  # Limite superior do eixo y ajustado para 100%

# Rótulos e título
plt.ylabel('Proporção de escolas com nota > 250 (%)')
plt.title('Proporção de escolas com nota SAEB em Matemática acima de 250')

# Adicionando valores no topo das barras
for i in range(len(proporcoes)):
    plt.text(i, proporcoes[i] + 1, f'{proporcoes[i]:.2f}%', ha='center', va='bottom', fontsize=12)

# Exibir o gráfico
plt.show()
