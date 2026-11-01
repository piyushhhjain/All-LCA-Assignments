import pandas as pd
df = pd.read_csv('Iris.csv')
df
df.head()
df.tail()
df.info()
df.describe()
df.dropna()
df.fillna(value = 'Missing')
df[df.duplicated(keep= False)]
df.duplicated().sum()
df = df.drop_duplicates()
