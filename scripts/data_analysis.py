import pandas as pd


df = pd.read_csv('data/dataset_pish.csv')

#print(df2.describe())
nan_counts = df.isna().sum()


print(nan_counts)