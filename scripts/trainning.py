import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from sklearn.model_selection import train_test_split


dataset_path = 'data/dataset_pish.csv'  
df = pd.read_csv(dataset_path)


df = df.drop(columns=['Domain'])


df = pd.get_dummies(df, columns=['Domain_End'])


features = df.drop(columns=['Label'])
labels = df['Label']


X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


joblib.dump(model, 'modelo_pish.pkl')


y_pred = model.predict(X_test)


precisao = accuracy_score(y_test, y_pred)
print(f"Precisão do modelo nos dados de teste: {precisao}")
