# Análise de Dados do Football Manager

## Visão Geral
Este projeto realiza o processamento e análise de um conjunto de dados do Football Manager, contendo informações detalhadas sobre jogadores de futebol, incluindo suas habilidades, posições e valores de mercado. O objetivo é limpar, transformar e analisar os dados para extrair insights significativos sobre as habilidades dos jogadores com base em suas posições principais.

O repositório contém dois scripts Python principais:
- `coleta_dados.py`: Responsável pela importação inicial e pré-processamento dos dados, com foco na limpeza e padronização da coluna de posições.
- `Preparação_dados_players.py`: Realiza limpeza avançada, transformação e análise estatística das habilidades dos jogadores por posição, gerando conjuntos de dados limpos e estatísticas resumidas.

## Conjunto de Dados
O conjunto de dados utilizado neste projeto é proveniente de um dataset do Football Manager (por exemplo, `merge_pl.csv`). Ele contém atributos dos jogadores, como habilidades, características físicas, valor de mercado, entre outros. Os scripts assumem que o dataset está disponível localmente ou pode ser baixado (por exemplo, via Kaggle).

## Descrição dos Scripts

### 1. `coleta_dados.py`
Este script é responsável pela importação inicial e pré-processamento dos dados, com foco na limpeza e padronização da coluna `Position` para criar uma coluna simplificada `Position_Main`, facilitando a análise.

**Etapas Realizadas:**
- **Importação de Dados**: Carrega o dataset (`merge_pl.csv`) usando pandas e configura opções de exibição para melhor visualização.
- **Tratamento de Valores Nulos**: Substitui valores ausentes por `0` para garantir consistência nos dados.
- **Limpeza da Coluna de Posições**:
  - Extrai valores únicos da coluna `Position` para inspeção.
  - Cria uma nova coluna, `Position_Main`, extraindo a posição principal da coluna `Position`.
  - Remove posições secundárias separando por vírgulas (`,`).
  - Remove especificações de função (por exemplo, texto entre parênteses como `(Apoio)`) e especificações de lado (por exemplo, `/E` ou `/D`) usando divisão de strings.
  - Padroniza a coluna `Position_Main` convertendo todos os valores para maiúsculas.
- **Saída**: Salva o dataset processado em `dataset_players.csv` para uso no próximo script.

**Exemplo de Saída**:
- O script imprime posições únicas, as primeiras linhas do dataset e resultados intermediários para verificar o processo de limpeza.
- O arquivo `dataset_players.csv` resultante contém uma coluna `Position_Main` limpa com nomes de posições padronizados (por exemplo, `GK`, `D`, `M`).

### 2. `Preparação_dados_players.py`
Este script realiza limpeza avançada, transformação e análise estatística das habilidades dos jogadores com base em suas posições principais. Também prepara um dataset final limpo para análises futuras.

**Etapas Realizadas:**
- **Importação de Dados**: Carrega o dataset pré-processado (`dataset_players.csv`) do script anterior.
- **Análise de Habilidades por Posição**:
  - Define habilidades-chave para cada posição (por exemplo, `gk_skills` para goleiros, `st_skills` para atacantes).
  - Analisa as habilidades de cada posição, calculando média, mediana e desvio padrão dos atributos relevantes.
  - Salva as estatísticas de média das habilidades para cada posição em arquivos CSV separados (por exemplo, `habilidades_GK_mean.csv`).
- **Limpeza do Valor de Mercado**:
  - Limpa a coluna `Transfer Value`, convertendo valores como `$10M` ou `$500K` para formato numérico (em dólares) e tratando valores ausentes ou inválidos.
  - Cria uma nova coluna `Transfer_Value` com valores limpos, substituindo valores ausentes por `0`.
- **Processamento de Altura e Peso**:
  - Converte alturas de pés e polegadas (por exemplo, `6'2"`) para centímetros usando extração por regex e fórmulas de conversão.
  - Limpa a coluna `Weight`, removendo a unidade `kg` e convertendo para valores numéricos.
- **Seleção e Renomeação de Colunas**:
  - Seleciona colunas relevantes, incluindo identificadores dos jogadores, atributos e todas as habilidades únicas por posição.
  - Renomeia colunas para maior clareza e consistência (por exemplo, `Position_Main` para `Position_main`, `Han` para `Handling`).
- **Saída**: Salva o dataset totalmente processado em `players_tratados.csv` com colunas limpas e renomeadas.

**Exemplo de Saída**:
- Imprime posições únicas, estatísticas de habilidades (média, mediana, desvio padrão) para cada posição e uma prévia do dataset final limpo.
- Gera arquivos CSV específicos por posição com estatísticas de média das habilidades.
- Produz `players_tratados.csv`, um dataset abrangente pronto para análises adicionais.

## Como Usar
Para executar os scripts, certifique-se de ter as dependências necessárias instaladas e o dataset de entrada (`merge_pl.csv`) disponível no diretório de trabalho.

### Pré-requisitos
- Python 3.x
- Bibliotecas necessárias:
  ```bash
  pip install pandas numpy
  ```
- Dataset de entrada: `merge_pl.csv` (ou ajuste o script para apontar para o local do seu dataset).

### Executando os Scripts
1. **Executar `coleta_dados.py`**:
   ```bash
   python coleta_dados.py
   ```
   Isso gera o arquivo `dataset_players.csv` com posições padronizadas.

2. **Executar `Preparação_dados_players.py`**:
   ```bash
   python Preparação_dados_players.py
   ```
   Isso gera:
   - Arquivos CSV com estatísticas de habilidades por posição (por exemplo, `habilidades_GK_mean.csv`).
   - O dataset final limpo, `players_tratados.csv`.

### Arquivos de Saída
- `dataset_players.csv`: Dataset com posições limpas e padronizadas.
- `habilidades_[POSIÇÃO]_mean.csv`: Estatísticas de média das habilidades para cada posição (por exemplo, `GK`, `D`, `ST`).
- `players_tratados.csv`: Dataset final limpo e transformado com colunas renomeadas e atributos processados.

## Observações
- Os scripts assumem que o dataset possui colunas específicas (por exemplo, `Position`, `Transfer Value`, `Height`, `Weight`). Ajuste o código se o seu dataset tiver nomes ou estruturas de colunas diferentes.
- O código comentado de download do dataset do Kaggle em `coleta_dados.py` pode ser descomentado e modificado para baixar o dataset diretamente, se necessário.
- Os scripts incluem comandos de impressão para depuração e verificação. Você pode modificá-los ou removê-los para uso em produção.
