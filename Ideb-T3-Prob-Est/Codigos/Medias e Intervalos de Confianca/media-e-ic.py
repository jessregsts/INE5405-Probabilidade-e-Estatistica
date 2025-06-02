import pandas as pd
import numpy as np
from scipy.stats import t

# Função para calcular intervalo de confiança para a média
def confidence_interval_mean(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_err = np.std(data, ddof=1) / np.sqrt(n)  # Desvio padrão da amostra / raiz(n)
    t_value = t.ppf((1 + confidence) / 2, n - 1)  # Valor crítico t
    margin_error = t_value * std_err
    return mean, mean - margin_error, mean + margin_error

# Função principal
def analyze_csv(file_path):
    # Carregar dados
    data = pd.read_csv(file_path)
    
    # Selecionar colunas numéricas relevantes
    columns_to_analyze = ['taxa_aprovacao', 'nota_saeb_matematica', 'nota_saeb_lingua_portuguesa', 'ideb']
    
    # Calcular ICs para as médias
    results = {}
    for col in columns_to_analyze:
        if col in data:
            mean, lower, upper = confidence_interval_mean(data[col].dropna())
            results[col] = {'mean': mean, 'ci_lower': lower, 'ci_upper': upper}
    
    # Printar resultados
    for col, stats in results.items():
        print(f"{col}:")
        print(f"  Média: {stats['mean']:.2f}")
        print(f"  IC 95%: [{stats['ci_lower']:.2f}, {stats['ci_upper']:.2f}]")
        print()
        
# Caminho do arquivo CSV
file_path = r"c:\Users\jessi\OneDrive\Área de Trabalho\24-2\Trabalhos probestat\Ideb-T3-Prob-Est\br-inep-ideb-brasil-versao-sem-total.csv"

# Executar análise
analyze_csv(file_path)
