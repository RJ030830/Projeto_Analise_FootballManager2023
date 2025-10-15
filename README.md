*Análise de Dados do Football Manager*

Visão Geral

Este projeto realiza a ingestão, limpeza e análise exploratória de um dataset do Football Manager, contendo atributos de jogadores (habilidades, posições, valor de mercado). O objetivo é transformar dados brutos em um dataset estruturado para análise de desempenho por posição, utilizando pipelines de ETL (Extract, Transform, Load).

Scripts:





coleta_dados.py: Pré-processamento e padronização da coluna de posições.



Preparação_dados_players.py: Transformação de dados, análise estatística e geração de datasets limpos.

Dataset

O dataset (merge_pl.csv) contém atributos de jogadores, como habilidades técnicas, físicas e valores de mercado. Ele é processado para análises baseadas em posições principais.

Descrição dos Scripts

1. coleta_dados.py

Realiza a ingestão de dados e pré-processamento para padronizar posições.

Etapas:





Ingestão: Carrega o dataset com pandas.



Limpeza: Substitui valores nulos por 0.



Feature Engineering: Cria a coluna Position_Main, extraindo a posição principal, removendo posições secundárias (split por ,) e especificações (split por ( e /).



Padronização: Converte posições para maiúsculas.



Saída: Gera dataset_players.csv.

2. Preparação_dados_players.py

Executa transformação de dados, análise estatística e feature engineering avançada.

Etapas:





Ingestão: Carrega dataset_players.csv.



Análise por Posição: Calcula médias, medianas e desvios padrão de habilidades específicas por posição (ex.: goleiros, atacantes). Salva estatísticas em CSVs (ex.: habilidades_GK_mean.csv).



Limpeza de Dados:





Converte valores de mercado ($10M, $500K) para numéricos, tratando nulos.



Converte alturas (pés/polegadas para cm) com regex.



Converte pesos (remove kg, converte para numérico).



Seleção e Renomeação: Seleciona colunas relevantes e renomeia atributos para maior clareza (ex.: Han → Handling).



Saída: Gera players_tratados.csv com dados limpos e estruturados.

Como Usar

Pré-requisitos





Python 3.x



Bibliotecas: pandas, numpy

pip install pandas numpy



Dataset: merge_pl.csv

Execução





Pré-processamento:

python coleta_dados.py

Gera dataset_players.csv.



Transformação e Análise:

python Preparação_dados_players.py

Gera players_tratados.csv e CSVs de estatísticas por posição.

Saídas


dataset_players.csv: Dados com posições padronizadas.

habilidades_[POSIÇÃO]_mean.csv: Estatísticas de habilidades por posição.

players_tratados.csv: Dataset final limpo e estruturado.
