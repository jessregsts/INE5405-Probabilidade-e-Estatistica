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
            infos[int(row[0])] = {"fundamental": 0, "medio": 0}
        if row[1] == "publica" and row[2] == "fundamental":
            infos[int(row[0])]["fundamental"] += round(float(row[5]), 2) * 100 / 2
        if row[1] == "publica" and row[2] == "medio":
            infos[int(row[0])]["medio"] += round(float(row[5]), 2) * 100

# Ordenar as chaves (anos).
chaves_ordenadas = sorted(infos.keys())

# Cria listas para inserção dos valores no gráfico.
anos = []
rendimento_medio = []
rendimento_fundamental = []

# Carrega listas de inserção com valores do dicionário infos.
for i in range(len(chaves_ordenadas)):
    anos.append(chaves_ordenadas[i])
    rendimento_medio.append(infos[chaves_ordenadas[i]]["medio"])
    rendimento_fundamental.append(infos[chaves_ordenadas[i]]["fundamental"])

# Criar o gráfico
plt.figure(figsize=(6.5, 4))  # Ajustar o tamanho do gráfico.

# Adicionar as séries de dados
plt.plot(anos, rendimento_medio, marker='o', label='Ensino Médio', color='orange')
plt.plot(anos, rendimento_fundamental, marker='s', label='Ensino Fundamental', color='green')

# Adicionar título e rótulos
plt.title("Comparação do Índice de Rendimento dos ensinos na rede pública do Brasil", fontsize=10)
plt.xlabel('Ano', fontsize=10)
plt.ylabel('Índice Rendimento (%)', fontsize=10)

# Definir os ticks do eixo X para todos os anos
plt.xticks(anos)

# Adicionar uma grade para facilitar a visualização
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionar legenda
plt.legend()

# Exibir o gráfico
plt.tight_layout()  # Ajustar o layout para evitar sobreposição.
plt.show()
