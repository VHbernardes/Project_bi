import pandas as pd

# Carregar os arquivos Excel
df1 = pd.read_excel('data/Exp_ranking_pais_part_mes.xlsx', header=5) 
df2 = pd.read_excel('data/Setores_Produtos.xlsx', header=6)
df3 = pd.read_excel('data/Tabela_Resumo.xlsx', header=11)

# Limpeza de Dados 1: Remover colunas com NaNs
df1_clean = df1.dropna(axis=1, how='all')

# Limpeza de Dados 2 e Dados 3: Ajustar a quantidade de NaNs permitidos
threshold = len(df2) * 0.5  # 50% NaNs permitidos
df2_clean = df2.dropna(axis=1, thresh=threshold)

threshold = len(df3) * 0.5  # 50% NaNs permitidos
df3_clean = df3.dropna(axis=1, thresh=threshold)

# Preencher NaNs em Dados 2 e Dados 3 com valores padrão
df2_clean = df2_clean.fillna({'Valor US$': 0, 'Toneladas': 0, 'Preço': 0})
df3_clean = df3_clean.fillna({'Período': 'Desconhecido', 'Dias Úteis': 0, 'EXPORTAÇÃO': 0})

# Exibir resultados
print("Dados 1 (Após Ajustes):")
print(df1_clean.head())

print("\nDados 2 (Após Ajustes):")
print(df2_clean.head())

print("\nDados 3 (Após Ajustes):")
print(df3_clean.head())


# Exibir as primeiras linhas de cada DataFrame para inspeção
print("Dados 1:")
print(df1.head())
print("\nDados 2:")
print(df2.head())
print("\nDados 3:")
print(df3.head())











