import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns; sns.set_theme(color_codes=True)
from sklearn.linear_model import LinearRegression



df = pd.read_csv('samsung_phone.csv')
#print(df.head(10), '\n')
#print(df.info())

df['price'] = df['price'].str.replace('Rp', '', regex=True).str.replace('.', '', regex=True)
df['price'] = pd.to_numeric(df['price'], downcast='integer')

df[['x', 'n_sold']] = df['sold'].str.rsplit(n=1, expand=True)
df.drop(['x', 'sold'], axis=1, inplace=True)

df['n_sold'] = pd.to_numeric(df['n_sold'])
df['n_sold'] = df['n_sold'].astype('Int32')
df['n_sold'] = df['n_sold'].replace(np.NaN, 0)

df[['name', 'x']] = df['name'].str.rsplit('-', n=1, expand=True)
df.drop(['x'], axis=1, inplace=True)
df[['name', 'ram']] = df['name'].str.rsplit(n=1, expand=True)
df[['ram', 'rom']] = df['ram'].str.split('/', expand=True)
df.dropna(subset=['rom'], axis=0, inplace=True)

df['ram'] = df['ram'].str.extract('(\d+)').astype(int) #extract number only from column ram
df['rom'] = df['rom'].str.extract('(\d+)').astype(int)

df.reset_index(inplace=True, drop=True)

df.to_csv('clean_samsung.csv', index=False, encoding='utf-8')

print(df.head(10), '\n')
print(df.info())

data = pd.read_csv('clean_samsung.csv')

plt.figure('Correlation 1')
sns.regplot(x='ram', y='price', data=data, color='g') #positive correlation
plt.title('Correlation of ram vs price')
plt.xlabel('ram (GB)')
plt.ylabel('price (Rp)')
plt.ylim(0,)

plt.show()

#linear regression
x = data[['ram','rom']]
y = data['price']

model = LinearRegression()
model.fit(x,y)
prediction = model.predict([[6, 128]])
print(int(prediction)) #print prediction result