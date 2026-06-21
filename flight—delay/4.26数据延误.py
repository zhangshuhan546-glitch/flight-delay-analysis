import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd .read_csv("C:/Users/Peter/Desktop/excel/FixedDelayedFlights.csv")

print(df.head())
print(df.describe())
print(df.info())
print(df.shape)
#
print(df.isnull().sum())
missing_arrtime = df[df['ArrTime'].isnull()]
print(missing_arrtime.shape)
delay_cols = [
    'CarrierDelay',
    'WeatherDelay',
    'NASDelay',
    'SecurityDelay',
    'LateAircraftDelay',
]
df[delay_cols] = df[delay_cols].fillna(0)
# # print(df.isnull().sum())
#把到达时间缺失的行直接删除
df =df[df['ArrTime'].notna()]
df =df[df['ArrDelay'].notna()]

df['ActualElapsedTime'] = df['ActualElapsedTime'].fillna(df['ActualElapsedTime'].median())

df['TailNum'] = df['TailNum'].fillna('Unknown')

df['CRSElapsedTime'] = df['CRSElapsedTime'].fillna(df['CRSElapsedTime'].median())

df['TaxiIn'] = df['TaxiIn'].fillna(df['TaxiIn'].median())
df['TaxiOut'] = df['TaxiOut'].fillna(df['TaxiOut'].median())
print(df.isnull().sum())
#延误高发机场，延误次数
delay_count = df[df['DepDelay']>15].groupby('Origin').size()
result= delay_count.sort_values(ascending=False).head(5)
print(result)
print(len(df))
#可视化
df[df['ArrDelay']<=200]['ArrDelay'].hist(bins=20)
plt.title('Arrival Delay Distribution')
plt.xlabel('Delay(minutes)')
plt.ylabel('Frequency')
plt.show()
#
df[df['ArrDelay']>=200]['ArrDelay'].hist(bins=50)
plt.title('Arrival Delay Distribution')
plt.xlabel('Delay(minutes)')
plt.ylabel('Frequency')
plt.show()
#
df[df['ArrDelay']>=500]['ArrDelay'].hist(bins=50)
plt.title('Arrival Delay Distribution')
plt.xlabel('Delay(minutes)')
plt.ylabel('Frequency')
plt.show()

plt.scatter(df['DepDelay'], df['ArrDelay'],alpha=0.5)
plt.xlabel('Departure Delay')
plt.ylabel('Arrival Delay')
plt.title('DeepDelay vs Arrival Delay')
plt.show()
#
df_sum = df[delay_cols].sum().sort_values()
df_sum.plot(kind='bar')
plt.xticks(rotation=0)
plt.title('Total Delay by Cause')
plt.show()

df.to_csv("C:/Users/Peter/Desktop/FixedDelayedFlights.csv",index=False)