import pandas as pd
import numpy as np

# Carregando o arquivo CSV
df = pd.read_csv(r'C:\Users\jessi\Downloads\br_inep_ideb_brasil_semtotal - br_inep_ideb_brasil.csv.csv')

# Função para gerar a tabela de frequência para variáveis qualitativas
def tabela_frequencia_categorica(coluna):
    frequencia_absoluta = df[coluna].value_counts()
    frequencia_relativa = df[coluna].value_counts(normalize=True) * 100
    tabela = pd.DataFrame({
        'Frequência Absoluta': frequencia_absoluta,
        'Frequência Relativa (%)': frequencia_relativa
    })
    tabela.loc['Total Geral'] = [frequencia_absoluta.sum(), frequencia_relativa.sum()]
    return tabela

# Tabelas de frequência para variáveis qualitativas
tabela_rede = tabela_frequencia_categorica('rede')
tabela_ensino = tabela_frequencia_categorica('ensino')
tabela_anos_escolares = tabela_frequencia_categorica('anos_escolares')

# Função para gerar tabela de frequência com intervalos de classe (quantitativas)
def tabela_frequencia_quantitativa(coluna):
    n = len(df[coluna].dropna())  # número de observações
    k = int(1 + 3.322 * np.log10(n))  # número de classes pela regra de Sturges
    intervalo_classes = pd.cut(df[coluna], bins=k)
    
    frequencia_absoluta = intervalo_classes.value_counts()
    frequencia_relativa = intervalo_classes.value_counts(normalize=True) * 100
    tabela = pd.DataFrame({
        'Intervalos de Classes': frequencia_absoluta.index,
        'Frequência Absoluta': frequencia_absoluta.values,
        'Frequência Relativa (%)': frequencia_relativa.values
    })
    tabela['Frequência Acumulada (%)'] = tabela['Frequência Relativa (%)'].cumsum()
    return tabela

# Tabelas de frequência para variáveis quantitativas
tabela_taxa_aprovacao = tabela_frequencia_quantitativa('taxa_aprovacao')
tabela_nota_saeb_matematica = tabela_frequencia_quantitativa('nota_saeb_matematica')
tabela_nota_saeb_portugues = tabela_frequencia_quantitativa('nota_saeb_lingua_portuguesa')
tabela_ideb = tabela_frequencia_quantitativa('ideb')

# Exibindo tabelas
print(tabela_rede)
print(tabela_ensino)
print(tabela_anos_escolares)

print(tabela_taxa_aprovacao)
print(tabela_nota_saeb_matematica)
print(tabela_nota_saeb_portugues)
print(tabela_ideb)
