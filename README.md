# Soccer Cleat Resale Market Analysis

## Overview
An analysis of the soccer cleat resale market using Python, SQL, and data visualization. 
This project explores which brands, platforms, and conditions yield the highest profit margins for resellers.

## Key Findings
- **Nike** cleats have the best average profit margin in the resale market
- **StockX** sells cleats the fastest at an average of 5.3 days listed
- **New** condition cleats are the only ones that consistently turn a profit (+$22 avg)
- **Used** cleats lose an average of $65 — not worth reselling

## Tools Used
- Python (pandas, matplotlib)
- SQL (SQLite via SQLAlchemy)
- VS Code
- GitHub

## Files
- `analysis.py` — data exploration and visualizations
- `database.py` — SQL database creation and queries
- `cleat_resale_data.csv` — custom dataset built from Mercari and StockX listings
- `profit_by_brand.png` — average profit margin by brand
- `days_by_platform.png` — average days listed by platform
- `profit_by_condition.png` — average profit by condition

## How to Run
1. Clone the repo
2. Install dependencies: `pip install pandas matplotlib sqlalchemy`
3. Run `python analysis.py` for charts
4. Run `python database.py` for SQL analysis