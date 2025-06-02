import matplotlib.pyplot as plt
import csv

infos = {}  # Dicionário para guardar ano e indicador redimento.

# Abrir o arquivo CSV.
with open('br_inep_ideb_brasil.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Iterar pelas linhas do CSV.
    for row in csv_reader:
        # Cria dict para indicador redimento do respectivo ano.
        if row[0] != "ano" and int(row[0]) not in infos:
            infos[int(row[0])] = {"estadual": 0, "municipal": 0}
        if row[1] == "estadual":
            infos[int(row[0])]["estadual"] += round(float(row[5]), 2) * 100 / 3
        if row[1] == "municipal":
            infos[int(row[0])]["municipal"] += round(float(row[5]), 2) * 100 / 3

# Ordenar as chaves (anos).
chaves_ordenadas = sorted(infos.keys())

# Cria listas para inserção dos valores no gráfico.
anos = []
rendimento_estadual = []
rendimento_municipal = []

# Carrega listas de inserção com valores do dicionário infos.
for i in range(len(chaves_ordenadas)):
    anos.append(chaves_ordenadas[i])
    rendimento_estadual.append(infos[chaves_ordenadas[i]]["estadual"])
    rendimento_municipal.append(infos[chaves_ordenadas[i]]["municipal"])

# Criar o gráfico
plt.figure(figsize=(6.5, 4))  # Ajustar o tamanho do gráfico.

# Adicionar as séries de dados
plt.plot(anos, rendimento_estadual, marker='o', label='Rede Estadual', color='skyblue')
plt.plot(anos, rendimento_municipal, marker='s', label='Rede Municipal', color='purple')

# Adicionar título e rótulos
plt.title("Comparação do Índice de Rendimento das redes públicas no Brasil", fontsize=10)
plt.xlabel('Ano', fontsize=10)
plt.ylabel('Índice Rendimento (%)', fontsize=10)

# Definir os ticks
plt.xticks(anos)
plt.yticks(range(30, 101, 10))

# Adicionar uma grade para facilitar a visualização
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionar legenda
plt.legend()

# Exibir o gráfico
plt.tight_layout()  # Ajustar o layout para evitar sobreposição.
plt.show()
