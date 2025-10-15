import pandas as pd
# import kagglehub

# IMPORTAÇÃO DE DADOS DO KAGGLEHUB
# # Download latest version
# path = kagglehub.dataset_download("siddhrajthakor/football-manager-2023-dataset")

# print("Path to dataset files:", path)

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('merge_pl.csv')
print(df.head())
df = df.fillna(0)

# após importação de dados e filtro de nulos, vamos coletar as estatísticas de todos os jogadores
# separar valores únicos
print("Valores Únicos do campo Position")
print(df['Position'].unique()[:10])
print('\nPrimeiras Linhas em position:')
print(df[['Name','Position']].head(10))
# Notei que as posições secundárias e especificações iriam dificultar o agrupamento de jogadores
# por isso decidi criar uma nova coluna para a posição principal de cada jogador
df['Position_Main'] = df['Position']
# Para a separação da posição principal, decidi usar o método str.split
df['Position_Main'] = df['Position_Main'].str.split(',').str[0]
print('Verificação de remoção de posições secundárias:\n', df['Position_Main'].head(10))
# Após o tratamento de posições secundárias, vamos fazer o tratamento de especificação de função
df['Position_Main'] = df['Position_Main'].str.split(' \(').str[0]
df['Position_Main'] = df['Position_Main'].str.split('/').str[0]
print('Verificação de Remoção de Especificação de função:\n', df['Position_Main'].unique())
# Padronização
df['Position_Main'] = df['Position_Main'].str.upper()
df.to_csv("dataset_players.csv", index=False)