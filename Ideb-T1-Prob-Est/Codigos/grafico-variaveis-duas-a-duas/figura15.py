import matplotlib.pyplot as plt
import csv

infos = {}  # Dicionário para guardar ano e IDEB das escolas publicas e privadas.

# Abrir o arquivo CSV.
with open('br_inep_ideb_brasil.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Iterar pelas linhas do CSV.
    for row in csv_reader:
        # Cria dict para IDEB do respectivo ano.
        if row[0] != "ano" and int(row[0]) not in infos:
            infos[int(row[0])] = {"publica": 0, "privada": 0}
        if row[1] == "publica":
            infos[int(row[0])]["publica"] = float(row[9])
        if row[1] == "privada":
            infos[int(row[0])]["privada"] = float(row[9])

# Ordenar as chaves (anos).
chaves_ordenadas = sorted(infos.keys())

# Cria listas para inserção dos valores no gráfico.
anos = []
ideb_privada = []
ideb_publica = []

# Carrega listas de inserção com valores do dicionário infos.
for i in range(len(chaves_ordenadas)):
    anos.append(chaves_ordenadas[i])
    ideb_privada.append(infos[chaves_ordenadas[i]]["privada"])
    ideb_publica.append(infos[chaves_ordenadas[i]]["publica"])

# Criar o gráfico
plt.figure(figsize=(6.5, 4))  # Ajustar o tamanho do gráfico.

# Adicionar as séries de dados
plt.plot(anos, ideb_privada, marker='o', label='Privada', color='skyblue')
plt.plot(anos, ideb_publica, marker='s', label='Pública', color='green')

# Adicionar título e rótulos
plt.title("Comparação IDEB das redes públicas e privadas no Brasil", fontsize=14)
plt.xlabel('Ano', fontsize=10)
plt.ylabel('IDEB', fontsize=10)

# Definir os ticks do eixo X para todos os anos
plt.xticks(anos)

# Adicionar uma grade para facilitar a visualização
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionar legenda
plt.legend()

# Exibir o gráfico
plt.tight_layout()  # Ajustar o layout para evitar sobreposição.
plt.show()
