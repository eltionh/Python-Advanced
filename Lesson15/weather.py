import pandas as pd
import matplotlib.pyplot as plt


file_path = 'weather_tokyo_data.csv'
df = pd.read_csv(file_path)


df['Date'] = pd.to_datetime(df['year'].astype(str) + '/' + df['day'].astype(str), errors='coerce')
df.set_index('Date', inplace=True)
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
df.dropna(subset=['temperature'], inplace=True)



overall_avg = df['temperature'].mean()
print(f"The Average Temperature: {overall_avg:.2f}°C")
print("-" * 30)


monthly_avg_series = df['temperature'].resample('ME').mean()
monthly_avg_data = (
    monthly_avg_series.groupby(monthly_avg_series.index.month_name())
    .mean()
    .reindex(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
)


print("Average Temperature per Month:")
print(monthly_avg_data.to_string(float_format="%.2f"))


plt.figure(figsize=(10, 6))


monthly_avg_data.plot(kind='bar', color='gray')

plt.title('Monthly Average Temperature', fontsize=17)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Average Temperature (°C)', fontsize=15)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


max_temp = df['temperature'].max()
min_temp = df['temperature'].min()


hottest_day = df[df['temperature'] == max_temp]
coldest_day = df[df['temperature'] == min_temp]

hottest_date = hottest_day.index[0].date()
coldest_date = coldest_day.index[0].date()

print(f"Highest Temperature (max()): {max_temp:.2f}°C on {hottest_date}")
print(f"Lowest Temperature (min()): {min_temp:.2f}°C on {coldest_date}")

