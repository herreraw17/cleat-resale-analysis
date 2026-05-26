import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleat_resale_data.csv')

# 1. Average profit margin by brand
print("=== Average Profit Margin by Brand ===")
brand_profit = df.groupby('Brand')['Profit_Margin_USD'].mean().sort_values(ascending=False)
print(brand_profit)

# 2. Average days listed by platform
print("\n=== Average Days Listed by Platform ===")
platform_speed = df.groupby('Platform')['Days_Listed'].mean().sort_values()
print(platform_speed)

# 3. Best selling condition
print("\n=== Average Profit by Condition ===")
condition_profit = df.groupby('Condition')['Profit_Margin_USD'].mean().sort_values(ascending=False)
print(condition_profit)

# Bar chart - Average profit by brand
brand_profit.plot(kind='bar', color='steelblue', figsize=(8,5))
plt.title('Average Profit Margin by Brand')
plt.xlabel('Brand')
plt.ylabel('Avg Profit (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('profit_by_brand.png')
plt.show()

# Bar chart - Average days listed by platform
platform_speed.plot(kind='bar', color='green', figsize=(8,5))
plt.title('Average Days Listed by Platform')
plt.xlabel('Platform')
plt.ylabel('Avg Days')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('days_by_platform.png')
plt.show()

# Bar chart - Average profit by condition
condition_profit.plot(kind='bar', color='orange', figsize=(8,5))
plt.title('Average Profit by Condition')
plt.xlabel('Condition')
plt.ylabel('Avg Profit (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('profit_by_condition.png')
plt.show()