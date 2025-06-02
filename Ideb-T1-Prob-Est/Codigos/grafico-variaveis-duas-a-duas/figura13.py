import matplotlib.pyplot as plt
import csv

infos = {}  # Dicionário para guardar ano e média das notas do SAEB.

# Abrir o arquivo CSV.
with open('br_inep_ideb_brasil.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Iterar pelas linhas do CSV.
    for row in csv_reader:
        # Cria dict para notas do respectivo ano.
        if row[0] != "ano" and int(row[0]) not in infos:
            infos[int(row[0])] = {"matematica": 0, "portugues": 0}  # dict media saeb escolas privadas.
        if row[1] == "privada":
            infos[int(row[0])]["matematica"] += float(row[6]) / 3
            infos[int(row[0])]["portugues"] += float(row[7]) / 3

# Ordenar as chaves (anos).
chaves_ordenadas = sorted(infos.keys())

# Cria listas para inserção dos valores no gráfico.
anos = []
notas_saeb_mat = []
notas_saeb_port = []

# Carrega listas de inserção com valores do dicionário infos.
for ano in chaves_ordenadas:
    anos.append(ano)
    notas_saeb_mat.append(infos[ano]["matematica"])
    notas_saeb_port.append(infos[ano]["portugues"])

# Criar o gráfico de linhas
plt.figure(figsize=(6.5, 4))  # Ajustar o tamanho do gráfico.

# Adicionar as séries de dados com linhas
plt.plot(anos, notas_saeb_mat, label='Matemática', marker='o', color='skyblue')
plt.plot(anos, notas_saeb_port, label='Língua Portuguesa', marker='s', color='orange')

# Adicionar título e rótulos
plt.title("Evolução das notas do SAEB nas escolas privadas do Brasil", fontsize=14)
plt.xlabel('Ano', fontsize=10)
plt.ylabel('Média das notas SAEB', fontsize=10)

# Ajustar intervalos dos eixos
plt.xticks(range(min(anos), max(anos)+1, 2))  # Intervalo de 2 anos para o eixo X
plt.yticks(range(200, 351, 15))  

# Adicionar uma grade para facilitar a visualização
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionar legenda
plt.legend()

# Exibir o gráfico
plt.tight_layout()  # Ajustar o layout para evitar sobreposição.
plt.show()
