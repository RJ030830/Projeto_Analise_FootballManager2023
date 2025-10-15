import pandas as pd
import numpy as np
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('dataset_players.csv')
print('Posições Únicas:\n', df['Position_Main'].unique())

# Selecionei algumas habilidades importantes por posição, para filtrarmos os jogadores
gk_skills = ['Han', 'Kic', 'Pun', 'Thr', '1v1', 'Ref', 'Aer', 'Agi', 'Jum', 'Pac']
df_skills = ['Tck', 'Mar', 'Hea', 'Pas', 'Tec', '1v1', 'Str', 'Jum', 'Pac', 'Acc', 'Sta', 'Agi', 'Bal']
wb_skills = ['Cro', 'Tck', 'Pas', 'Tec', 'Dri', 'L Th', '1v1', 'Acc', 'Pac', 'Sta', 'Agi', 'Bal', 'Str', 'Nat.1']
dm_skills = ['Tck','Mar','Pas','Tec','Fir','Str','Sta','Acc','Pac','Agi','Bal','Nat.1']
mf_skills = ['Pas','Tec','Fir','Dri','Cro','Cor','Fre','Sta','Acc','Pac','Agi','Bal','Str','Nat.1']
am_skills = ['Dri','Fin','Pas','Tec','Fre','Cro','Fir','Lon','Acc','Pac','Agi','Sta','Bal']
st_skills = ['Fin','Dri','Fir','Hea','Tec','Pen','Acc','Pac','Agi','Str','Jum','Bal']


def analyze_skills_by_position(position, skills, position_name):
    # Filtrar jogadores da posição
    df_position = df[df['Position_Main'] == position]

    # Calcular estatísticas
    stats_mean = df_position[skills].mean().round(2)
    stats_median = df_position[skills].median().round(2)
    stats_std = df_position[skills].std().round(2)

    # Exibir resultados
    print(f"\nEstatísticas para {position_name} ({position}):")
    print("\nMédias:")
    print(stats_mean)
    print("\nMedianas:")
    print(stats_median)
    print("\nDesvio Padrão:")
    print(stats_std)

    # Salvar em CSV
    stats_mean.to_csv(f'habilidades_{position}_mean.csv')

    return df_position, stats_mean


# Passo 3: Analisar cada posição
positions = {
    'GK': ('Goleiros', gk_skills),
    'D': ('Zagueiros', df_skills),
    'WB': ('Laterais', wb_skills),
    'DM': ('Volantes', dm_skills),
    'M': ('Meio-campistas', mf_skills),
    'AM': ('Meio-campistas Ofensivos', am_skills),
    'ST': ('Atacantes', st_skills)
}

# Dicionário para armazenar resultados
results = {}
for pos, (name, skills) in positions.items():
    if pos in df['Position_Main'].values:
        df_pos, mean_stats = analyze_skills_by_position(pos, skills, name)
        results[pos] = {'df': df_pos, 'mean': mean_stats}
    else:
        print(f"\nPosição {pos} não encontrada no dataset.")

# Função para limpar coluna de valor de mercado
def clean_transfer_value(value):
    if pd.isna(value) or value == '-' or value == '0$':
        return 0
    try:
        value = value.replace('$', '').strip()
        if 'M' in value:
            return float(value.replace('M', '')) * 1_000_000
        elif 'K' in value:
            return float(value.replace('K', '')) * 1_000
        return float(value)
    except:
        return np.nan

df['Transfer_Value'] = df['Transfer Value'].apply(clean_transfer_value)
print(df['Transfer_Value'].unique())
df['Transfer_Value'] = df['Transfer_Value'].fillna(0)

# Tratamento dos campos Height e Weight
# Extrair pés e polegadas com regex e depois converter para cm
extracted = df['Height'].str.extract(r"(\d+)'(\d+)")
df['Height_cm'] = extracted[0].astype(float) * 30.48 + extracted[1].astype(float) * 2.54

df['Weight'] = df['Weight'].str.replace('kg', '').str.strip()
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')

# Seleção de colunas relevantes + união de todas as skills relevantes por posição
all_skills = list(set(gk_skills + df_skills + wb_skills + dm_skills + mf_skills + am_skills + st_skills))
columns_to_keep = [
    'UID', 'Name', 'Position_Main', 'Nat', 'Club', 'Based', 'Age', 'Height_cm', 'Weight', 'Transfer_Value',
    'Preferred Foot', 'Media Description', 'Rc Injury', 'Caps', 'AT Gls', 'AT Lge Gls'
] + all_skills

# Renomear Campos para facilitar análise
rename_dict = {
    'Position_Main': 'Position_main',
    'Transfer_Value': 'Market_Value',
    'Nat': 'Nationality',
    'Rc Injury': 'Injury_Risk',
    'AT Gls': 'Total_Goals',
    'AT Lge Gls': 'League_Goals',
    'Han': 'Handling',
    'Kic': 'Kicking',
    'Pun': 'Punching',
    'Thr': 'Throwing',
    '1v1': 'One_v_One',
    'Ref': 'Reflexes',
    'Aer': 'Aerial_Reach',
    'Agi': 'Agility',
    'Jum': 'Jumping_Reach',
    'Pac': 'Pace',
    'Tck': 'Tackling',
    'Mar': 'Marking',
    'Hea': 'Heading',
    'Pas': 'Passing',
    'Tec': 'Technique',
    'Str': 'Strength',
    'Acc': 'Acceleration',
    'Sta': 'Stamina',
    'Bal': 'Balance',
    'Cro': 'Crossing',
    'Dri': 'Dribbling',
    'L Th': 'Long_Throws',
    'Nat.1': 'Natural_Fitness',
    'Fir': 'First_Touch',
    'Cor': 'Corners',
    'Fre': 'Free_Kicks',
    'Fin': 'Finishing',
    'Lon': 'Long_Shots',
    'Pen': 'Penalty_Taking'
}

players_tratado = df.rename(columns=rename_dict)

# Salvar DataFrame tratado
players_tratado.to_csv('players_tratados.csv', index=False, encoding='utf-8')
print('Teste DF:\n',players_tratado.head())