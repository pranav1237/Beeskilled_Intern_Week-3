# Data Analyst Course — Week 3 Assignment

This project covers Python/Pandas data wrangling and basic visualization. **The supplied course ZIP contained only the assignment brief, not an actual dataset or detailed rubric**, so `data/messy_sales.csv` is a synthetic practice dataset designed to demonstrate the requested tasks. Replace it with your instructor's dataset if one exists.

## Run it
Install Python 3.10+, then run:
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python clean_sales.py
```

## Assignment requirements covered
- Read a CSV into Pandas and inspect data quality (also demonstrated in the notebook).
- Normalize inconsistent whitespace/capitalization.
- Parse dates and numeric fields safely; handle missing/invalid values.
- Filter invalid rows and create a paid-orders subset.
- Create `revenue`, `order_month`, and `is_paid` columns.
- Group and summarize by status.
- Create Matplotlib/Seaborn bar and line charts.

## Output files
`outputs/cleaned_sales.csv`, `outputs/paid_orders.csv`, `outputs/summary_by_status.csv`, `outputs/paid_revenue_by_region.png`, `outputs/paid_revenue_by_month.png`.

## Cleaning decisions
Invalid/missing order IDs, dates, quantities, or prices are removed; non-positive quantities/prices are excluded; duplicate order IDs retain their first record. Missing customer/email values are labeled `Unknown`/`Not provided`. Pending/cancelled/returned orders remain in the cleaned dataset; paid revenue is calculated separately. The data is synthetic and for learning only.
