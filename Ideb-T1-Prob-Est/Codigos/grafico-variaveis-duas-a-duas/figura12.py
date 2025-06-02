import matplotlib.pyplot as plt
import csv

infos = {}  # Dicionário para guardar ano e seu respectivo IDEB.

# Abrir o arquivo CSV.
with open(r'C:\Users\jessi\OneDrive\Área de Trabalho\24-2\Ideb-T1-Prob-Est\br_inep_ideb_brasil.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Iterar pelas linhas do CSV.
    for row in csv_reader:
        # Cria dict para notas do respectivo ano.
        if row[0] != "ano" and int(row[0]) not in infos:
            infos[int(row[0])] = {}
        # Carregar dicionario dos respectivos anos com IDEB de ensino (fundamental 1, fundamental 2 e medio).
        if row[1] == "total" and row[2] == "medio":
            infos[int(row[0])]["medio"] = float(row[9])
        if row[1] == "total" and row[2] == "fundamental" and row[3] == "finais (6-9)":
            infos[int(row[0])]["fundamental_2"] = float(row[9])
        if row[1] == "total" and row[2] == "fundamental" and row[3] == "iniciais (1-5)":
            infos[int(row[0])]["fundamental_1"] = float(row[9])

    # Ordenar as chaves (anos).
    chaves_ordenadas = sorted(infos.keys())
    
    # Cria listas para inserção dos valores no gráfico.
    anos = []
    ideb_ensino_medio = []
    ideb_ensino_fund_2 = []
    ideb_ensino_fund_1 = []

    # Carrega listas de inserção com valores do dicionário infos.
    for i in range(len(chaves_ordenadas)):
        anos.append(chaves_ordenadas[i])
        ideb_ensino_medio.append(infos[chaves_ordenadas[i]]["medio"])
        ideb_ensino_fund_2.append(infos[chaves_ordenadas[i]]["fundamental_2"])
        ideb_ensino_fund_1.append(infos[chaves_ordenadas[i]]["fundamental_1"])

# Criar o gráfico
plt.figure(figsize=(8, 5))  # Ajustar o tamanho do gráfico.

# Adicionar as três séries de dados (Ensino Médio, Fundamental 1 e Fundamental 2)
plt.plot(anos, ideb_ensino_medio, label='Ensino Médio', marker='o', color='skyblue')
plt.plot(anos, ideb_ensino_fund_2, label='Fundamental 2 (6º-9º ano)', marker='s', color='green')
plt.plot(anos, ideb_ensino_fund_1, label='Fundamental 1 (1º-5º ano)', marker='^', color='orange')

# Adicionar título e rótulos
plt.title('Evolução do IDEB no Brasil', fontsize=16)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('IDEB', fontsize=12)

# Exibir todos os anos no eixo X
plt.xticks(anos)

# Adicionar uma grade para facilitar a visualização
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionar legenda
plt.legend()

# Exibir o gráfico
plt.tight_layout()  # Ajustar o layout para evitar sobreposição.
plt.show()
