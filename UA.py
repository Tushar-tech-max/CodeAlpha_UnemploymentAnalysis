import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Unemployment in India.csv")

df.columns = df.columns.str.strip()

df = df.dropna()

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

print(df.info())
print(df.isnull().sum())

print(df['Estimated Unemployment Rate (%)'].describe())
print(df[ 'Estimated Labour Participation Rate (%)'].describe())

monthly = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(12,6))
plt.plot(monthly)
plt.title("Unemployment Rate Trend")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()


pre_covid = df[df['Date'] < '2020-03-01']
covid = df[df['Date'] >= '2020-03-01']

print(pre_covid['Estimated Unemployment Rate (%)'].mean())
print(covid['Estimated Unemployment Rate (%)'].mean())

state_unemployment = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()
print(state_unemployment.sort_values(ascending=False))

monthly_avg = df.groupby(df['Date'].dt.month)['Estimated Unemployment Rate (%)'].mean()
print(monthly_avg)

sns.boxplot(x='Area',
            y='Estimated Unemployment Rate (%)',
            data=df)
plt.show()