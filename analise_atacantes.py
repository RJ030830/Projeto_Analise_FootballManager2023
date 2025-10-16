import pandas as pd
# Opções de display
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
# arquivos carregados
df_players = pd.read_csv('players_tratados.csv')
df_medias_st = pd.read_csv('habilidades_ST_mean.csv', header=None, names=['skill', 'mean'])
# dicionário criado para facilitar uso das médias salvas
dict_medias = dict(zip(df_medias_st['skill'], df_medias_st['mean']))
# Sistema de filtro de jogador (modelo)
filtro_st_good_in_air = df_players[
    (df_players['Position_main'] == 'ST') &
    (df_players['Finishing'] >= dict_medias['Fin']) &
    (df_players['Height_cm'] >= 185.00) &
    (df_players['First_Touch'] >= dict_medias['Fir']) &
    (df_players['Heading'] >= dict_medias['Hea'])
]

print(f"Atacantes bons no jogo aéreo ({len(filtro_st_good_in_air)} encontrados):")
print(filtro_st_good_in_air[['Name', 'Club', 'Finishing', 'Dribbling', 'First_Touch', 'Heading', 'Height_cm']].head(10))
filtro_st_good_in_air.to_csv('st_good_in_air.csv', index=False)
