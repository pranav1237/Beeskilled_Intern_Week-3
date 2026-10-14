from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'/'messy_sales.csv'; OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
def clean_data(raw):
    df=raw.copy(); df.columns=df.columns.str.strip().str.lower()
    for c in ['customer','region','product','status','email']: df[c]=df[c].astype('string').str.strip()
    for c in ['region','product','status']: df[c]=df[c].str.title()
    df['customer']=df['customer'].replace('',pd.NA); df['email']=df['email'].replace('',pd.NA)
    df['order_date']=pd.to_datetime(df['order_date'],errors='coerce'); df['quantity']=pd.to_numeric(df['quantity'],errors='coerce'); df['unit_price']=pd.to_numeric(df['unit_price'],errors='coerce')
    df['order_id']=df['order_id'].astype('string').str.strip(); df=df.dropna(subset=['order_id','order_date','quantity','unit_price'])
    df=df[(df.quantity>0)&(df.unit_price>0)].drop_duplicates('order_id',keep='first')
    df['customer']=df.customer.fillna('Unknown'); df['email']=df.email.fillna('Not provided')
    df['revenue']=df.quantity*df.unit_price; df['order_month']=df.order_date.dt.to_period('M').astype(str); df['is_paid']=df.status.eq('Paid')
    return df.sort_values(['order_date','order_id']).reset_index(drop=True)
def main():
    raw=pd.read_csv(DATA); df=clean_data(raw); paid=df[df.is_paid].copy()
    df.to_csv(OUT/'cleaned_sales.csv',index=False); paid.to_csv(OUT/'paid_orders.csv',index=False)
    summary=df.groupby('status').agg(order_count=('order_id','count'),total_revenue=('revenue','sum')).reset_index(); summary.to_csv(OUT/'summary_by_status.csv',index=False)
    sns.set_theme(style='whitegrid'); by_region=paid.groupby('region',as_index=False).revenue.sum()
    plt.figure(figsize=(8,5)); sns.barplot(data=by_region,x='region',y='revenue',color='steelblue'); plt.title('Paid Revenue by Region'); plt.tight_layout(); plt.savefig(OUT/'paid_revenue_by_region.png',dpi=160); plt.close()
    by_month=paid.groupby('order_month',as_index=False).revenue.sum()
    plt.figure(figsize=(8,5)); sns.lineplot(data=by_month,x='order_month',y='revenue',marker='o',color='steelblue'); plt.title('Paid Revenue by Month'); plt.xticks(rotation=30); plt.tight_layout(); plt.savefig(OUT/'paid_revenue_by_month.png',dpi=160); plt.close()
    print(f'Raw rows: {len(raw)} | Clean rows: {len(df)} | Paid orders: {len(paid)}'); print(f'Total cleaned revenue: {df.revenue.sum():,.2f} | Paid revenue: {paid.revenue.sum():,.2f}')
if __name__=='__main__': main()
