import pandas as pd
from sqlalchemy import create_engine, text

# Load CSV
df = pd.read_csv('cleat_resale_data.csv')

# Create a local SQLite database
engine = create_engine('sqlite:///cleats.db')

# Load data into SQL table
df.to_sql('cleats', engine, if_exists='replace', index=False)
print("Data loaded into database successfully!")

# Run SQL queries
with engine.connect() as conn:

    print("\n=== Top 5 Most Profitable Models ===")
    result = conn.execute(text("""
        SELECT Model, Brand, ROUND(AVG(Profit_Margin_USD), 2) as Avg_Profit
        FROM cleats
        WHERE Condition = 'New'
        GROUP BY Model, Brand
        ORDER BY Avg_Profit DESC
        LIMIT 5
    """))
    for row in result:
        print(row)

    print("\n=== Best Platform for New Cleats ===")
    result = conn.execute(text("""
        SELECT Platform, ROUND(AVG(Profit_Margin_USD), 2) as Avg_Profit,
               ROUND(AVG(Days_Listed), 1) as Avg_Days
        FROM cleats
        WHERE Condition = 'New'
        GROUP BY Platform
        ORDER BY Avg_Profit DESC
    """))
    for row in result:
        print(row)