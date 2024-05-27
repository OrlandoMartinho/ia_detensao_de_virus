import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib


dataset_path = 'data/dataset_pish.csv'
df = pd.read_csv(dataset_path)


df = df.drop(columns=['Domain'])


df = pd.get_dummies(df, columns=['Domain_End'])


features = df.drop(columns=['Label'])
labels = df['Label']




modelo_pish = 'AI_models/modelo_pish.pkl'
model = joblib.load(modelo_pish)


def fazer_previsoes(modelo, novos_dados):
   
    df_novos_dados = pd.DataFrame(novos_dados)
    
   
    df_novos_dados = df_novos_dados[features.columns]
    

    previsoes = modelo.predict(df_novos_dados)

    return previsoes


novos_dados = [
    {'Have_IP': 0, 'Have_At': 0, 'URL_Length': 1, 'URL_Depth': 1, 'Redirection': 0, 'https_Domain': 0, 'TinyURL': 0, 'Prefix/Suffix': 0, 'DNS_Record': 0, 'Web_Traffic': 1, 'Domain_Age': 1, 'Domain_End_0': 1, 'Domain_End_1': 0, 'iFrame': 0, 'Mouse_Over': 0, 'Right_Click': 0, 'Web_Forwards': 0},
    {'Have_IP': 1, 'Have_At': 0, 'URL_Length': 0, 'URL_Depth': 1, 'Redirection': 1, 'https_Domain': 0, 'TinyURL': 0, 'Prefix/Suffix': 1, 'DNS_Record': 0, 'Web_Traffic': 0, 'Domain_Age': 0, 'Domain_End_0': 0, 'Domain_End_1': 1, 'iFrame': 0, 'Mouse_Over': 0, 'Right_Click': 0, 'Web_Forwards': 0},
  
]

previsoes = fazer_previsoes(model, novos_dados)
for i, previsao in enumerate(previsoes, start=1):
    if previsao == 1:
        print(f"Dado {i}: O modelo prevê que é phishing.")
    else:
        print(f"Dado {i}: O modelo prevê que não é phishing.")
