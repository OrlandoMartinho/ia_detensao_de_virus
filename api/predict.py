import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Carregar o conjunto de dados
dataset_path = 'data/dataset_pish.csv'
df = pd.read_csv(dataset_path)

# Remover a coluna 'Domain'
df = df.drop(columns=['Domain'])

# Converter colunas categóricas em numéricas
df = pd.get_dummies(df, columns=['Domain_End'])

# Separar características e rótulos
features = df.drop(columns=['Label'])
labels = df['Label']

# Carregar o modelo
modelo_pish = 'AI_models/modelo_pish.pkl'
model = joblib.load(modelo_pish)

# Função para fazer previsões
def fazer_previsoes(modelo, novos_dados):
    # Criar DataFrame com os novos dados
    df_novos_dados = pd.DataFrame([novos_dados])
    # Reordenar colunas para corresponder à ordem do modelo treinado
    df_novos_dados = df_novos_dados[features.columns]
    # Fazer previsões
    previsoes = modelo.predict(df_novos_dados)
    return previsoes

# Dados de teste
 # {'Have_IP': 0, 'Have_At': 0, 'URL_Length': 1, 'URL_Depth': 1, 'Redirection': 0, 'https_Domain': 0, 'TinyURL': 0, 'Prefix/Suffix': 0, 'DNS_Record': 0, 'Web_Traffic': 1, 'Domain_Age': 1, 'Domain_End_0': 1, 'Domain_End_1': 0, 'iFrame': 0, 'Mouse_Over': 0, 'Right_Click': 0, 'Web_Forwards': 0}

def prever(dados):

    previsoes = fazer_previsoes(model, dados)
    # Exibir resultado
    if previsoes == 1:
        return 1
    else:
        return 0
