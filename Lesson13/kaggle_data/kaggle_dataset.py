import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')

print(df.info())

first_rows = df.head()
print(first_rows)

country_data = df['Country']
print(country_data)

subset = df[['Country', 'Average IQ']]
print(subset)

filtered_df = subset[subset['Average IQ'] > 100]
print(filtered_df)

null_mask = df.isnull()

null_count = null_mask.sum()
print("\nCount of null values in each column:")
print(null_count)

df.dropna(inplace=True)
print("\nDataset information after removing null values:")
print(df.info())

duplicated_count = df.duplicated().sum()
print("\nCount of duplicate rows:")
print(duplicated_count)

average_iq_per_continent = df.groupby('Continent')['Average IQ'].mean()
print(average_iq_per_continent)


df['Population - 2023'] = df['Population - 2023'].apply(lambda x: float(x.replace(',', '')))
print(df.info())

total_nobel_by_country = df.groupby('Country')['Nobel Prices'].sum()
sorted_total_nobel_by_country = total_nobel_by_country.sort_values(ascending=False)

print("\nTotal Nobel Prizes by country", sorted_total_nobel_by_country)

sorted_total_nobel_nonzero = sorted_total_nobel_by_country[sorted_total_nobel_by_country !=0]
print("\nTotal nobel prizes by country, excluding countries with zero nobel prizes")



